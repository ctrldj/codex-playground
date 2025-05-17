const { exec } = require("child_process");

function runCodex(prompt, cwd = process.cwd()) {
  return new Promise((resolve, reject) => {
    exec(`codex "${prompt}"`, { cwd }, (err, stdout, stderr) => {
      if (err) return reject(stderr);
      resolve(stdout);
    });
  });
}

module.exports = runCodex;

if (require.main === module) {
  runCodex("Create a README that says hello", "C:/Projects/codex-playground")
    .then(output => console.log("Codex said:\n", output))
    .catch(err => console.error("Codex failed:\n", err));
}
