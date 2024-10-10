number=(int(input("Enter the numerator: ")))
dnum=(int(input("Enter the denominator: ")))
if number%dnum==0:
    print(number, "is divisible by", dnum)
else:
    print(number, "is not divisible by", dnum)