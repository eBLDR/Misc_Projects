import pygal

SVG_FILENAME = 'insurance_chart.svg'

COST_MAPPER = {
    1: 1024,
    8: 1140
}

AVG_YEAR_DELTA = (COST_MAPPER[8] - COST_MAPPER[1]) / 8

SURRENDER_VALUES = {
    10: 4666,
    15: 9003,
    20: 29639,
    25: 42024,
    30: 56053,
    35: 73083,
    36: 76832,
    40: 93318,
    41: 97801,
    45: 114951,
    46: 119475
}

MAX_YEARS = max(SURRENDER_VALUES.keys())
MIN_YEARS = min(SURRENDER_VALUES.keys())


def calculate_total_cost_at_year(year):
    total = 0
    for i in range(1, year + 1):
        total += calculate_year_cost(i)

    return total


def calculate_year_cost(years):
    return COST_MAPPER[1] + (AVG_YEAR_DELTA * years) - AVG_YEAR_DELTA


def get_surrender_value(year):
    if year >= MAX_YEARS:
        value = SURRENDER_VALUES[MAX_YEARS]

    elif year < MIN_YEARS:
        # TODO: fill me if you wish
        value = 1

    else:
        value = SURRENDER_VALUES.get(year)

    while not value:
        year -= 1
        value = SURRENDER_VALUES.get(year)

    return value


def get_balance(accumulated_cost, year):
    return get_surrender_value(year) - accumulated_cost


def generate_chart(x_data, y_data):
    chart = pygal.Line()
    chart.title = 'Surrender Balance'
    chart.x_labels = x_data
    chart.add('Balance', y_data)

    chart.render_to_file(SVG_FILENAME)


def main(start, end):
    print('Avg year delta: ${}'.format(AVG_YEAR_DELTA))

    data = {}

    for year in range(start, end + 1):
        accumulated_cost = calculate_total_cost_at_year(year)
        balance = get_balance(accumulated_cost, year)

        print('Year {}: ${}'.format(year, calculate_year_cost(year)))
        print('Accumulated cost: ${}'.format(accumulated_cost))
        print('Surrender value: ${}'.format(get_surrender_value(year)))
        print('Balance: ${}'.format(balance))
        print('= ' * 10)

        data[year] = balance

    generate_chart(x_data=data.keys(), y_data=data.values())


if __name__ == '__main__':
    main(10, 50)
