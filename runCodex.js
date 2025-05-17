const { exec } = require("child_process");

function runCodex(prompt, cwd = process.cwd()) {
  return new Promise((resolve, reject) => {
    exec(`codex "${prompt}"`, { cwd }, (err, stdout, stderr) => {
      if (err) {
        const error = new Error(stderr || err.message);
        error.code = err.code;
        return reject(error);
      }
      resolve(stdout);
    });
  });
}

// Run it once
runCodex("Create a README that says hello", "C:/Projects/codex-playground")
  .then(output => console.log("Codex said:\n", output))
  .catch(err => console.error("Codex failed:\n", err));
