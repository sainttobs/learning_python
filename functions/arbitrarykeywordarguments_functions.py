#  Using arbitrary keyword arguments

def seat_profile(first, last, **passenger_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in passenger_info.items():
        profile[key] = value

    return profile


passenger_profile = seat_profile('Adeyefa', 'Oluwatoba', seatnumber = 20, breakfastOrdered = 'yes')
print(passenger_profile)