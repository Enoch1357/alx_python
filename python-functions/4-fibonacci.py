n = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if n <= 0:
   print(0)
# if there is only one term, return n1
elif n == 1:
   print([n1])
# generate fibonacci sequence
elif n ==2:
    print("[{}, {}]".format(n1, n2))
else:
   while count < n:
       print("{},".format(n1), end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1