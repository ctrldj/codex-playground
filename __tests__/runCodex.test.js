jest.mock('child_process', () => ({
  exec: jest.fn((cmd, options, cb) => cb(null, 'out', ''))
}));

const runCodex = require('../runCodex');

const { exec } = require('child_process');

test('runCodex executes codex command in cwd', async () => {
  const cwd = process.cwd();
  await runCodex('foo');
  expect(exec).toHaveBeenCalledWith(
    'codex "foo"',
    { cwd },
    expect.any(Function)
  );
});
