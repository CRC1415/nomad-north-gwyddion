ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
ARG PLUGIN_NAME=nomad-north-gwyddion

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# RUN apt update \
#  && apt install --no-install-recommends -y \
#       wget \
#       libgl1 \
#       libglu1-mesa \
#       libglu1-mesa-dev \
#  && rm -rf /var/lib/apt/lists/*

# See: https://github.com/AFM-SPM/gwyddion-python
# Install main packages
RUN apt-get update && apt-get install -y \
    gwyddion \
    python3 \
    python3-gi \
    xvfb \
 && rm -rf /var/lib/apt/lists/*

# Required for gwyutils
ENV PYTHONPATH "${PYTHONPATH}:/usr/share/gwyddion/pygwy"

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}

WORKDIR "${HOME}/gwyddion"

# WORKDIR "${HOME}"

COPY --chown=${NB_UID}:${NB_GID} "src/nomad_north_gwyddion/north_tools/gwyddion/config/Gwyddion.desktop" "${HOME}/.config/autostart/Gwyddion.desktop"
