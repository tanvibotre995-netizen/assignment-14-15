from functools import reduce

Numbers = lambda a,b:(a*b) 

def main():
    Data = [12,4,6,23,15]

    print("input is :",Data)

    rdata=reduce(Numbers,Data)

    print("data after filter",rdata)

if __name__ == "__main__":
    main()
