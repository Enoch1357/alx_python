def is_prime(n):
  for i in range(2,int(n)): #or n-1 or n/2
    if (n % i) == 0:
      return False
  return True