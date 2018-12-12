import datetime


def get_user_birth_year(today):
    while True:
        year = input('Year of birth:\n> ')
        if year.isdigit() and 1900 <= int(year) <= today.year:
            return int(year)
        
        print('Invalid year!')


def get_user_birth_month(today, year):
    while True:
        month = input('Month of birth:\n> ')
        if month.isdigit():
            month = int(month)
            if year != today.year and 1 <= month <= 12:
                return month
            elif year == today.year and 1 <= month <= today.month:
                return month
        
        print('Invalid month!')


def get_user_birth_day(today, year, month):
    while True:
        day = input('Day of birth:\n> ')
        if day.isdigit():
            day = int(day)
            if year != today.year:
                max_days = month_mapper.get(month)
                
                # Check if it was leap year
                leap_year = True if year % 4 == 0 else False
                max_days = max_days[0] if not leap_year else max_days[1]
                
                if 1 <= day <= max_days:
                    return day
            
            elif year == today.year and month == today.month and 1 <= day <= today.day:
                return day
        
        print('Invalid day!')


def get_user_birth_date(today):
    year = get_user_birth_year(today)
    month = get_user_birth_month(today, year)
    day = get_user_birth_day(today, year, month)
    
    return datetime.date(year=year, month=month, day=day)


def calculate_days_old(today, birth_date):
    delta = today - birth_date
    return delta.days


def calculate_relevant_dates(birth_date):
    return {
        '10000': birth_date + datetime.timedelta(days=10000),
        '20000': birth_date + datetime.timedelta(days=20000),
        '30000': birth_date + datetime.timedelta(days=30000)
    }


def get_days_old():
    while True:
        days_old = input('Days of life: ')
        if days_old.isdigit() and int(days_old) >= 0:
            return int(days_old)


def calculate_specific_date(today, birth_date):
    days_old = get_days_old()
    display_date(today, days_old, birth_date + datetime.timedelta(days=days_old))


def display_date(today, days_old, date):
    verb = 'were' if date < today else 'will be' if date > today else 'are'
    print('You {} {} days old on the {}.'.format(verb, days_old, date))


def run():
    today = datetime.date.today()
    user_birth_date = get_user_birth_date(today)
    days_old = calculate_days_old(today, user_birth_date)
    
    suffix = suffix_mapper.get(str(days_old)[-1], default_suffix)
    input('\nToday is your {}{} day alive, so you are {} days old...\n'.format(days_old + 1, suffix, days_old))
    
    relevant_dates = calculate_relevant_dates(user_birth_date)
    
    for days in sorted(relevant_dates.keys()):
        display_date(today, days, relevant_dates[days])
    
    while True:
        flow = input('\nDo you wish to calculate another date [y/n]?\n> ').lower()
        if flow == 'y':
            calculate_specific_date(today, user_birth_date)
            input()
        elif flow == 'n':
            break


month_mapper = {
    1: [31],
    2: [28, 29],
    3: [31],
    4: [30],
    5: [31],
    6: [30],
    7: [31],
    8: [31],
    9: [30],
    10: [31],
    11: [30],
    12: [31],
}

suffix_mapper = {
    '1': 'st',
    '2': 'nd',
    '3': 'rd',
}

default_suffix = 'th'

if __name__ == '__main__':
    run()
