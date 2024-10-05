weight = int(input("weight: "))
unit = input("weight in (K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight % 0.45
    print("weight in (L)bs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in (K)g: " + str(converted))
print("done")