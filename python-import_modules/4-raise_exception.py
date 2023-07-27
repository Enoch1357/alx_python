#! /usr/bin/python3
__name__ = "__main__"
a = [1, 2, 3]
b = (4, 5, 6)
def raise_exception(a, b):
    
    try: 
        myResult = a + b
        print(myResult)    
    except TypeError:
        myResult = "Exception raised" 
    finally:
        return myResult