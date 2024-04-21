from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # current date and new list
    today = datetime.today().date()
    congratulation_list = []
    #going through the list
    for user in users:
        #convert string to datetime object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        #convert year of birth to current
        birthday_this_year = birthday.replace(year=today.year)
        #checking the correctness of birthday date
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        #check next week for birthdays. If any coincide with the weekend, move the greeting to the start of the next week.
        days_to_birthday = (birthday_this_year - today).days
        if 0 <= days_to_birthday < 7:
            if birthday_this_year.weekday() >= 5:
                days_to_birthday += (7 - birthday_this_year.weekday())

            #add all info to the new list
            congratulation_date = today + timedelta(days=days_to_birthday)
            congratulation_list.append({"name": user["name"], "congratulation_date": congratulation_date})

    return congratulation_list


users = [
    {"name": "Luna", "birthday": "2000.04.25"},
    {"name": "Bella", "birthday": "1995.03.14"},
    {"name": "Lucy", "birthday": "1988.04.21"}
]

upcoming_birthdays = get_upcoming_birthdays(users=users)
print("Список привітань на цьому тижні:", upcoming_birthdays)