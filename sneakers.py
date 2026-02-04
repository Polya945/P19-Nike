from pprint import pprint


def load_data():
    with open('D:\\prog\\[P 19] Nike\\Nike_shoes_2023-04-16.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    headers = lines[0].strip().split(',')
    data = []

    for line in lines[1:]:
        values = line.strip().split(',')
        shoe = {}

        for i in range(len(headers)):
            if headers[i] == 'fullPrice' or headers[i] == 'currentPrice':
                shoe[headers[i]] = float(values[i])
            else:
                shoe[headers[i]] = values[i]

        data.append(shoe)

    return data


def main():
    shoes = load_data()
    print('Lehetőségek: ')
    print('1 - title')
    print('2 - color_breif')
    print('3 - fullPrice')
    print('4 - currentPrice')
    print('5 - publish_date')

    choice = int(input('Válassz egyet: '))

    keys = ['title', 'color_breif', 'fullPrice', 'currentPrice', 'publish_date']
    key = keys[choice - 1]

    shoes = sorted(shoes, key=lambda x: x[key])

    pprint(shoes, sort_dicts=False)


main()
