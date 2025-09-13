def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("x is even")
    else :
        print("x is not even ")
def is_even(x):
    if x%2 == 0:
        return True  
    else:
        return False   
main()