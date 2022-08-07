def palindrome_checker():
    print("Please enter string value in lower case only else a error would occur.")
    x = str(input('Type a string or number: '))
    y = x[::-1]

    if x == y:
        print(x,'=',y)
        print('Yes,',x,'is a palindrome.')
    else:
        print(x,'≠',y)
        print('No,',x,'is not a palindrome.')

palindrome_checker()