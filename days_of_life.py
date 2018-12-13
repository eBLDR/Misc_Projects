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
                max_days = max_days[1] if leap_year and month == 2 else max_days[0]
                
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


def calculate_relevant_dates(today, birth_date):
    relevant_dates = {
        '10000': birth_date + datetime.timedelta(days=10000),
        '20000': birth_date + datetime.timedelta(days=20000),
        '30000': birth_date + datetime.timedelta(days=30000)
    }
    for days in sorted(relevant_dates.keys()):
        display_date(today, days, relevant_dates[days])


def calculate_specific_date(today, birth_date):
    def get_days_old():
        while True:
            days = input('\nDays of life: ')
            if days.isdigit() and int(days) >= 0:
                return int(days)
    
    days_old = get_days_old()
    print()
    display_date(today, days_old, birth_date + datetime.timedelta(days=days_old))


def calculate_life_expectancy(days_old):
    def get_country():
        while True:
            country = input('\nCountry:\n> ').lower()
            if country in [country_name.lower() for country_name in life_expectancy_mapper.keys()]:
                return country
            else:
                print('Country unknown/not supported.')
    
    def get_gender():
        while True:
            gender = input('\nMale [m] or female [f]:\n> ').lower()
            if gender in ['m', 'f']:
                return gender
    
    user_country = get_country()
    user_gender = get_gender()
    life_expectancy_years = life_expectancy_mapper[user_country][user_gender]
    life_expectancy_range = [round(life_expectancy_years * 365 * 0.9), round(life_expectancy_years * 365 * 1.1)]
    life_expectancy_left_range = [days - days_old for days in life_expectancy_range]
    life_expectancy_left_min = life_expectancy_left_range[0] if life_expectancy_left_range[0] > 0 else 0
    life_expectancy_left_max = life_expectancy_left_range[1] if life_expectancy_left_range[1] > 0 else '?'
    life_expectancy_consumed_percentage_range = [round(days_old * 100 / days, 3) for days in life_expectancy_range]
    life_expectancy_consumed_percentage_min = life_expectancy_consumed_percentage_range[1] if life_expectancy_consumed_percentage_range[1] < 100 else '?'
    life_expectancy_consumed_percentage_max = life_expectancy_consumed_percentage_range[0] if life_expectancy_consumed_percentage_range[0] < 100 else 100
    
    print('\nLife expectancy in {} is {} years, that is a range (+/-10%) from {} to {} days of life.'.format(user_country.title(), life_expectancy_years, life_expectancy_range[0], life_expectancy_range[1]))
    print('You have used {} days of life, then you have an estimation of \033[1;33m{}\033[0m to \033[1;33m{}\033[0m days more for living.'.format(days_old, life_expectancy_left_min, life_expectancy_left_max))
    print('In percentage, this means that you have consumed already \033[1;33m{}%\033[0m to \033[1;33m{}%\033[0m of your lifespan...'.format(life_expectancy_consumed_percentage_min, life_expectancy_consumed_percentage_max))


def display_date(today, days_old, date):
    verb = 'were' if date < today else 'will be' if date > today else 'are'
    print('You {} \033[1m{}\033[0m days old on the \033[1m{}\033[0m.'.format(verb, days_old, date))


def run():
    # Days of life
    today = datetime.date.today()
    user_birth_date = get_user_birth_date(today)
    days_old = calculate_days_old(today, user_birth_date)
    
    suffix = suffix_mapper.get(str(days_old + 1)[-1], default_suffix)
    input('\nToday is your \033[1;34m{}{}\033[0m day alive, so you are {} days old...\n'.format(days_old + 1, suffix, days_old))
    
    # Relevant dates
    calculate_relevant_dates(today, user_birth_date)
    
    # Specific date
    while True:
        flow = input('\nDo you wish to calculate another specific date [y/n]?\n> ').lower()
        if flow == 'y':
            calculate_specific_date(today, user_birth_date)
        elif flow == 'n':
            break
    
    # Life expectancy
    flow = input('\nDo you want to know what\'s your life expectancy [y/*]?\n> ').lower()
    if flow == 'y':
        calculate_life_expectancy(days_old)
        input()


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

life_expectancy_mapper = {
    'pakistan': {
        'f': 66.84,
        'm': 64.99
    },
    'france': {
        'f': 84.87,
        'm': 78.76
    },
    'peru': {
        'f': 76.84,
        'm': 71.54
    },
    'burundi': {
        'f': 58.04,
        'm': 54.18
    },
    'costa rica': {
        'f': 81.69,
        'm': 76.7
    },
    'macau': {
        'f': 82.51,
        'm': 78.07
    },
    'fiji': {
        'f': 72.89,
        'm': 66.93
    },
    'puerto rico': {
        'f': 83.17,
        'm': 75.19
    },
    'brazil': {
        'f': 77.86,
        'm': 70.29
    },
    'saint lucia': {
        'f': 77.57,
        'm': 72.17
    },
    'u.s. virgin islands': {
        'f': 82.92,
        'm': 77.24
    },
    'mayotte': {
        'f': 82.9,
        'm': 76.04
    },
    'central african republic': {
        'f': 51.25,
        'm': 47.83
    },
    'belgium': {
        'f': 83.02,
        'm': 77.95
    },
    'belize': {
        'f': 72.72,
        'm': 67.19
    },
    'estonia': {
        'f': 81.05,
        'm': 71.57
    },
    'burkina faso': {
        'f': 59.33,
        'm': 56.73
    },
    'bangladesh': {
        'f': 72.26,
        'm': 69.85
    },
    'poland': {
        'f': 81.14,
        'm': 73.06
    },
    'libya': {
        'f': 74.41,
        'm': 68.79
    },
    'switzerland': {
        'f': 85.23,
        'm': 80.27
    },
    'democratic republic of the congo': {
        'f': 59.53,
        'm': 56.67
    },
    'swaziland': {
        'f': 48.54,
        'm': 49.69
    },
    'chile': {
        'f': 84.12,
        'm': 78.09
    },
    'myanmar': {
        'f': 67.66,
        'm': 63.58
    },
    'canada': {
        'f': 83.78,
        'm': 79.69
    },
    'kyrgyzstan': {
        'f': 74.29,
        'm': 66.35
    },
    'honduras': {
        'f': 75.4,
        'm': 70.39
    },
    'slovakia': {
        'f': 79.73,
        'm': 72.24
    },
    'nepal': {
        'f': 70.45,
        'm': 67.64
    },
    'czech republic': {
        'f': 81.27,
        'm': 75.36
    },
    'guyana': {
        'f': 68.59,
        'm': 64.03
    },
    'mauritius': {
        'f': 77.74,
        'm': 70.67
    },
    'bahamas': {
        'f': 78.09,
        'm': 72.02
    },
    'cambodia': {
        'f': 69.55,
        'm': 65.5
    },
    'moldova': {
        'f': 75.43,
        'm': 67.22
    },
    'maldives': {
        'f': 77.41,
        'm': 75.4
    },
    'australia': {
        'f': 86.56,
        'm': 80.33
    },
    'equatorial guinea': {
        'f': 58.57,
        'm': 55.87
    },
    'belarus': {
        'f': 76.97,
        'm': 65.29
    },
    'trinidad and tobago': {
        'f': 73.84,
        'm': 66.87
    },
    'russia': {
        'f': 75.55,
        'm': 64.15
    },
    'dominican republic': {
        'f': 76.45,
        'm': 70.16
    },
    'south sudan': {
        'f': 56.03,
        'm': 54.1
    },
    'argentina': {
        'f': 79.83,
        'm': 72.15
    },
    'south korea': {
        'f': 84.63,
        'm': 77.95
    },
    'new caledonia': {
        'f': 79.31,
        'm': 73.55
    },
    'new zealand': {
        'f': 83.35,
        'm': 79.71
    },
    'malawi': {
        'f': 61.98,
        'm': 59.86
    },
    'saint vincent and the grenadines': {
        'f': 74.9,
        'm': 70.7
    },
    'spain': {
        'f': 85.05,
        'm': 79.42
    },
    'togo': {
        'f': 59.68,
        'm': 58.28
    },
    'iceland': {
        'f': 83.84,
        'm': 80.73
    },
    'ireland': {
        'f': 82.74,
        'm': 78.4
    },
    'mauritania': {
        'f': 64.25,
        'm': 61.29
    },
    'cyprus': {
        'f': 82.17,
        'm': 77.69
    },
    'liberia': {
        'f': 61.21,
        'm': 59.29
    },
    'mozambique': {
        'f': 56.18,
        'm': 52.94
    },
    'seychelles': {
        'f': 77.91,
        'm': 68.69
    },
    'guinea': {
        'f': 58.49,
        'm': 57.58
    },
    'uganda': {
        'f': 58.83,
        'm': 55.67
    },
    'austria': {
        'f': 83.59,
        'm': 78.47
    },
    'laos': {
        'f': 66.84,
        'm': 64.14
    },
    'gabon': {
        'f': 64.07,
        'm': 63.15
    },
    'eritrea': {
        'f': 65.18,
        'm': 60.9
    },
    'gambia': {
        'f': 61.21,
        'm': 58.54
    },
    'sri lanka': {
        'f': 78.03,
        'm': 71.24
    },
    'uzbekistan': {
        'f': 71.61,
        'm': 64.9
    },
    'afghanistan': {
        'f': 61.06,
        'm': 58.67
    },
    'croatia': {
        'f': 80.38,
        'm': 73.64
    },
    'jamaica': {
        'f': 77.89,
        'm': 73.07
    },
    'djibouti': {
        'f': 63.24,
        'm': 60.04
    },
    'united kingdom': {
        'f': 82.39,
        'm': 78.45
    },
    'ethiopia': {
        'f': 65.02,
        'm': 61.3
    },
    'romania': {
        'f': 78.07,
        'm': 70.92
    },
    'china': {
        'f': 77.02,
        'm': 73.97
    },
    'north korea': {
        'f': 73.27,
        'm': 66.3
    },
    "cote d'ivoire": {
        'f': 51.85,
        'm': 50.21
    },
    'bulgaria': {
        'f': 77.56,
        'm': 70.64
    },
    'denmark': {
        'f': 81.94,
        'm': 78.0
    },
    'luxembourg': {
        'f': 83.65,
        'm': 78.94
    },
    'cameroon': {
        'f': 56.02,
        'm': 53.74
    },
    'syria': {
        'f': 76.26,
        'm': 63.98
    },
    'botswana': {
        'f': 66.51,
        'm': 61.8
    },
    'turkey': {
        'f': 78.12,
        'm': 71.53
    },
    'iraq': {
        'f': 71.44,
        'm': 66.99
    },
    'cuba': {
        'f': 81.27,
        'm': 77.1
    },
    'comoros': {
        'f': 64.5,
        'm': 61.2
    },
    'suriname': {
        'f': 74.18,
        'm': 67.81
    },
    'timor-leste': {
        'f': 69.51,
        'm': 66.06
    },
    'latvia': {
        'f': 78.68,
        'm': 68.85
    },
    'rwanda': {
        'f': 66.3,
        'm': 59.65
    },
    'sao tome and principe': {
        'f': 68.19,
        'm': 64.23
    },
    'benin': {
        'f': 60.61,
        'm': 57.77
    },
    'armenia': {
        'f': 78.39,
        'm': 70.74
    },
    'senegal': {
        'f': 67.61,
        'm': 63.86
    },
    'lithuania': {
        'f': 78.78,
        'm': 67.39
    },
    'brunei': {
        'f': 80.39,
        'm': 76.64
    },
    'kazakhstan': {
        'f': 73.87,
        'm': 64.29
    },
    'azerbaijan': {
        'f': 73.77,
        'm': 67.54
    },
    'kenya': {
        'f': 62.17,
        'm': 59.08
    },
    'thailand': {
        'f': 77.58,
        'm': 70.83
    },
    'solomon islands': {
        'f': 69.03,
        'm': 66.19
    },
    'guadeloupe': {
        'f': 83.98,
        'm': 76.83
    },
    'ukraine': {
        'f': 75.67,
        'm': 65.73
    },
    'malta': {
        'f': 81.98,
        'm': 78.55
    },
    'hong kong': {
        'f': 83.82,
        'm': 80.18
    },
    'aruba': {
        'f': 77.76,
        'm': 72.89
    },
    'martinique': {
        'f': 84.36,
        'm': 77.79
    },
    'portugal': {
        'f': 83.5,
        'm': 77.43
    },
    'tanzania': {
        'f': 65.55,
        'm': 62.55
    },
    'slovenia': {
        'f': 83.14,
        'm': 76.92
    },
    'barbados': {
        'f': 77.71,
        'm': 72.91
    },
    'venezuela': {
        'f': 78.24,
        'm': 69.93
    },
    'lesotho': {
        'f': 49.59,
        'm': 49.19
    },
    'netherlands': {
        'f': 83.14,
        'm': 79.36
    },
    'bolivia': {
        'f': 70.21,
        'm': 65.34
    },
    'oman': {
        'f': 78.85,
        'm': 74.66
    },
    'zimbabwe': {
        'f': 55.95,
        'm': 53.6
    },
    'federated states of micronesia': {
        'f': 69.85,
        'm': 67.99
    },
    'bhutan': {
        'f': 69.09,
        'm': 68.63
    },
    'philippines': {
        'f': 71.55,
        'm': 64.72
    },
    'yemen': {
        'f': 64.88,
        'm': 62.18
    },
    'french polynesia': {
        'f': 78.55,
        'm': 73.97
    },
    'tunisia': {
        'f': 77.04,
        'm': 72.3
    },
    'bahrain': {
        'f': 77.42,
        'm': 75.58
    },
    'montenegro': {
        'f': 78.18,
        'm': 73.83
    },
    'antigua and barbuda': {
        'f': 78.21,
        'm': 73.29
    },
    'somalia': {
        'f': 56.51,
        'm': 53.28
    },
    'morocco': {
        'f': 74.62,
        'm': 72.6
    },
    'papua new guinea': {
        'f': 64.49,
        'm': 60.25
    },
    'sierra leone': {
        'f': 50.74,
        'm': 49.65
    },
    'panama': {
        'f': 80.49,
        'm': 74.34
    },
    'south africa': {
        'f': 59.11,
        'm': 54.85
    },
    'nicaragua': {
        'f': 77.48,
        'm': 71.38
    },
    'haiti': {
        'f': 64.42,
        'm': 60.18
    },
    'israel': {
        'f': 85.61,
        'm': 79.59
    },
    'colombia': {
        'f': 77.39,
        'm': 70.19
    },
    'mongolia': {
        'f': 73.29,
        'm': 64.76
    },
    'guam': {
        'f': 81.47,
        'm': 76.14
    },
    'curaçao': {
        'f': 80.7,
        'm': 74.5
    },
    'eswatini': {
        'f': 48.54,
        'm': 49.69
    },
    'congo': {
        'f': 62.92,
        'm': 59.95
    },
    'ghana': {
        'f': 61.97,
        'm': 60.06
    },
    'niger': {
        'f': 61.55,
        'm': 59.85
    },
    'samoa': {
        'f': 76.39,
        'm': 70.02
    },
    'tajikistan': {
        'f': 72.84,
        'm': 65.9
    },
    'zambia': {
        'f': 60.33,
        'm': 57.16
    },
    'cape verde': {
        'f': 74.65,
        'm': 71.05
    },
    'georgia': {
        'f': 78.14,
        'm': 70.91
    },
    'taiwan': {
        'f': 82.3,
        'm': 76.43
    },
    'saudi arabia': {
        'f': 75.47,
        'm': 72.82
    },
    'channel islands': {
        'f': 82.39,
        'm': 78.45
    },
    'mexico': {
        'f': 78.93,
        'm': 74.04
    },
    'norway': {
        'f': 83.38,
        'm': 79.22
    },
    'vietnam': {
        'f': 80.31,
        'm': 70.73
    },
    'iran': {
        'f': 76.22,
        'm': 73.98
    },
    'india': {
        'f': 68.93,
        'm': 66.13
    },
    'uruguay': {
        'f': 80.44,
        'm': 73.25
    },
    'ecuador': {
        'f': 78.37,
        'm': 72.82
    },
    'egypt': {
        'f': 73.05,
        'm': 68.71
    },
    'kiribati': {
        'f': 68.93,
        'm': 62.55
    },
    'guatemala': {
        'f': 74.98,
        'm': 67.92
    },
    'vanuatu': {
        'f': 73.6,
        'm': 69.59
    },
    'reunion': {
        'f': 82.9,
        'm': 76.04
    },
    'united states': {
        'f': 81.25,
        'm': 76.47
    },
    'united arab emirates': {
        'f': 78.23,
        'm': 76.02
    },
    'japan': {
        'f': 86.58,
        'm': 80.91
    },
    'guinea-bissau': {
        'f': 56.5,
        'm': 53.0
    },
    'germany': {
        'f': 83.06,
        'm': 78.18
    },
    'lebanon': {
        'f': 80.87,
        'm': 77.14
    },
    'hungary': {
        'f': 78.54,
        'm': 71.23
    },
    'palestine': {
        'f': 74.66,
        'm': 70.74
    },
    'singapore': {
        'f': 84.74,
        'm': 80.43
    },
    'turkmenistan': {
        'f': 69.69,
        'm': 61.31
    },
    'malaysia': {
        'f': 76.88,
        'm': 72.21
    },
    'indonesia': {
        'f': 70.7,
        'm': 66.61
    },
    'jordan': {
        'f': 75.52,
        'm': 72.21
    },
    'republic of macedonia': {
        'f': 77.48,
        'm': 72.87
    },
    'albania': {
        'f': 80.19,
        'm': 75.04
    },
    'chad': {
        'f': 52.18,
        'm': 50.08
    },
    'paraguay': {
        'f': 74.92,
        'm': 70.7
    },
    'italy': {
        'f': 86.49,
        'm': 80.0
    },
    'sudan': {
        'f': 64.6,
        'm': 61.6
    },
    'qatar': {
        'f': 79.68,
        'm': 77.1
    },
    'greece': {
        'f': 83.6,
        'm': 77.64
    },
    'western sahara': {
        'f': 69.81,
        'm': 65.89
    },
    'namibia': {
        'f': 66.95,
        'm': 61.58
    },
    'angola': {
        'f': 53.17,
        'm': 50.2
    },
    'serbia': {
        'f': 77.5,
        'm': 71.83
    },
    'mali': {
        'f': 56.98,
        'm': 57.44
    },
    'nigeria': {
        'f': 52.61,
        'm': 51.97
    },
    'sweden': {
        'f': 83.71,
        'm': 80.1
    },
    'madagascar': {
        'f': 66.0,
        'm': 63.02
    },
    'grenada': {
        'f': 75.59,
        'm': 70.78
    },
    'el salvador': {
        'f': 77.08,
        'm': 67.89
    },
    'algeria': {
        'f': 76.84,
        'm': 72.14
    },
    'finland': {
        'f': 83.4,
        'm': 77.6
    },
    'bosnia and herzegovina': {
        'f': 78.82,
        'm': 73.71
    },
    'kuwait': {
        'f': 75.56,
        'm': 73.34
    },
    'tonga': {
        'f': 75.56,
        'm': 69.72
    },
    'french guiana': {
        'f': 82.58,
        'm': 75.75
    }
}

if __name__ == '__main__':
    run()
