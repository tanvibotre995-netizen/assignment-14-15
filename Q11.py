Square = lambda n:(n * n)

def main():
    data= [1,2,3,4,5]

    print("input is :",data)

    mdata=list(map(Square,data))

    print("data after filter",mdata)

if __name__ == "__main__":
    main()
