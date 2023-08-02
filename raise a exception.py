try:

    a_number=int(input('Your Number? '))

except:

    print ('Enter a only even Number.')

else:

    eve_or_odd = a_number%2 == 0

    if eve_or_odd:

        print('no even number allowed .')

    else:

        print('An Odd number.')


