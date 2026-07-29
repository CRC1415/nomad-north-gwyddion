# Install This Plugin

## In your NOMAD Oasis

If your Oasis is built from [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"} (the standard way to run a NOMAD Oasis), plugins are configured through that distro project's `pyproject.toml`, which its CI pipeline uses to build the NOMAD Docker image your Oasis actually runs -- only plugins listed there end up installed and available. See the [template README > Adding a plugin](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#adding-a-plugin){:target="_blank" rel="noopener"} for the exact steps, and the general [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/plugins/plugins.html#add-a-plugin-to-your-nomad){:target="_blank" rel="noopener"} for background. In short:

1. Add `nomad-north-gwyddion` as a dependency in your distro project's `pyproject.toml`, and rebuild/redeploy the Oasis image so it's actually installed.
2. That's it -- plugin entry points are loaded automatically once the package is installed. Only add anything to `nomad.yaml`'s `plugins.entry_points` section if you need to override the default behavior:
     - `exclude`, to turn the tool off despite it being installed;
     - a non-empty `include` allowlist, which (if your `nomad.yaml` already uses one for other plugins) must then also list `"nomad_north_gwyddion.north_tools:gwyddion"`, since a non-empty allowlist means everything not listed stays disabled;
     - `options`, to override one of the `NORTHTool` fields listed in [Reference](../reference/references.md#northtool-configuration) (e.g. pin a different image tag).
3. Restart the Oasis. The **gwyddion** tool then appears in NORTH's tool launcher for files with a matching extension -- see [Use this Plugin](use_this_plugin.md). No separate Docker build step is needed on your side: NORTH pulls the tool's own container image (`ghcr.io/fairmat-nfdi/nomad-north-gwyddion`) automatically the first time someone launches it.

We recommend installing from [PyPI](https://pypi.org/project/nomad-north-gwyddion/){:target="_blank" rel="noopener"} rather than a GitHub checkout or release ZIP -- see [Explanation > Why install from PyPI](../explanation/explanation.md#why-install-from-pypi) for why that distinction matters for this particular plugin.

## Development install in `nomad-distro-dev`

If you want to make changes to this NOMAD plugin or if you want to work on NOMAD core or another plugin against a live Gwyddion NORTH tool (rather than running a real Oasis), it is recommended to use [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}. Follow the steps in the `nomad-distro-dev` README to add `nomad-north-gwyddion` as a (development) plugin.