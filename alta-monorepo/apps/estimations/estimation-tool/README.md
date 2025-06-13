## In one sentence, what this folder does
This folder contains the **estimation-tool**. It calculates scaffold quotes.

### Setup steps
- Follow the virtual environment instructions in the root `README.md`.
- No extra packages are required for this tool.

### How to run
```powershell
python -m estimation_tool 10 5
```
This example assumes each component weighs 10kg and you need 5 of them.

### Running the tests
```powershell
python pytest.py alta-monorepo/apps/estimations/estimation-tool/tests
```

### Glossary
- **Component** – A single scaffolding item such as a tube or board.
- **Quote** – Calculated price sent to a customer.
