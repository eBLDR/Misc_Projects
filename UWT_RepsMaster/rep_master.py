#! /usr/bin/python3

"""
Data Structure Sample:

- Goals:
data_file['goals1] = {'period': (2018, 2), 'start_day': 12, 'reps': [1, 1, 1, ..., 1]}

- Workout:
data_file['w1'] = {'period': (2018, 2), 'day': 12, 'reps': [1, 1, 1, ..., 1]}
"""

import shelve
import datetime
import os
import sys


def clear_terminal():
    os.system('clear')


def get_date():
    now = datetime.date.today()
    return now.day, now.month, now.year


def get_period(day_only=False):
    # returns the current OS date in format (DD, MM, YYY)
    now = datetime.date.today()
    if day_only:
        return now.day
    return now.year, now.month


def input_year():
    while True:
        year = input("Year: ")
        if year.isdigit():
            year = int(year)
            if 2000 <= year <= get_date()[2]:
                return year


def input_month(year):
    while True:
        month = input("Month: ")
        if month.isdigit():
            month = int(month)
            if year == get_date()[2]:  # workout done in the current year
                if 1 <= month <= get_date()[1]:
                    return month
            else:
                return month


def input_day(month, year):
    while True:
        day = input("Day: ")
        if day.isdigit():
            day = int(day)
            if month == 2:
                days = 28
                if year % 4 == 0:
                    days = 29
            elif month in [4, 6, 9, 11]:
                days = 30
            else:
                days = 31
            if 1 <= day <= days:
                return day


"""
def get_ending_date(months):
    date = get_period()
    supposed_month = date[1] + months
    if supposed_month > 12:  # changing year
        year = date[2] + (supposed_month // 12)
        month = supposed_month % 12
    else:
        month = supposed_month
        year = date[2]

    if month == 2 and date > 28:
        day = 28
    elif date[0] == 31 and month in [4, 6, 9, 11]:
        day = 30
    else:
        day = date[0]
    return day, month, year
"""


def get_number(prompt):
    while True:
        n = input(prompt)
        if n.isdigit():
            return int(n)


def get_option(opts):
    display_menu(opts)
    while True:
        opt = input("Choose: ").lower()
        if opt == 'quit':
            sys.exit()
        elif opt in opts.keys():
            return opt


def display_menu(opts):
    clear_terminal()
    print(title)
    for opt in sorted(opts.keys()):
        print("- {}".format(opts[opt]['descr']))
    print("- Quit")


def find_key_number(name, file):
    number = 1
    while True:
        key_name = '{}{}'.format(name, number)
        if key_name not in file.keys():
            break
        number += 1
    return number


def set_goals(data_strct, file):
    current_period = get_period()
    if not get_period_goals_key(file, current_period):
        key_name = 'goals'
        number = find_key_number(key_name, file)
        key_name = key_name + str(number)
        file[key_name] = fill_goals(data_strct)
    else:
        print("Goals already set for {} period.".format(current_period))
        input("\n<enter>")


def get_period_goals_key(file, period):
    for key in file.keys():
        if key[:2] == 'go':
            if file[key]['period'] == period:
                return key
    else:
        return False


def fill_goals(data_strct):
    while True:
        goal_reps = []
        print("Reps to be done during this month.")
        for exercise in data_strct['reps']:
            goal_reps.append(get_number("\tTotal # of {}: ".format(exercise)))
        if confirm_data(data_strct, goal_reps, goal=True):
            return {'period': get_period(), 'start_day': get_period(day_only=True), 'reps': goal_reps}


def confirm_data(data_strct, data_to_confirm, date=None, goal=False):
    clear_terminal()
    for exercise, rep_num in zip(data_strct['reps'], data_to_confirm):
        print("{} {}".format(exercise.ljust(12, '-'), rep_num))
    if goal:
        print("To be completed before the end of this month.")
    else:
        print("Done on the {}".format(date))
    while True:
        c = input("\nIs that correct [y/n]? ").lower()
        if c == 'y':
            return True
        elif c == 'n':
            clear_terminal()
            return False


def add_workout(data_strct, file):
    # finding workout number
    key_name = 'w'
    number = find_key_number(key_name, file)
    key_name = key_name + str(number)
    today = get_date()
    while True:
        is_today = input("Has the workout been done today {} [y/n]? ".format(today)).lower()
        if is_today == 'y':
            period = get_period()
            day = get_period(day_only=True)
            break
        elif is_today == 'n':
            ok = False
            while not ok:
                print("Introduce date")
                year = input_year()
                month = input_month(year)
                day = input_day(month, year)
                period = year, month
                while True:
                    print("\n({}, {}, {})".format(day, month, year))
                    c = input("\nIs that correct [y/n]? ").lower()
                    if c == 'y':
                        ok = True
                        break
                    elif c == 'n':
                        clear_terminal()
                        break
            break

    clear_terminal()
    # saving workout to file
    file[key_name] = {'period': period, 'day': day, 'reps': fill_reps(data_strct, number,
                                                                      date=(day, period[1], period[0]))}


def fill_reps(data_strct, num, date):
    while True:
        reps = []
        print("WORKOUT # {}".format(num).center(30, '-') + '\n')
        for exercise in data_strct['reps']:
            reps.append(get_number("# of {}: ".format(exercise)))
        if confirm_data(data_strct, reps, date):
            return reps


def display_progress(data_strct, file):
    while True:
        lapse = input("Display progress for <current> period or <total> progress: ").lower()
        if lapse == 'current':
            clear_terminal()
            current_period = get_period()
            display_period_progress(data_strct, file, current_period)
            break
        elif lapse == 'total':
            clear_terminal()
            abs_total_reps, abs_num_workouts = 0, 0
            used_periods = []
            for key in file.keys():
                if key[:1] == 'w':
                    period = file[key]['period']
                    if period not in used_periods:
                        used_periods.append(period)
            for period in sorted(used_periods, reverse=True):
                partial_reps, partial_num_workouts = display_period_progress(data_strct, file, all_=True,
                                                                             period=period)
                abs_total_reps += partial_reps
                abs_num_workouts += partial_num_workouts

            print("=" * 40)
            print("\nAbsolute total # of workouts: {}".format(abs_num_workouts))
            print("\nAbsolute total # of reps: {}".format(abs_total_reps))
            input("\n<enter>")
            break


def display_period_progress(data_strct, file, period, all_=False):
    print(title)
    print("\nProgress for {}".format(period))
    print("\n" + " Total reps/goal ".center(40, '=') + '\n')

    period_key_goals = get_period_goals_key(file, period)
    total_reps = 0  # num of total reps of any exercise
    num_workouts = 0  # num of workouts

    for i in range(len(data_strct['reps'])):
        subtotal = 0  # num of total reps of a certain exercise
        for key in file.keys():
            if key[:1] == 'w':
                if file[key]['period'] == period:
                    subtotal += file[key]['reps'][i]
                    num_workouts += 1

        rep_goal = ' -'
        ok_or_x = ''
        if period_key_goals:
            rep_goal = file[period_key_goals]['reps'][i]
            if subtotal < rep_goal:
                ok_or_x = 'X'
            else:
                ok_or_x = 'OK'
        print("\t{} {}/{} {}".format(data_strct['reps'][i].ljust(15, '-'), str(subtotal).rjust(6),
                                     str(rep_goal).ljust(5), ok_or_x.rjust(3)))
        total_reps += subtotal

    num_workouts = round(num_workouts/len(data_strct['reps']))
    print("\nTotal # of workouts: {}".format(num_workouts))
    print("\nTotal # of reps: {}".format(total_reps) + '\n')

    if all_:
        return total_reps, num_workouts

    input("<enter>")


def choose_profile(profs):
    print(title)
    print("Select profile:")
    for profile in profs:
        print("- {}".format(profile))
    while True:
        who_is = input("Choose: ").upper()
        if who_is in profs:
            return who_is


title = " UNBREAKABLE - REPS MASTER ".center(40, '=')

# options available
options = {'add': {'descr': '<Add> new workout', 'func': add_workout},
           'progress': {'descr': 'See training <progress>', 'func': display_progress},
           'goals': {'descr': 'Set monthly <goals> for {}'.format(get_period()), 'func': set_goals}}

# for reference and displaying
data_structure = {'period': (0, 0), 'day': 0, 'reps': ['Push Ups', 'Pull Ups', 'Dips',
                                                       'Rows', 'Squats', 'V Push', 'Crunches']}

profiles = ['BLDR', 'ALLY']

if __name__ == '__main__':
    clear_terminal()
    account = choose_profile(profiles)
    file_name = '{}-wdata'.format(account.lower())
    clear_terminal()
    while True:
        option = get_option(options)
        clear_terminal()
        # action
        with shelve.open(file_name) as data_file:
            options[option]['func'](data_structure, data_file)
