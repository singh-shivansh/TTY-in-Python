def pythagorean_triplet_checker_and_finder():

    import math
   
    print('''With the help of this program you can:
1.Find missing number in pythagorean triplet
2.Check if a set of numbers is pythagorean triplet''')
    
    print("Do not type any thing in uppercase or (²)as an error would occur.")

    answer = str(input('Type the option from above:'))
    
    if answer == 'find missing number in pythagorean triplet':
        
        if answer == 'first value':
            b = int(input('Enter the seccond value: '))
            b = b ** 2
            c = int(input('Enter the third value: '))
            c = c ** 2
            a = c - b
            a = math.sqrt()
            print(a,'is the missing value in pythagorean triplet.')
        elif answer == 'second value':
            a = int(input('Enter the first value: '))
            a = a ** 2
            c = int(input('Enter the third value: '))
            c = c ** 2
            b = c - a
            b = math.sqrt()
            print(b,'is the missing value in pythagorean triplet.')
        elif answer == 'third value':
            a = int(input('Enter the first value: '))
            a = a ** 2
            b = int(input('Enter the seconf\d value: '))
            b = b ** 2
            c = a + b
            c = math.sqrt()
            print(c,'is the missing value in pythagorean triplet.')
        else:
            print('Invalid answer.')
            answer = str(input('Whats missing(first value, second value, third value)? '))
    elif answer == 'check if a set of numbers is pythagorean triplet':
        a = int(input('Enter the first value:'))
        a = a**2
        b = int(input('enter the second value:'))
        b = b**2
        c = int(input('enter the third value:'))
        c = c**2

        if a + b == c:
            print(a + b,'=',c)
            print('Hence, it is a pythagorean triplet.')
        else:
            print(a + b,'≠',c)
            print('Hence, it is not a pythagorean triplet.')
    
    else:
        print('Invalid answer.')

        print('''With the help of this program you can:
1.Find missing number in pythagorean triplet
2.Check if a set of numbers is pythagorean triplet''')
    
    print("Do not type any thing in uppercase or (²)as an error would occur.")

pythagorean_triplet_checker_and_finder()