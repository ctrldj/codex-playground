"""Minimal pytest replacement for this environment."""
import importlib.util
import inspect
import pathlib
import sys
import tempfile
import traceback


def main() -> None:
    root = pathlib.Path('tests')
    files = sorted(root.rglob('test_*.py'))
    failures = 0
    for path in files:
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for name in dir(module):
            obj = getattr(module, name)
            if name.startswith('test_') and callable(obj):
                sig = inspect.signature(obj)
                kwargs = {}
                if 'tmp_path' in sig.parameters:
                    with tempfile.TemporaryDirectory() as td:
                        kwargs['tmp_path'] = pathlib.Path(td)
                        try:
                            obj(**kwargs)
                            print(f'{path}:{name} PASSED')
                        except Exception:
                            failures += 1
                            print(f'{path}:{name} FAILED')
                            traceback.print_exc()
                else:
                    try:
                        obj()
                        print(f'{path}:{name} PASSED')
                    except Exception:
                        failures += 1
                        print(f'{path}:{name} FAILED')
                        traceback.print_exc()
    if failures:
        sys.exit(1)


if __name__ == '__main__':
    main()
