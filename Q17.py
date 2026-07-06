String = lambda s: len(s)>5

def main():
    Data = ["pune","mumbai","solapur","satara"]

    print("input is :",Data)

    fdata=list(filter(String,Data))

    print("data after filter",fdata)

if __name__ == "__main__":
    main()
