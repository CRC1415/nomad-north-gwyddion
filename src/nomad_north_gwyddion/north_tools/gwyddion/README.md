# gwyddion - NORTH tool

This directory contains the configuration and the Dockerfile for defining the Gwyddion NORTH (NOMAD Remote Tools Hub) tool.

## Quick start

The gwyddion NORTH tool provides a containerized environment defined in `NORTHtool` definition, `NORTHToolEntryPoint`, and Dockerfile.

## Base Image

This tool uses a pre-built base image `**nomad-north-desktop-base**` called that includes a basic Desktop-based environment. You can find more information here:

- Repository: https://github.com/FAIRmat-NFDI/nomad-north-desktop-base
- Image: `ghcr.io/fairmat-nfdi/nomad-north-desktop-base:main`

## Building and testing

Build the Docker image locally (from the package root):

```bash
docker build -f src/nomad_north_gwyddion/north_tools/gwyddion/Dockerfile \
    -t ghcr.io/fairmat-nfdi/nomad-north-gwyddion:latest .
```

Test the image (for jupyter notebook image):

```bash
docker run -p 8888:8888 ghcr.io/fairmat-nfdi/nomad-north-gwyddion:latest
```

Access JupyterLab at `http://localhost:8888`.

## Documentation

For comprehensive documentation on creating and managing NORTH tools, including detailed about some of the topic e.g.,

- Entry point configuration and `NORTHTool` API
- Docker image structure and best practices
- Dependency management

See the [NOMAD NORTH Tools documentation](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html).
