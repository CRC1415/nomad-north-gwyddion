# Explanation

## What this plugin is (and isn't)

`nomad-north-gwyddion` is a thin wrapper: it does not implement any SPM data processing itself. All it does is package the existing [Gwyddion](https://gwyddion.net/){:target="_blank" rel="noopener"} application into a container and register that container with NOMAD as a [NORTH](https://fairmat-nfdi.github.io/nomad-docs/explanation/north.html){:target="_blank" rel="noopener"} tool, so it can be launched, isolated and reproducibly, directly against files already stored in a NOMAD upload -- without anyone having to install Gwyddion locally or move data out of NOMAD to work with it.

There is deliberately no NOMAD schema, parser, or app in this plugin: Gwyddion's own project files and exports stay Gwyddion's own formats, and nothing here tries to normalize them into NOMAD metadata.

## Why a desktop tool, not a Jupyter tool

Gwyddion is a GUI application (levelling, filtering, and profile tools are used interactively on 2D data), so it is built on FAIRmat's [`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base){:target="_blank" rel="noopener"} image rather than a Jupyter-only base. That base image provides the `xfce` desktop that NORTH needs to expose a full application window in the browser; this plugin's [Dockerfile](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/blob/main/src/nomad_north_gwyddion/north_tools/gwyddion/Dockerfile){:target="_blank" rel="noopener"} only adds the `gwyddion` package itself and an autostart entry (`config/Gwyddion.desktop`) so the application opens automatically when the desktop session starts, instead of leaving the user to find it in a menu.

## Why these file extensions

The `file_extensions` list in the `NORTHTool` configuration (`dm4`, `tif`, `tiff`, `wip`, `wit`, `spm`, `ibw`) drives which files in a NOMAD upload offer "open with gwyddion" -- it is intentionally scoped to formats Gwyddion can actually import (Digital Micrograph, TIFF, WITec, and Asylum Research/Igor Binary Wave, among others; see [Gwyddion's supported file formats](https://gwyddion.net/documentation/user-guide-en/file-formats.html){:target="_blank" rel="noopener"} for the full, much larger list Gwyddion itself supports beyond what's exposed here).

## Why install from PyPI

The publishing workflow bumps the image tag in `NORTHTool` (e.g. to `v0.1.6`) as part of building the release, but that bump is not pushed back to GitHub -- so the entry point on the `main` branch, and in any release tag or ZIP downloaded from GitHub, always resolves to the `:main` image tag rather than the pinned release image. Installing from PyPI is the only way to get an entry point whose image tag actually matches the installed package version; if you must install from a GitHub checkout or ZIP, update the image tag in `north_tools/__init__.py` by hand first.
