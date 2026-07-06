Even = lambda n:(n % 2 == 0)

def main():
    Data =[11,8,21,40,20]

    print("input is :",Data)

    fdata = list(filter(Even,Data))

    print("data after filter",fdata)

if __name__ == "__main__":
    main()
