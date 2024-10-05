len = float(input("Enter the Length : "))
bre = float(input("Enter the Breadth : "))
area = len * bre
perimeter = 2 * (len + bre)
print("Area of Rectangle :", area)
print("Perimeter of Rectangle :", perimeter)
if area > perimeter:
    print("Area of rectangle is greater than Perimeter")
else:
    print("Perimeter of rectangle is greater than Area")