def temperature_converter():
    print('''This code can covert:
1.Celsius to fahrenheit
2.Fahrenheit to celsius
3.Celsius to kelvin
4.Kelvin to celsius
5.Fahrenheit to kelvin
6.Kelvin to fahrenheit''')

    print("Do not type '°,C,F and K' after temperature. ")

    answer = str(input('Type the option from above:'))

    if answer == 'Celsius to fahrenheit':
        celsius = int(input('Type the temperature for conversion:'))
        fahrenheit = (celsius * 9/5) + 32
        print(celsius,'degree celsius is equals to',fahrenheit,'degree fahrenheit.')
    elif answer == 'Fahrenheit to celsius':
        fahrenheit = int(input('Type the temperature for conversion:'))
        celsius = (fahrenheit - 32) * 5/9
        print(fahrenheit,'degree fahrenheit is equals to',celsius,'degree celsius.')
    elif answer == 'Celsius to kelvin':
        celsius = int(input('Type the temperature for conversion:'))
        kelvin = celsius + 273.15
        print(celsius,'degree celsius is equals to',kelvin,'kelvin.')
    elif answer == 'Kelvin to celsius':
        kelvin = int(input('Type the temperature for conversion:'))
        celsius = kelvin - 273.15
        print(kelvin,'kelvin is equals to',celsius,'degree celsius.')
    elif answer == 'Fahrenheit to kelvin':
        fahrenheit = int(input('Type the temperature for conversion:'))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(fahrenheit,'degree is equals to',kelvin,'kelvin.')
    elif answer == 'Kelvin to fahrenheit':
        kelvin = int(input('Type the temperature for conversion:'))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(kelvin,'kelvin is equals to',fahrenheit,'degree fahrenheit.')
    else:
        print('Invalid answer.')
        print('''This code can covert:
1.Celsius to fahrenheit
2.Fahrenheit to celsius
3.Celsius to kelvin
4.Kelvin to celsius
5.Fahrenheit to kelvin
6.Kelvin to fahrenheit''')

temperature_converter()