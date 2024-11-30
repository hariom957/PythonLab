input_string = input("Enter a comma-separated string: ")

input_list = input_string.split(",")

letters = list(filter(lambda x: x.isalpha(), input_list))
uppercase_letters = list(map(lambda x: x.upper(), letters))

digits = list(filter(lambda x: x.isdigit(), input_list))
squared_digits = list(map(lambda x: int(x) ** 2, digits))

alphanumeric = list(filter(lambda x: x.isalnum(), input_list))

print("Uppercase Letters:", uppercase_letters)
print("Squared Digits:", squared_digits)
print("Alphanumeric Characters:", alphanumeric)
