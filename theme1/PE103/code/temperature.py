def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    :param celsius (float): Temperature in Celsius

    :returns: Temperature converted to Fahrenheit
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

print(f"0 deg C is {celsius_to_fahrenheit(0)} deg F")
