def celsuis_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

#Hardcoded values for testing
print('Testing conversion functions with hardcoded values:')
celsius_value = -25
fahrenheit_value = 77
converted_to_fahrenheit = celsuis_to_fahrenheit(celsius_value)
converted_to_celsius = fahrenheit_to_celsius(fahrenheit_value)
print(f'{celsius_value}°C is equal to {converted_to_fahrenheit}°F')
print(f'{fahrenheit_value}°F is equal to {converted_to_celsius}°C')
