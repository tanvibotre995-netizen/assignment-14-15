from functools import reduce

Maximum = lambda No1,No2:(No1 if No1>No2 else No2)

def main():
    data = [13,8,20,55,45]

    print("input is",data)

    rdata = reduce(Maximum,data)

    print("list after reduce",rdata)

if __name__ == "__main__":
    main()
