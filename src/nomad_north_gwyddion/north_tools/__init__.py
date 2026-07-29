from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

gwyddion_north_tool = NORTHTool(
    short_description='Use Gwyddion as scanning probe microscopy data processing software.',
    image='ghcr.io/fairmat-nfdi/nomad-north-gwyddion:main',
    description="""### **Gwyddion**:

    [Gwyddion is a Scanning Probe Microscopy data processing software.](https://gwyddion.net/)

    [Research article about the software](https://doi.org/10.2478/s11534-011-0096-2)

    [Supported file types v2.71](https://gwyddion.net/documentation/user-guide-en/file-formats.html)""",
    external_mounts=[],
    file_extensions=['dm4', 'tif', 'tiff', 'wip', 'wit', 'spm', 'ibw'],
    icon='https://raw.githubusercontent.com/fairmat-nfdi/nomad-north-gwyddion/refs/heads/main/src/nomad_north_gwyddion/north_tools/gwyddion/gwyddion.png',
    image_pull_policy='Always',
    default_url='/desktop',
    maintainer=[{'email': 'lukas.pielsticker@physik.hu-berlin.de', 'name': 'Lukas Pielsticker'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='gwyddion',
)

gwyddion = NorthToolEntryPoint(
    id_url_safe='gwyddion',
    north_tool=gwyddion_north_tool,
)
