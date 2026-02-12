import math
fam1 = int(input("How many slices for family member 1 "))
fam2 = int(input("How many slices for family member 2 "))
fam3 = int(input("How many slices for family member 3 "))
fam4 = int(input("How many slices for family member 4 "))
sum = fam1+fam2+fam3+fam4
totalpizza = math.ceil(sum/8)
leftover = (totalpizza*8) - sum
print("In total, you would need to order", totalpizza , "pizzas")
print("You would have", leftover, "slices leftover")
