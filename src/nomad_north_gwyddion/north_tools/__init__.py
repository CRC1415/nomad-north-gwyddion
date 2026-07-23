from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NORTHToolEntryPoint

my_north_tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-gwyddion.',
    image='ghcr.io/crc1415/nomad-north-gwyddion:main',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-gwyddion.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'ron.dockhorn@tu-dresden.de', 'name': 'Ron Dockhorn'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='my_north_tool',
)

north_entry_point = NORTHToolEntryPoint(
    id_url_safe='nomad-north-gwyddion-my-north-tool',
    north_tool=my_north_tool,
)
