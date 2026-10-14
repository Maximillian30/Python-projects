print('Enter the value you want to convert:')
user_input = input()

if user_input.isdigit():
    temp = float(user_input)
    print('Enter the unit you want to convert from (C for Celsius, F for Fahrenheit):')
    choice = input().strip().upper()
     #convert temperature based on user choice
    if choice == 'C':
        converted_temp = (temp * 9/5) + 32
        print(f'{temp}°C is equal to {converted_temp}°F')
    elif choice == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f'{temp}°F is equal to {converted_temp}°C')
    else:
        print('Invalid unit. Please enter C for Celsius or F for Fahrenheit.')