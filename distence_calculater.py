unit = input('enter a unit km, ft, i, cm, m: ')
unit1 = input('enter the unit you want to convert into(km, ft, i, cm, m, all): ')
number = int(input('enter the number you want to convert into ' + unit + ':'))
unit = unit.lower()
if unit == 'km':
    if unit1 == 'km':
        print('km = ' + str(number))
    elif unit1 == 'ft':
        number = number // 0.0003048
        print('ft = ' + str(number))
    elif unit1 == 'i':
        number = number // 0.0000254
        print('i = ' + str(number))
    elif unit1 == 'cm':
        number = number * 100000
        print('cm = ' + str(number))
    elif unit1 == 'm':
        number = number * 1000
        print('m = ' + str(number))
    elif unit1 == 'all':
        km = number
        ft = number // 0.0003048
        i = number // 0.0000254
        cm = number * 100000
        m = number * 1000
        print('km = ' + str(km))
        print('ft = ' + str(ft))
        print('i = ' + str(i))
        print('cm = ' + str(cm))
        print('m = ' + str(m))
elif unit == 'ft':
    if unit1 == 'km':
        number = number * 0.0003048
        print('km = ' + str(number))
    elif unit1 == 'ft':
        print('ft = ' + str(number))
    elif unit1 == 'i':
        number = number * 12
        print('i = ' + str(number))
    elif unit1 == 'cm':
        number = number * 30.48
        print('cm = ' + str(number))
    elif unit1 == 'm':
        number = number * 0.3048
        print('m = ' + str(number))
    elif unit1 == 'all':
        km = number * 0.0003048
        ft = number
        i = number * 12
        cm = number * 30.48
        m = number * 0.3048
        print('km = ' + str(km))
        print('ft = ' + str(ft))
        print('i = ' + str(i))
        print('cm = ' + str(cm))
        print('m = ' + str(m))
elif unit == 'i':
    if unit1 == 'km':
        number = number * 0.0000254
        print('km = ' + str(number))
    elif unit1 == 'ft':
        number = number // 12
        print('ft = ' + str(number))
    elif unit1 == 'i':
        print('i = ' + str(number))
    elif unit1 == 'cm':
        number = number * 0.3937
        print('cm = ' + str(number))
    elif unit1 == 'm':
        number = number * 0.0254
        print('m = ' + str(number))
    elif unit1 == 'all':
        km = number * 0.0000254
        ft = number // 12
        i = number
        cm = number * 0.3937
        m = number * 0.0254
        print('km = ' + str(km))
        print('ft = ' + str(ft))
        print('i = ' + str(i))
        print('cm = ' + str(cm))
        print('m = ' + str(m))
elif unit == 'cm':
    if unit1 == 'km':
        number = number // 100000
        print('km = ' + str(number))
    elif unit1 == 'ft':
        number = number * 0.0328084
        print('ft = ' + str(number))
    elif unit1 == 'i':
        number = number * 0.393701
        print('i = ' + str(number))
    elif unit1 == 'cm':
        print('cm = ' + str(number))
    elif unit1 == 'm':
        number = number * 0.01
        print('m = ' + str(number))
    elif unit1 == 'all':
        km = number * 100000
        ft = number * 0.0328084
        i = number * 0.393701
        cm = number
        m = number * 0.01
        print('km = ' + str(km))
        print('ft = ' + str(ft))
        print('i = ' + str(i))
        print('cm = ' + str(cm))
        print('m = ' + str(m))
elif unit == 'm':
    if unit1 == 'km':
        number = number * 1000
        print('km = ' + str(number))
    elif unit1 == 'ft':
        number = number * 3.28084
        print('ft = ' + str(number))
    elif unit1 == 'i':
        number = number * 39.36
        print('i = ' + str(number))
    elif unit1 == 'cm':
        number = number * 100
        print('cm = ' + str(number))
    elif unit1 == 'm':
        print('m = ' + str(number))
    elif unit1 == 'all':
        km = number * 1000
        ft = number * 3.28084
        i = number * 39.36
        cm = number * 100
        m = number
        print('km = ' + str(km))
        print('ft = ' + str(ft))
        print('i = ' + str(i))
        print('cm = ' + str(cm))
        print('m = ' + str(m))