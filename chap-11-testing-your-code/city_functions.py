# 11-1, 11-2
def city_country(city, country, population=''):
    ccp = f"{city.title()}, {country.title()}"
    if population:
        ccp += f" - population {population}"
    return ccp