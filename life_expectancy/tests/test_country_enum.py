from life_expectancy.enums import Country

def test_all_actual_countries(all_actual_countries):
    """
    Test all countries
    """
    assert all_actual_countries == Country.__actual_countries__()