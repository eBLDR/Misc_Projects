import datetime


def get_item_from_list(group_name, list_):
    print('Possible {}:\n- {}\n'.format(group_name.title(), '\n- '.join(list_)))
    list_lower = [item.lower() for item in list_]
    while True:
        item = input('> ').lower()
        if item in list_lower:
            return item


def set_label():
    while True:
        label = input('Label:\n> ')
        if label:
            # if input('Confirm label \033[1m{}\033[0m [y/*]:\n> '.format(label)).lower() == 'y':
            return label


def set_year(today, not_less_than=None):
    while True:
        year = input('Year:\n> ')
        if year.isdigit() and 1900 <= int(year) <= today.year:
            if (not_less_than and not_less_than <= int(year)) or not not_less_than:
                return year
        print('Invalid year!')


def set_month(today, year, not_less_than=None):
    while True:
        month = input('Month:\n> ')
        if month.isdigit():
            if (year != today.year and 1 <= int(month) <= 12) or (year == today.year and 1 <= int(month) <= today.month):
                if (not_less_than and not_less_than <= int(month)) or not not_less_than:
                    return month
        print('Invalid month!')


def set_date(to_present_available=False, not_less_than=None):
    if to_present_available:
        while True:
            option = input('To <present> or to <date>:\n> ').lower()
            if option == 'present':
                return 'present'
            elif option == 'date':
                break

    today = datetime.date.today()
    while True:
        if not_less_than:
            min_year, min_month = not_less_than.split('-')[0], not_less_than.split('-')[1]
            year = set_year(today, not_less_than=int(min_year))
            month = set_month(today, year, not_less_than=int(min_month) if year == min_year else None)
        else:
            year = set_year(today)
            month = set_month(today, year)
        date = '{}-{}'.format(year, month)
        # if input('Confirm date \033[1m{}\033[0m [y/*]:\n> '.format(date)).lower() == 'y':
        return date
