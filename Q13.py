odd = lambda n:(n% 2 != 0)

def main():
    data = [13,5,8,10,20]

    print("input is :",data)

    fdata=list(filter(odd,data))

    print("list after filter",fdata)

if __name__ == "__main__":
    main()
