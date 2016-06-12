positive_real_numbers =
   [for i in range(-infinity,infinity) where i > 0]

[] -> make a list
for i in ... -> let's call each item of this list "i"
range(-infinity, infinity) -> give me a list of numbers from negative infinity to infinity
where i > 0 -> filter the list, only keeping the items where i > 0

