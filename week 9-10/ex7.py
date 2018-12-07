def mystery(n):
    if n <= 0:
        return 0
    else:
        return mystery(n // 2) + 1
def main():

    n = int(input("Enter a number "))
    print(mystery(n))
main()
