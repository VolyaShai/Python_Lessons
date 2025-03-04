numbers = int (input("Enter a positive integer:"))
high_numb = 0
while numbers != 0 :
    digit = numbers % 10
    if  digit > high_numb :
        high_numb = digit
    numbers = numbers // 10
print ( f"The highest digit in the {numbers} it is {high_numb} " )