largest = lambda A,B,C:(A if A>=B and A>=C else (B if B>=C else C))

def main():
    value1=int(input("enter number:"))
    value2=int(input("enter number:"))
    value3=int(input("enter number:"))

    ret = largest(value1,value2,value3)

    print("largest number is",ret)

if __name__ == "__main__":
    main()
