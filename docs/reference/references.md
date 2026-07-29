# References

## `NORTHTool` configuration

Defined in [`src/nomad_north_gwyddion/north_tools/__init__.py`](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/blob/main/src/nomad_north_gwyddion/north_tools/__init__.py){:target="_blank" rel="noopener"}. See the [`NORTHTool` reference](https://fairmat-nfdi.github.io/nomad-docs/reference/config.html#northtool){:target="_blank" rel="noopener"} for the full field-by-field documentation; the values used here are:

| Field | Value | Meaning |
|---|---|---|
| `image` | `ghcr.io/fairmat-nfdi/nomad-north-gwyddion:main` on `main`; a version tag (e.g. `v0.1.6`) once published to PyPI | Container image, see [Explanation > Why install from PyPI](../explanation/explanation.md#why-install-from-pypi) |
| `file_extensions` | `dm4`, `tif`, `tiff`, `wip`, `wit`, `spm`, `ibw` | Which uploaded files offer this tool |
| `default_url` | `/desktop` | Opens straight into the desktop session |
| `mount_path` | `/home/jovyan` | Where the triggering upload is mounted inside the container |
| `path_prefix` | `lab/tree` | URL path prefix used to address files within the mount |
| `with_path` | `true` | The launched file's path is passed through to the tool |
| `image_pull_policy` | `Always` | The image is re-pulled on every launch |
| `privileged` | `false` | The container does not run with elevated privileges |
| `display_name` | `gwyddion` | Name shown in NORTH's tool list |

## Entry point

Registered under `[project.entry-points.'nomad.plugin']` in `pyproject.toml`:

```toml
gwyddion = "nomad_north_gwyddion.north_tools:gwyddion"
```

## Base image

The container builds on [`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base){:target="_blank" rel="noopener"} (`ghcr.io/fairmat-nfdi/nomad-north-desktop-base`), which provides the xfce desktop and noVNC session that NORTH connects to.

## Further reading

- [Gwyddion](https://gwyddion.net/){:target="_blank" rel="noopener"} -- project homepage
- [Gwyddion user guide](https://gwyddion.net/documentation/user-guide-en/){:target="_blank" rel="noopener"}
- [Gwyddion supported file formats](https://gwyddion.net/documentation/user-guide-en/file-formats.html){:target="_blank" rel="noopener"}
- [Nečas, D. & Klapetek, P. (2012), *Gwyddion: an open-source software for SPM data analysis*](https://doi.org/10.2478/s11534-011-0096-2){:target="_blank" rel="noopener"} -- research article about the software
- [NOMAD Docs > Explanation > NOMAD Remote Tools Hub (NORTH)](https://fairmat-nfdi.github.io/nomad-docs/explanation/north.html){:target="_blank" rel="noopener"}
- [NOMAD Docs > How-to > How to create a NORTH tool](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html){:target="_blank" rel="noopener"}
