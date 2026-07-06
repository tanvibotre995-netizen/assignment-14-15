from functools import reduce

Addition = lambda No1,No2 : No1+No2

def main():
    Data= [12,5,7,23,10]

    print("input is :",Data)

    rdata=reduce(Addition,Data)

    print("data after reduce",rdata)

if __name__ == "__main__":
    main()
