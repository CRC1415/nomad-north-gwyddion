# Welcome to the nomad-north-gwyddion documentation

`nomad-north-gwyddion` is a NOMAD NORTH plugin that packages [Gwyddion](https://gwyddion.net/){:target="_blank" rel="noopener"}, a free scanning probe microscopy (SPM) data processing software, as a ready-to-launch desktop tool inside a NOMAD Oasis.

## Introduction

[Gwyddion](https://gwyddion.net/){:target="_blank" rel="noopener"} is an open-source application for visualizing and analyzing data from scanning probe microscopy techniques (AFM, STM, and related methods), as well as some other 2D data such as SEM or profilometry images. See the [research article about the software](https://doi.org/10.2478/s11534-011-0096-2){:target="_blank" rel="noopener"} for background.

This plugin registers Gwyddion as a NORTH tool: a full desktop environment, built on FAIRmat's [`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base){:target="_blank" rel="noopener"} image, that a NOMAD Oasis can launch directly against files in an upload.

<div markdown="block" class="home-grid">
<div markdown="block">

### Tutorial

A short walkthrough of launching Gwyddion on a file inside a NOMAD Oasis.

- [Tutorial](tutorial/tutorial.md)

</div>
<div markdown="block">

### How-to guides

How-to guides provide step-by-step instructions for a wide range of tasks, with the overarching topics:

- [How-to guides > Install this Plugin](how_to/install_this_plugin.md)
- [How-to guides > Use this Plugin](how_to/use_this_plugin.md)
- [How-to guides > Contribute to this Plugin](how_to/contribute_to_this_plugin.md)
- [How-to guides > Contribute to the Documentation](how_to/contribute_to_the_documentation.md)

</div>

<div markdown="block">

### Explanation

The [Explanation](explanation/explanation.md) section covers what a NORTH tool is in general and how this particular one is built.

</div>
<div markdown="block">

### Reference

The [Reference](reference/references.md) section lists the tool's configuration (file extensions, mount path, image) and the project's maintainers.

</div>
</div>
