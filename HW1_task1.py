from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Creating a dict for storing usernames by weekdays
    birthday_dict = defaultdict(list)
    
    # Getting a current date
    today = datetime.today().date()
    
    # Defining a date of the next Monday
    days_until_next_monday = (7 - today.weekday()) % 7
    next_monday = today + timedelta(days=days_until_next_monday)
    
    # Iterating users
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=2023)
        
        # Checkштп if the birthday has passed already this year
        if birthday_this_year <= today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculating the difference between dates
        delta_days = (birthday_this_year - today).days
        
        # Defining a weekday of birthday
        day_of_week = birthday_this_year.strftime("%A")
        
        # Checking if a birthday is during a weekend
        if day_of_week in ["Saturday", "Sunday"]:
            day_of_week = f"Congratulations should be sent on Monday next week, as the Birthday will be during the weekend"
        
        # If birthday is on the next week, storing the username
        if delta_days >= 0 and delta_days < 7:
            birthday_dict[day_of_week].append(name)
    
    # Printing result
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")

# Приклад виклику функції
# users = [
#     {"name": "Bill Gates", "birthday": datetime(1955, 10, 16)},
#     {"name": "Jan Koum", "birthday": datetime(1976, 10, 17)},
#     {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 18)},
#     {"name": "Jill Valentine", "birthday": datetime(1974, 10, 19)},
#     {"name": "Eugene Churylov", "birthday": datetime(1974, 10, 21)},
#     {"name": "Roman Balk", "birthday": datetime(1974, 10, 22)}
# ]

# get_birthdays_per_week(users)
