# Tutorial

This is a short walkthrough of launching Gwyddion on a scanning probe microscopy file from inside a NOMAD Oasis. It assumes the plugin is already installed and enabled (see [How-to guides > Install this Plugin](../how_to/install_this_plugin.md)).

## Prerequisites

- Access to a NOMAD Oasis with this plugin enabled and NORTH running.
- An upload containing at least one file with one of the supported extensions: `dm4`, `tif`, `tiff`, `wip`, `wit`, `spm`, or `ibw`.

## Steps

1. **Open your upload.** In the NOMAD GUI, navigate to the upload that contains the SPM file you want to inspect.
2. **Launch Gwyddion.** From the upload's file browser, open the tool launcher for that file (or the upload's list of available NORTH tools) and select **gwyddion**. The first launch pulls and starts the container, which can take a moment.
3. **Work in the desktop.** NORTH opens a remote desktop session with Gwyddion already running and your upload's files mounted and visible in the file browser, so you can open the file directly from within Gwyddion.
4. **Use Gwyddion as usual**: load the data, apply levelling/filtering, and export processed images or data as you would with a local Gwyddion installation. See the [Gwyddion user guide](https://gwyddion.net/documentation/user-guide-en/){:target="_blank" rel="noopener"} for how to use the software itself -- this plugin only provides the environment, not a guided workflow through it.
5. **Save results back to the upload.** Files you save under the mounted upload directory become part of the upload and can be reprocessed like any other upload file.

!!! tip "Important"
    Anything you save outside the mounted upload directory is lost once the container session ends.
