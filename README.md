## In one sentence, what this file does
High-level overview of the Alta monorepo, its structure, and setup instructions.

## Monorepo Layout

This repository utilizes a monorepo structure, housing various applications and shared libraries within the `alta-monorepo/` directory. This approach helps in managing dependencies and streamlining development across multiple projects.

### `alta-monorepo/`

This is the core directory containing all company-specific tools and libraries.

#### `alta-monorepo/apps/`

This directory contains standalone applications. Each application typically has its own README file with specific instructions.

*   **`document-assembly/`**: Combines templates and data to generate final documents.
*   **`estimations/`**: A collection of tools related to project estimations.
    *   **`da-lead-scraping/`**: Gathers potential lead data from websites.
    *   **`estimation-tool/`**: Helps in calculating project costs quickly.
    *   **`folder-automation/`**: Sets up client job folders with template documents.
    *   **`inventory-sql-db/`**: Manages inventory data using a simple SQL database.
    *   **`quotation-pipeline/`**: Processes incoming quote requests.
*   **`operations/`**: Contains tools for streamlining operational tasks.
    *   **`job-scheduler/`**: Runs recurring tasks for the operations team.
    *   **`operations-pipeline/`**: Chains together routine tasks for operations.
*   **`scaffold-audit/`**: Checks scaffold drawings against safety rules.

#### `alta-monorepo/libs/`

This directory contains shared libraries used by one or more applications.

*   **`powershell/AltaUtils/`**: Shared PowerShell utilities. (General purpose PowerShell functions for Alta projects.)
*   **`python/alta_utils/`**: Shared Python utilities. (General purpose Python functions for Alta projects.)

#### Other notable directories within `alta-monorepo/`:

*   **`docs/`**: Contains documentation for the monorepo.
*   **`infra/`**: Likely contains infrastructure-related code (e.g., deployment scripts).
*   **`scripts/`**: Contains various scripts, possibly for development or CI/CD.

## Glossary

- **DXF** – Drawing Exchange Format used by many CAD programs.
- **Audit** – Automatic check of a drawing against safety rules.
- **Stub** – Lightweight placeholder module used when a dependency is missing.
- **Template** – A starter document copied into each new job folder.
- **GUI** – Graphical User Interface that lets you interact via buttons instead of the command line.

## Getting Started

This monorepo contains multiple applications and libraries. The general workflow for working with a specific application is as follows:

1.  **Prerequisites**:
    *   Ensure you have Python installed (if working with Python-based applications).
    *   Ensure you have PowerShell installed (if working with PowerShell-based scripts or libraries).
    *   Other application-specific prerequisites might be mentioned in their respective READMEs.
    *   For developers contributing to Python packages or working on shared libraries, consider installing the root package in editable mode from the repository root after cloning and setting up your primary virtual environment:
        ```powershell
        # From the root of the monorepo
        pip install -e . 
        ```
        This can be useful if you're working on shared libraries and applications simultaneously. Some applications might also require specific versions of tools, like `pythonocc-core` for 3D features:
        ```powershell
        pip install pythonocc-core==7.6
        ```
        Always check the application's specific `README.md` or `requirements.txt`.


2.  **Clone the Repository**:
    ```bash
    git clone <your_repository_url_here>
    cd <repository_root_folder_name>
    ```

3.  **Navigate to an Application**:
    Most applications reside in the `alta-monorepo/apps/` directory. Navigate to the specific application you want to work with.
    ```bash
    cd alta-monorepo/apps/<application_name> # Replace <application_name> with the actual directory name
    ```

4.  **Follow Application-Specific Instructions**:
    Each application directory (e.g., `alta-monorepo/apps/scaffold-audit/`) should contain its own `README.md` file. These READMEs provide detailed setup, build, run, and test instructions for that specific application.

    **Example: `scaffold-audit`**
    *   Navigate to `alta-monorepo/apps/scaffold-audit/`.
    *   Follow the setup instructions in its `README.md`. This typically involves creating a Python virtual environment and installing dependencies:
        ```powershell
        # From within alta-monorepo/apps/scaffold-audit/ (or the monorepo root for a shared venv)
        python -m venv .venv
        .venv\Scripts\Activate.ps1 # On Windows
        # source .venv/bin/activate # On macOS/Linux
        pip install -r requirements.txt # Or similar (e.g., pip install -e .)
        ```
    *   Then, you can run the application as described in its README, e.g.:
        ```powershell
        python -m scaffold_audit path\to\drawing.dxf
        ```

    **Example: `folder-automation`**
    *   Navigate to `alta-monorepo/apps/estimations/folder-automation/`.
    *   Follow its specific setup instructions (virtual environment, dependencies).
    *   To create a job folder using the command line:
        ```powershell
        # Provide paths if the defaults do not match your system
        python -m folder_automation "ClientName" "JobName" \
          --base-dir C:\path\to\Clients --template-dir C:\path\to\Templates
        ```
    *   To launch the graphical interface:
        ```powershell
        python -m folder_automation.gui
        ```
    *   To build a Windows `.exe` (requires `pyinstaller`, ensure it's installed: `pip install pyinstaller`):
        ```powershell
        python -m folder_automation.build_exe
        ```
    *   After building, run the executable without Python from the `dist` directory:
        ```powershell
        dist\folder_automation_gui.exe
        ```
    *   If you see an `ImportError` running `build_exe.py` directly, run it as a module: `python -m folder_automation.build_exe`.


5.  **Shared Libraries**:
    Shared libraries are located in `alta-monorepo/libs/`. These are typically used as dependencies by the applications. If you are developing a shared library, refer to any specific instructions within its directory.

6.  **Running Tests**:
    To run tests for a specific application, navigate to its directory and follow the instructions in its README. Many Python projects use `pytest`.

    For example, to run tests for `scaffold-audit`:
    *   The root directory contains a `pytest.py` script that can be used:
        ```powershell
        # From the root of the monorepo
        python pytest.py alta-monorepo/apps/scaffold-audit/tests
        ```
    *   Alternatively, if `pytest` is installed and the application is structured for it, you might run (from within `alta-monorepo/apps/scaffold-audit/`):
        ```bash
        pytest tests/
        ```
    A general way to run tests from the root of `alta-monorepo` for many Python apps (if they are structured to support it and `pytest` is installed globally or in a shared virtual environment) might be:
    ```powershell
    # From within alta-monorepo/
    pytest
    ```
    However, it's best to consult the application-specific README for the recommended testing instructions.

## Contributing

Contributions are welcome! Whether it's fixing a bug, improving documentation, or adding a new feature, your help is appreciated. Here's how you can contribute:

### Development Workflow

1.  **Set up your environment**: Follow the instructions in the "Getting Started" section to clone the repository and set up any necessary tools for the specific application or library you intend to work on.
2.  **Branching**: Create a new branch for your changes from the `main` branch. A good branch naming convention is `feature/<your-feature-name>` or `fix/<bug-name>`.
3.  **Make your changes**: Write your code, ensuring you adhere to the coding standards outlined below.
4.  **Testing**:
    *   Add relevant automated tests for your changes.
    *   Ensure all tests pass before committing. For Python projects, this typically involves running `pytest` from the application's directory (e.g., `alta-monorepo/apps/scaffold-audit/tests/`).
    *   The specific command `python pytest.py alta-monorepo/apps/scaffold-audit/tests` is used for the scaffold-audit tool.
    *   For PowerShell, `Pester` is the preferred testing framework.
    *   Run `ruff --fix` (for Python projects) before committing to auto-format and lint your code.
5.  **Commit your changes**:
    *   This repository uses **Conventional Commits**. Ensure your commit messages follow this format (e.g., `feat: add new login endpoint`, `fix: correct calculation error in estimator`). This is enforced by `commitlint`.
    *   Example commit types: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `perf:`, `test:`, `build:`, `ci:`, `chore:`.
6.  **Rebase**: Before submitting a pull request, rebase your branch onto the latest `main` branch to ensure a clean merge history.
    ```bash
    git fetch origin
    git rebase origin/main
    ```
7.  **Submit a Pull Request (PR)**:
    *   Push your branch to the remote repository.
    *   Create a Pull Request against the `main` branch.
    *   Provide a clear description of the changes made and why.
    *   Aim to keep PRs focused and relatively small (e.g., under 300 lines of code if possible, as suggested in internal guidelines).
8.  **Update Documentation**: If you add a new tool, module, or make significant changes to an existing one, please update or create the relevant `README.md` file.

### Coding Standards

*   **General**:
    *   Write clear, understandable code with appropriate comments.
    *   Add docstrings to functions and modules, including examples where helpful.
    *   Prefer creating shared, reusable code in the `alta-monorepo/libs/` directory rather than duplicating logic.
*   **Python**:
    *   Follow PEP 8 guidelines.
    *   Use Black for code formatting (line length 120, target Python 3.11 as per `pyproject.toml`).
    *   Use Ruff for linting.
*   **PowerShell**:
    *   Adhere to common PowerShell styling conventions.
*   **TypeScript/JavaScript** (if working on Node.js projects within the monorepo, as hinted by `node_modules` and some config files):
    *   Use Prettier for formatting (usually with default settings).
    *   Follow standard linting practices (e.g., ESLint).

### Questions or Suggestions?

If you have any questions or want to discuss an idea, feel free to open an issue on the repository.

## License

The licensing terms for this project have not yet been specified. Please refer to the project maintainers for more information.
