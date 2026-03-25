# flake-uv-template

Copier template for Python projects using Nix + uv. Generated project files live
under `template/` (copier `_subdirectory: template`). The root is a plain Nix
flake with a dev shell — not a Python project itself.

## Tools

- **copier**: Template engine that generates projects from this repo. Docs:
  https://copier.readthedocs.io/
- **prek**: Fast, Rust-based git hooks manager (drop-in alternative to
  pre-commit). Uses `prek.toml`. Docs: https://prek.j178.dev/ Repo:
  https://github.com/j178/prek

  **prek.toml structure:**
  ```toml
  [[repos]]
  repo = "builtin"          # fast, no-network Rust-native hooks
  hooks = [{id = "..."}]

  [[repos]]
  repo = "local"            # custom hooks
  hooks = [{id = "...", name = "...", entry = "...", language = "..."}]
  ```

  **Top-level keys:** `repos` (required), `files`, `exclude`, `fail_fast`,
  `default_language_version`, `default_stages`, `minimum_prek_version`

  **Hook options:** `id`, `name`, `entry`, `language`, `args`, `files`,
  `exclude`, `types`, `stages`, `always_run`, `pass_filenames`, `priority`
  (prek-only), `env` (prek-only)

  **Built-in hooks** (`repo = "builtin"`, no network/env needed):
  `trailing-whitespace`, `end-of-file-fixer`, `check-added-large-files`,
  `check-case-conflict`, `check-merge-conflict`, `check-toml`, `check-yaml`,
  `check-json`, `check-json5`, `check-xml`, `check-symlinks`,
  `detect-private-key`, `no-commit-to-branch`, `mixed-line-ending`,
  `pretty-format-json`, `check-illegal-windows-names`
- **uv**: Python package and project manager. Used in generated projects.
- **nixfmt / statix / deadnix**: Nix formatting and linting tools, available in
  the dev shell.

## Dev workflow

Enter the dev shell:

```
nix develop
```

Generate a project from the template (for testing):

```
copier copy . /path/to/output
```

## Conventions

- Changes to the template go under `template/`, not the root.
- The root `flake.nix` and `copier.yml` are repo infrastructure, not part of the
  generated project.
