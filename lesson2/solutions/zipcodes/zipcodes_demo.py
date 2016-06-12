from zipcodes import read_file, find_zipcode, find_zipcode_count, find_unique_zipcodes


zipcodes = read_file()
#print(zipcodes)
#print("unique zips:", len(find_unique_zipcodes(zipcodes)))
#print("zipcode tally", find_zipcode_count(zipcodes))
print("zipcode max tally:", find_zipcode_count(zipcodes)[1])
#print(find_zipcode('63317', zipcodes))
