# zipcodes

def read_file():
    with open("zipcodes.txt") as f:
        lines = f.readlines()
        zipcodes = [line.strip() for line in lines]
        return zipcodes

def find_zipcode(zipcode, zipcodes):
    zipcodes = sorted(zipcodes)

    upper = len(zipcodes) - 1
    lower = 0

    found = False
    while not found:
        pos = int((upper + lower) / 2)
        print("pos is now:", pos)
        if upper == lower:
            found = True
            return None
        elif zipcode < zipcodes[pos]:
            upper = pos
        elif zipcode > zipcodes[pos]:
            lower = pos
        else:
            found = True
            return pos

def find_zipcode_count(zipcodes):
    tally = {}
    maximum = (None, 0)
    for z in zipcodes:
        if tally.get(z, None) == None:
            tally[z] = 1
        else:
            tally[z] += 1
            if tally[z] > maximum[1]:
                maximum = (z, tally[z])
    return tally, maximum

def find_unique_zipcodes(zipcodes):
    unique_zipcodes = set()
    for z in zipcodes:
        unique_zipcodes.add(z)
    return unique_zipcodes
