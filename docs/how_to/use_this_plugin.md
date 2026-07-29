# How to Use This Plugin

This plugin can be used in a NOMAD Oasis installation.

## Add This Plugin to Your NOMAD installation

Read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/plugins/plugins.html#add-a-plugin-to-your-nomad){:target="_blank" rel="noopener"} for all details on how to deploy the plugin on your NOMAD instance, or see [Install this Plugin](install_this_plugin.md) for the `nomad-distro-dev` wiring.

## Launching Gwyddion

Once installed, **gwyddion** shows up in NORTH's tool launcher for any file in an upload with one of the following extensions: `dm4`, `tif`, `tiff`, `wip`, `wit`, `spm`, or `ibw`. Selecting it starts a container with:

- the full [Gwyddion](https://gwyddion.net/){:target="_blank" rel="noopener"} desktop application, opened directly (`default_url: /desktop`), with Gwyddion auto-started rather than a bare desktop;
- the triggering upload mounted at `/home/jovyan`, so files in that upload are visible from within Gwyddion's own file browser.

See the [Tutorial](../tutorial/tutorial.md) for a walkthrough, and the [Gwyddion user guide](https://gwyddion.net/documentation/user-guide-en/){:target="_blank" rel="noopener"} and [supported file formats](https://gwyddion.net/documentation/user-guide-en/file-formats.html){:target="_blank" rel="noopener"} for how to use the software itself.

!!! note "Attention"
    Only files saved back under the mounted upload directory are persisted as part of the upload. Anything written elsewhere in the container is lost when the session ends.
