#  using positional and arbitrary arguments

def assign_seat(seat, *requests):
    print("\n Assing seat number " + str(seat) + " with the following requests :")
    for request in requests:
        print("- " + request)


assign_seat(20, 'window seat', 'top of the plane', 'preorder breakfast')