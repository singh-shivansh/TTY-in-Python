#in a range of a number
def divisibility_checker():

    print('''With the help of this program you can take out:
1.For a range of number
2.For a single number''')

    print("Do not type any thing in uppercase as an error would occur.")
    answer = str(input('Type the option from above:'))
    
    if answer == 'for a range of number':
        divisor = int(input('Enter the divisor:'))
        tillwhen = int(input('Till when to find:'))
        tillwhen = tillwhen + 1
        num = 1

        print("These are the numbers divible by",divisor,"till",tillwhen - 1,":")

        for num in range(1, tillwhen):
            if num % divisor == 0:
                print(num)
    
    else:
        divident = int(input("Enter the divident:"))
        divisor = int(input('Enter the divisor'))

        if divident % divisor == 0:
            print("Yes,",divident,"is divisble by",divisor,".")
        else:
            print("No,",divident,"is not divisble by",divisor,".")

divisibility_checker()