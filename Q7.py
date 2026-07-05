Divisible = lambda n:(n % 5 == 0)

def main():
    value = int(input("enter number:"))

    ret = Divisible(value)

    print(ret)

if __name__ == "__main__":
    main()
