for i in range(10):
    for k in range(10):
        number = str("{}{}".format(i, k)) 
        if i != k and i < k and number!=89:
            print("{:02},".format(number), end=" ")