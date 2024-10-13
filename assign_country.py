def assign_country(bf):
    countries = (None, None)
    found_first =
    for row in range(len(bf)):
        for col in range(len(bf[row])):
            tile_country = bf[row][col].country
            if tile_country > 0:
                if not found_first:
                    countries[0] = tile_country
                    found_first = True
                else:
                    if tile_country != countries[0]
                    countries[1] = tile_country
    return (min(countries), max(countries))
