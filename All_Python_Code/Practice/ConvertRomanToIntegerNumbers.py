roman = {"I":1,
         "V":5,
         "X":10,
         "L":50,
         "C":100,
         "D":500,
         "M":1000}
# CDXLIV = 444

# num = input("Enter Roman Numbers : ")

# if len(num) == 1:
#     if num in roman:
#         print(roman[num])
#     else:
#         print("Invalid.")

# add = 0
# if len(num) > 1:
#     for i in range(0,len(roman),2):
#         number = roman[i+1] - roman[i]
#         add += number



def roman_to_decimal(num):
    result = 0
    prev_value = 0
    
    for symbol in num[::-1]:  # Iterate the Roman numeral string in reverse order
        value = roman.get(symbol, 0)
        
        if value < prev_value:
            result -= value
        else:
            result += value
        
        prev_value = value
    
    return result

num = input("Enter Roman Numerals: ").upper()
decimal_value = roman_to_decimal(num)

if decimal_value != 0:
    print(f"The decimal equivalent of {num} is {decimal_value}.")
else:
    print("Invalid Roman numeral entered.")
