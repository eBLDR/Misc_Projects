#!/usr/bin/python3
# 2019
import argparse
import csv
import datetime
import os
import sys

import pygal

FILENAME = 'bps_data.csv'
SVG_FILENAME = 'bps_chart.svg'
HEADERS = ['date', 'time', 'bpm']

DATE_FORMAT = '%Y-%m-%d'
TIME_FORMAT = '%H:%M'
PATH = os.path.join(os.getcwd(), FILENAME)


def assert_file():
    return os.path.isfile(PATH)


def read_data():
    if not assert_file():
        return

    data = []

    with open(PATH, 'r') as csv_file:
        read_csv = csv.reader(csv_file)

        for row in read_csv:
            data.append(row)

    return data


def insert_record(bpm, date, time):
    headers = None

    if not assert_file():
        headers = HEADERS

    row = [date, time, bpm]

    with open(PATH, 'a') as csv_file:
        write_csv = csv.writer(csv_file)

        if headers:
            write_csv.writerow(headers)

        write_csv.writerow(row)


def display_data():
    data = read_data()

    if not data:
        print('Register is empty')
        return

    print_row(HEADERS, upper_case=True)

    for record in data[1:]:
        print_row(record)


def print_row(row, upper_case=False):
    str_ = ''

    for item in row:
        str_ += '{:15}'.format(item)

    if upper_case:
        str_ = str_.upper()

    print(str_)


def generate_charts():
    data_csv = read_data()
    data = {}

    for row in data_csv[1:]:
        if row[0] not in data:
            data[row[0]] = {}

        data[row[0]].update(
            {row[1]: row[2]}
        )

    for date in data:
        generate_chart(date, data[date])


def generate_chart(date, data):
    chart = pygal.Line()
    chart.title = 'BPM {}'.format(date)
    chart.x_labels = data.keys()
    chart.add('BPM', list(map(int, data.values())))

    filename = str(date) + '_' + SVG_FILENAME
    chart.render_to_file(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Heart beat tracker.'
    )
    parser.add_argument(
        '--bpm', help='insert new record - beats per minute', default=None, type=int
    )
    parser.add_argument('-t', '--time', help='record\'s time', default=None)
    parser.add_argument('-c', '--chart', help='generate chart files', action='store_true')

    args = parser.parse_args()

    now = datetime.datetime.now()
    date = now.strftime(DATE_FORMAT)

    if args.time:
        try:
            datetime.datetime.strptime(args.time, TIME_FORMAT)
        except ValueError:
            print('Time format not ISO standard - {}'.format(TIME_FORMAT))
            sys.exit()

    else:
        args.time = now.strftime(TIME_FORMAT)

    if args.bpm:
        insert_record(args.bpm, date, args.time)

    display_data()

    if args.chart:
        generate_charts()
