import requests
from fake_useragent import UserAgent
from utilities.params_utility import *
from utilities.get_info import *


def get_response():
    ua = UserAgent().random
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'if-none-match': 'W/"fba1-yPAB4i7J3DGZE/QAOVrdKj2bw7k"',
        'origin': 'https://pump.fun',
        'priority': 'u=1, i',
        'referer': 'https://pump.fun/',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': ua,
    }

    params = get_params_creation_time()

    response = requests.get('https://frontend-api-v3.pump.fun/coins/for-you', params=params, headers=headers)
    return response


def get_data(params):
    response = get_response()
    data = response.json()
    return data


def selection_mode(selection_mods):
    if selection_mods == 1:
        return get_params_last_reply()
    if selection_mods == 2:
        return get_params_featured()
    if selection_mods == 3:
        return get_params_creation_time()
    if selection_mods == 4:
        return get_params_last_trade()
    if selection_mods == 5:
        return get_params_market_cap()


def selection():
    return int(input(
        'Введите мод:\n'
        '1 - last_reply\n'
        '2 - featured\n'
        '3 - creation_time\n'
        '4 - last_trade\n'
        '5 - market_cap\n'
    ))

def information(data):
    names = name_token(data)
    token_cas = token_ca(data)
    creator_tokens = creator_token(data)
    market_cap_in_usdt = market_cap_usdt(data)
    market_cap_in_sol = market_cap_sol(data)
    twitters = twitter(data)
    telegrams = telegram(data)
    websites = website_token(data)

    for i in range(len(twitters)):
        print(f'Name: {names[i]}')
        print(f'CA: {token_cas[i]}')
        print(f'Creator: {creator_tokens[i]}')
        print(f'Market Cap USDT: {market_cap_in_usdt[i]}')
        print(f'Market Cap SOL: {market_cap_in_sol[i]}')
        if twitters[i] is not None:
            print(f'Twitter: {twitters[i]}')
        else:
            print('Telegram: Отсутствует')

        if telegrams[i] is not None:
            print(f'Telegram: {telegrams[i]}')
        else:
            print('Telegram: Отсутствует')

        if websites[i] is not None:
            print(f'Websites: {websites[i]}')
        else:
            print('Websites: Отсутствует')

        print(20 * '------')


def main():
    mod = selection()
    params = selection_mode(mod)
    data = get_data(params)
    information(data)


if __name__ == '__main__':
    main()








