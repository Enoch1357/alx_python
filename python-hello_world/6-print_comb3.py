for i in range(10):
    for k in range(10):
        number = str("{}{}".format(i, k)) 
        if i != k and i < k and int(number) != 89:
            print("{:02}".format(int(number)), end=", ")
        elif i != k and i < k and int(number) == 89:
            print("{:02}".format(int(number)))