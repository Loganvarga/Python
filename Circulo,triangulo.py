figura = input("seleccione figura c o t")
if (figura=="t"):
    base = int(input("seleccione numero"));
    altura = int(input("seleccione numero"));
    area = (base * altura /2)
    print (area)
else:
    if (figura=="c"):
        radio = int(input("seleccione numero"));
        PI = (3.14);
        area = (radio * PI)
        print (area)
