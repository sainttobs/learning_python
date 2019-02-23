# adding an arbitrary number of arguments to a function


def creat_passenger(*requests):  # use the * sign to add an arbitraty arguments
    print('\n This passenger has requested the following: ')
    for request in requests:
        print('- ' + request)


creat_passenger('window seat', 'top of the plane', 'preorder breakfast')