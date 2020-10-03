import argparse

from data.time_use import TimeUse


def main():
    parser = argparse.ArgumentParser(description='Daily Activity Time')
    parser.add_argument('file', help='Input csv file')
    parser.add_argument(
        '-m',
        '--manual',
        help='Enable to get data from user input instead of csv file',
        action='store_true',
    )
    parser.add_argument(
        '-hu',
        '--hide_unassigned',
        help='Enable to hide auto-generated "unassigned" activity',
        action='store_true',
    )

    args = parser.parse_args()
    input_filename = args.file
    auto = not args.manual
    display_unassigned = not args.hide_unassigned

    time_use = TimeUse(
        input_filename,
        auto=auto,
        display_unassigned=display_unassigned,
    )

    time_use.run()


if __name__ == '__main__':
    main()
