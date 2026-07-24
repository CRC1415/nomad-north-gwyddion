def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_gwyddion.north_tools import gwyddion

    assert (
        gwyddion.id_url_safe == 'gwyddion'
        or gwyddion.id == 'nomad-north-gwyddion'
    ), 'NORTHTool entry point has incorrect id or id_url_safe'
