def table_printer():
    x = int(input('Table of:'))
    y = int(input('Till when:'))
    y = y + 1
    z = 1
    print("The table of",x,"till",y - 1,"is:")
    while z < y:
        print(x * z)
        z = z + 1

table_printer()