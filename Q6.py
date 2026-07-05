odd = lambda n:(n%2 != 0)

def main():
    value = int(input("enter number:"))

    ret = odd(value)

    print(ret)
if __name__ == "__main__":
    main()
