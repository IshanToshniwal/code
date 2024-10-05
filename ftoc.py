def main():
    def ftc(c):
        return (c - 32) * 5 / 9

    def ctf(f):
        return f * 5 / 9 + 32

    unit = input('do you want to Fahrenheit to Celsius or Celsius to Fahrenheit: ')
    unit = unit.lower()
    if unit == 'fahrenheit to celsius':
        i = int(input('Enter the number to be converted: '))
        print(ftc(i))
    elif unit == 'celsius to fahrenheit':
        i = int(input('Enter the number to be converted: '))
        print(ctf(i))


main()
