year=0

if __name__ == "__main__":
    year=int(input("Imput the Year:"))

    if((year%4==0)and(year%100!=0))or(year%4==0):
        print("%d year is Yunion"%year)
    else:
        print("%d year is not Yunion"%year)
