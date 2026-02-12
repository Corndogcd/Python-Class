buying = input("Would you like a muffin or a cupcake? ")
muffin = 10
cupcake = 10
while buying != "0":
    if buying == "muffin":
        if muffin > 0:
            muffin = muffin - 1
            if muffin == 0:
                print("The muffins are out of stock!")
        else:
            print("The muffins are out of stock!")
    if buying == "cupcake":
        if cupcake > 0:
            cupcake = cupcake - 1
            if cupcake == 0:
                print("The cupcakes are out of stock!")
        else:
            print("The cupcakes are out of stock!")
    buying = input("Would you like a muffin or a cupcake? ")
print("Muffins: ", muffin, "Cupcakes: ", cupcake)
