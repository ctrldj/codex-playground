## In one sentence, what this file does
Overview of the Alta monorepo structure for all tools.

# Alta Monorepo

This folder hosts multiple applications and shared libraries for Alta's tooling.

## Setup

- Navigate into the relevant app directory.
- Follow the app-specific README or create one if missing.

## How to run

- Each app in `apps/` should provide a `src/` folder with runnable code.
- Run unit tests with:
  ```powershell
  pytest
  ```

## Glossary

- **Monorepo** – A single repository containing multiple projects.
- **App** – A standalone tool or service under `apps/`.
- **Lib** – Reusable code shared across apps under `libs/`.
