Numbers = lambda n:(n % 3 == 0 and n% 5 == 0) 

def main():
    Data = [12,4,6,23,15]

    print("input is :",Data)

    fdata=list(filter(Numbers,Data))

    print("data after filter",fdata)

if __name__ == "__main__":
    main()
