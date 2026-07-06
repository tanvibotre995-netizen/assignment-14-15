from functools import reduce

Minimum = lambda No1,No2:(No1 if No1<No2 else No2)

def main():
    data = [13,8,20,55,45]

    print("input is",data)

    rdata = reduce(Minimum,data)

    print("list after reduce",rdata)

if __name__ == "__main__":
    main()
