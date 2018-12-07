
def mystery(n):
    
    if n <= 0:
        return 0
    else:
        return n + mystery(n - 1)
    
def main():

    n = int(input("Enter a number "))
    print(mystery(n))
main()
