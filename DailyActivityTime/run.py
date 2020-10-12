import argparse

from daily_activity_time.time_use import TimeUse


def main():
    parser = argparse.ArgumentParser(description='Daily Activity Time')
    parser.add_argument('file', help='Input csv file')
    parser.add_argument(
        '-hu',
        '--hide_unassigned',
        help='Enable to hide auto-generated "unassigned" activity',
        action='store_true',
    )

    args = parser.parse_args()
    input_filename = args.file
    display_unassigned = not args.hide_unassigned

    time_use = TimeUse(
        input_filename,
        display_unassigned=display_unassigned,
    )

    time_use.run()


if __name__ == '__main__':
    main()
