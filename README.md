[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/actions/workflows/actions.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/actions/workflows/publish.yml/badge.svg)
![](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/actions/workflows/mkdocs-deploy.yml/badge.svg)
![](https://img.shields.io/pypi/pyversions/nomad-north-gwyddion)
![](https://img.shields.io/pypi/l/nomad-north-gwyddion)
![](https://img.shields.io/pypi/v/nomad-north-gwyddion)

# nomad-north-gwyddion

A NOMAD NORTH plugin for [Gwyddion](https://gwyddion.net/), a free scanning probe microscopy data processing software.

This `nomad` plugin was generated with `Cookiecutter` along with `@nomad`'s [`cookiecutter-nomad-plugin`](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin) template.

## Docs

More information about this plugin is available in the [documentation](https://fairmat-nfdi.github.io/nomad-north-gwyddion/), including how to
[install](https://fairmat-nfdi.github.io/nomad-north-gwyddion/how_to/install_this_plugin/) and
[contribute to](https://fairmat-nfdi.github.io/nomad-north-gwyddion/how_to/contribute_to_this_plugin/) this plugin.

## Adding this plugin to NOMAD

Currently, NOMAD has two distinct flavors that are relevant depending on your role as an user:
1. [A NOMAD Oasis](#adding-this-plugin-in-your-nomad-oasis): any user with a NOMAD Oasis instance.
2. [Local NOMAD installation and the source code of NOMAD](#adding-this-plugin-in-your-local-nomad-installation-and-the-source-code-of-nomad): internal developers.

### Adding this plugin in your NOMAD Oasis

Read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/oasis/plugins_install.html) for all details on how to deploy the plugin on your NOMAD instance.

### Adding this plugin in your local NOMAD installation and the source code of NOMAD

We now recommend using the dedicated [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev) repository to simplify the process. Please refer to that repository for detailed instructions.

## Publish note

In our Python package publishing workflow, before building the package, we update the image tag in the [NORTHTool](./src/nomad_north_gwyddion/north_tools/__init__.py) entry point to the latest release version of the image (e.g., `v0.1.5`), and then publish the package to PyPI.

However, the updated image tag in `NORTHTool` is not pushed back to the GitHub repository. Therefore, the image tag in the GitHub repository always remains set to `main`, even when you check out a specific release tag. For this reason, we recommend installing the plugin from [PyPI](https://pypi.org/), where the entry point always contains the correct image tag corresponding to the release.

If you download a ZIP file of a specific release from GitHub, the image tag in the entry point will still be set to `main`, which is not correct. In that case, you can either manually update the image tag in the entry point to the correct release version (e.g., `v0.1.5`), or install the plugin directly from PyPI.

### Template update

We use [`cruft`](https://github.com/cruft/cruft) to update the project based on template changes. To run the check for updates locally, run `cruft update` in the root of the project. More details see the instructions on [`cruft` website](https://cruft.github.io/cruft/#updating-a-project).

## Main contributors
| Name | E-mail     |
|------|------------|
| Lukas Pielsticker | [lukas.pielsticker@physik.hu-berlin.de](mailto:lukas.pielsticker@physik.hu-berlin.de)
| Ron Dockhorn | [ron.dockhorn@tu-dresden.de](mailto:ron.dockhorn@tu-dresden.de)
