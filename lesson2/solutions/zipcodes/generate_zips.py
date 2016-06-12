from random import randint
import sys

digits = range(0,10)

def random_digit():
    return randint(0,9)

def generate_zipcode():
    return "".join([str(random_digit()) for _ in range(5)])

def generate_zipcodes(count):
    return "\n".join([generate_zipcode() for i in range(count)])

def generate_all_zipcodes(count):
    zipcodes = []
    for a in digits:
        for b in digits:
            for c in digits:
                for d in digits:
                    for e in digits:
                        zipcodes.append("%d%d%d%d%d" % (a, b, c, d, e))
    return zipcodes


zip_count = sys.argv[1]
print (generate_zipcodes(int(zip_count)))
