import os
import tempfile
import shutil
import timeit
import create_job


def setup_env(tmpdir):
    tpl = os.path.join(tmpdir, 'templates')
    cli = os.path.join(tmpdir, 'clients')
    sp = os.path.join(tmpdir, 'sharepoint')
    os.makedirs(tpl)
    os.makedirs(cli)
    os.makedirs(sp)
    for name in create_job.TEMPLATES:
        open(os.path.join(tpl, name), 'w').close()
    create_job.TEMPLATE_DIR = tpl
    create_job.CLIENTS_DIR = cli
    create_job.SHAREPOINT_DIR = sp
    return tpl, cli, sp


def test_create_job_success(tmp_path):
    tpl, cli, sp = setup_env(tmp_path)
    msg = create_job.create_job('Acme', 'ALT-N-9999 - Demo', sharepoint=True)
    job_path = os.path.join(cli, 'Acme', 'Jobs', 'ALT-N-9999 - Demo')
    sp_path = os.path.join(sp, 'Acme', 'Jobs', 'ALT-N-9999 - Demo')
    assert os.path.isdir(job_path)
    assert os.path.isdir(sp_path)
    for dest in create_job.TEMPLATES.values():
        assert os.path.isfile(os.path.join(job_path, dest))
        assert os.path.isfile(os.path.join(sp_path, dest))
    assert 'Created job at' in msg


def test_job_already_exists(tmp_path):
    tpl, cli, sp = setup_env(tmp_path)
    create_job.create_job('Acme', 'ALT-N-9999 - Demo')
    msg = create_job.create_job('Acme', 'ALT-N-9999 - Demo')
    assert 'Job already exists' in msg


def test_benchmark(tmp_path):
    tpl, cli, _ = setup_env(tmp_path)
    def run():
        create_job.create_job('Acme', 'ALT-N-9999 - Demo')
    timings = timeit.repeat(run, repeat=3, number=100)
    assert min(timings) < 1.0
