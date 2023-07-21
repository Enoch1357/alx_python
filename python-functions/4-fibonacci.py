n = int()
def fibonacci_sequence(n):
   n1 = 0
   n2 = 1
   count = 0
   if n <= 0:
      print("[", end="")
   elif n == 1:
      print("[{}".format(0), end="")
   elif n ==2:
      print("[{},".format(n1), end=" ")
   else:
      print("[", end="")
      while count < n - 1:
         print("{},".format(n1), end=" ")
         nth = n1 + n2

         n1 = n2
         n2 = nth
         count += 1
         if count == n -1:
            print("{}".format(n1), end="")
   return ("]")