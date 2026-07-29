# Contribute to This Plugin

This guide walks through setting up a working environment for developing `nomad-north-gwyddion`.

??? info "Structure of this repository"
    The plugin's Python side (the `NORTHTool`/`NorthToolEntryPoint` definition) lives in
    [`src/nomad_north_gwyddion`](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/tree/main/src/nomad_north_gwyddion){:target="_blank" rel="noopener"}.
    The container itself -- Dockerfile, autostart config, and icon -- lives in
    [`src/nomad_north_gwyddion/north_tools/gwyddion`](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/tree/main/src/nomad_north_gwyddion/north_tools/gwyddion){:target="_blank" rel="noopener"},
    which has its own [README](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/blob/main/src/nomad_north_gwyddion/north_tools/gwyddion/README.md){:target="_blank" rel="noopener"} covering the Docker side in more detail.

## Setup

It is recommended to use Python 3.11 with a dedicated virtual environment. We recommend [`uv`](https://github.com/astral-sh/uv){:target="_blank" rel="noopener"}, an extremely fast Python package and project manager; a more classical `venv`/`pip` approach works too.

=== "uv"
    `uv` is capable of creating a virtual environment and installing the required Python version at the same time.

    ```bash
    uv venv --python 3.11
    ```

=== "venv"
    Note that you will need to install the Python version manually beforehand.

    ```bash
    python3.11 -m venv .venv
    . .venv/bin/activate
    ```

## Development installation

Clone the repository:

```console
git clone https://github.com/FAIRmat-NFDI/nomad-north-gwyddion.git
cd nomad-north-gwyddion
```

Install the package in editable mode, together with its dev dependencies:

=== "uv"

    ```bash
    uv pip install -e ".[dev]"
    ```

=== "pip"

    ```bash
    pip install --upgrade pip
    pip install -e ".[dev]"
    ```

## Linting, formatting, and pre-commit hooks

We use [Ruff](https://docs.astral.sh/ruff/){:target="_blank" rel="noopener"} for linting/formatting and mypy for type checking. `.pre-commit-config.yaml` also runs pyupgrade, nbstripout, and cspell. We use [`prek`](https://github.com/j178/prek){:target="_blank" rel="noopener"} -- a drop-in, faster reimplementation of `pre-commit` that reads the same config file -- as the runner; it's installed as part of the `dev` extra above, so you just need to enable the hook once per clone:

```console
prek install           # installs the git hook
prek run --all-files   # run all hooks against the whole repo once
```

You can also run Ruff directly:

```console
ruff check .
ruff format . --check
```

If `cspell` flags a real (correctly spelled) word, add it to `.cspell/custom-dictionary.txt`, or regenerate it from the current source/docs:

```console
scripts/generate_custom_dict.sh
```

## Working on the Docker image

If you're changing the [Dockerfile](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/blob/main/src/nomad_north_gwyddion/north_tools/gwyddion/Dockerfile){:target="_blank" rel="noopener"} or the autostart config, build and smoke-test the image locally before opening a PR (from the package root):

```console
docker build -f src/nomad_north_gwyddion/north_tools/gwyddion/Dockerfile \
    -t nomad-north-gwyddion:dev .
docker run -p 8888:8888 nomad-north-gwyddion:dev
```

Then point `NORTHTool.image` in
[`src/nomad_north_gwyddion/north_tools/__init__.py`](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/blob/main/src/nomad_north_gwyddion/north_tools/__init__.py){:target="_blank" rel="noopener"}
at your local tag (e.g. `nomad-north-gwyddion:dev`) to test it end-to-end from within a running NOMAD -- see the [NORTH tools how-to](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html){:target="_blank" rel="noopener"} for details on testing local images. Revert that change before merging: CI (`.github/workflows/publish_north.yml`) builds and publishes the real image on every push to `main`.

## Testing

Unit tests are written with [pytest](https://docs.pytest.org/en/stable/){:target="_blank" rel="noopener"}:

```console
pytest -sv tests
```

## Contributing on GitHub

Commit your changes on a separate branch and open a pull request. CI checks linting, runs the tests, builds the Docker image, and builds the docs; once those pass and a review happens, the PR can be merged.

Changing something in `docs/`? See [How-to guides > Contribute to the Documentation](contribute_to_the_documentation.md) for the writing conventions, how to build the docs locally, and how to add a new page.

### Template updates

This project was generated from, and stays in sync with, FAIRmat's [`cookiecutter-nomad-plugin`](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin){:target="_blank" rel="noopener"} template via [`cruft`](https://github.com/cruft/cruft){:target="_blank" rel="noopener"}. To check for and apply template updates, run `cruft update` in the repository root -- see the [`cruft` documentation](https://cruft.github.io/cruft/#updating-a-project){:target="_blank" rel="noopener"} for details. `.github/*` workflow files are excluded from these updates (`[tool.cruft].skip` in `pyproject.toml`) to avoid permissions issues.

### Releasing

Before tagging a release, the image tag in `NORTHTool` (in `north_tools/__init__.py`) is automatically updated to the version you are about to release (e.g. `v0.1.6`). The publish workflow (used for publishign to PyPI) does not push this change back to GitHub, so the entry point on `main` always points at the `:main` image tag -- see the [project README](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion#publish-note){:target="_blank" rel="noopener"} for why installing from PyPI is recommended over a GitHub checkout.

## Developing this plugin as part of NOMAD

If you're testing this plugin's NORTH integration against a full NOMAD instance -- not just its own unit tests -- use [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}, FAIRmat's development environment for NOMAD and its plugins. See [How-to guides > Install this Plugin](install_this_plugin.md) for how this repo is wired into that workspace.

## Troubleshooting

If you hit an issue with the tool or with setting up the development environment, open a [GitHub issue](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/issues/new){:target="_blank" rel="noopener"}.
