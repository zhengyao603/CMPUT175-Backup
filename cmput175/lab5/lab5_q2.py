# function which is responsible for checking the validity of input date
def isValidDate(year_month_day):
    date_list = year_month_day.split('-')
    # month which have 30 days
    month_30 = [4, 6, 9, 11]
    # month which have 31 days
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    
    # check if the input are numbers
    for i in range(len(date_list)):
        try:
            int(date_list[i])
        except ValueError:
            if i == 0:
                return "Invalid year entered"
            elif i == 1:
                return "Invalid month entered"
            elif i == 2:
                return "Invalid day entered"
    
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    
    # check if the input year is between given range
    try:
        assert year >= 1901 and year <= 2020, "Invalid year entered"
    except AssertionError:
        return "Invalid year entered"
    
    # check if the input month is valid
    try:
        assert month >= 1 and month <= 12, "Invalid month entered"
    except AssertionError:
        return "Invalid month entered"
    
    # if the input month should have 31 days
    if month in month_31:
        try:
            assert day >= 1 and day <= 31, "Invalid day entered"
        except AssertionError:
            return "Invalid day entered"
    # if the input month should have 30 days
    elif month in month_30:
        try:
            assert day >= 1 and day <= 30, "Invalid day entered"
        except AssertionError:
            return "Invalid day entered"
    # if the input month is 2
    else:
        # if the input year is not leap year
        if year % 4 != 0:
            try:
                assert day >= 1 and day <= 28, "Invalid day entered"
            except AssertionError:
                return "Invalid day entered"
        # if the input year is leap year
        elif year % 4 == 0:
            try:
                assert day >= 1 and day <= 29, "Invalid day entered"
            except AssertionError:
                return "Invalid day entered"            

    return "The date entered is valid"

user_input = input("Please enter a date in YYYY-MM-DD format: ")
validity = isValidDate(user_input)
# check if all parts of the input are valid
if validity == "The date entered is valid":
    print("The date entered is valid")
elif validity == "Invalid year entered":
    print("Invalid year entered")
elif validity == "Invalid month entered":
    print("Invalid month entered")
elif validity == "Invalid day entered":
    print("Invalid day entered")