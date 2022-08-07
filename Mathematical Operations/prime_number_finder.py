def prime_number_finder():
    
    print('''With the help of this program you can:
1.check if a number is prime number
2.Take out prime number in a range''')

    print("Do not type any thing in uppercase as an error would occur.")

    answer = str(input('Type the option from above:'))

    if answer == 'prime number in a range':
        print("Type a range.")
        lower = int(input('Lower:'))
        upper = int(input('Upper:'))

        print("Prime numbers between",lower,"and",upper,"are:")

        for num in range(lower, upper + 1):
               for i in range(2, num):
                   if (num % i) == 0:
                       break
               else:
                   print(num)

    else:
        num = 11
 
        if num > 1:
                for i in range(2, int(num/2)+1):
                    if (num % i) == 0:
                        print(num, "is not a prime number")
                        break
                    else:
                        print(num, "is a prime number")
        else:
                print(num, "is not a prime number")

prime_number_finder()