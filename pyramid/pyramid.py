def pyramid(height, building=None):
    if not building:
        building = []

    if len(building) == height:
        return '\n'.join(building)
    else:
        building.append('0' * (len(building) + 1))
        return pyramid(height, building)
