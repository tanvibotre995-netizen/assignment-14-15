maximum = lambda A,B:(A if A>B else B)

def main():
    value1=int(input("enter number:"))
    value2=int(input("enter number:"))

    ret = maximum(value1,value2)

    print("maximum number is",ret)
    
if __name__ == "__main__":
        main()
