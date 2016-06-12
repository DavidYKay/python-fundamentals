defcon = 5

print("Current DEFCON is:", defcon, "and I had beans for breakfast today!")
if defcon > 3:
    print("Declare war on Russia")
elif defcon == 2:
    print("Maintain PRISM Program")
else:
    print("Cut defense budget")


defcon = 2
if defcon > 3:
    print("Declare war on Russia")
else:
    if defcon == 2:
       print("Maintain PRISM Program")
    else:
       print("Cut defense budget")
