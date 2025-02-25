def get_params_last_reply():
    params_last_reply = {
        'offset': '0',
        'limit': '48',
        'sort': 'last_reply',
        'includeNsfw': 'true',
        'order': 'DESC',
    }
    return params_last_reply


def get_params_featured():
    params_featured = {
        'offset': '0',
        'limit': '48',
        'includeNsfw': 'true',
    }
    return params_featured


def get_params_creation_time():
    params_creation_time = {
        'offset': '0',
        'limit': '48',
        'sort': 'created_timestamp',
        'includeNsfw': 'true',
        'order': 'DESC',
    }
    return params_creation_time


def get_params_last_trade():
    params_last_trade = {
        'offset': '0',
        'limit': '48',
        'sort': 'last_trade_timestamp',
        'includeNsfw': 'true',
        'order': 'DESC',
    }
    return params_last_trade


def get_params_market_cap():
    params_market_cap = {
        'offset': '0',
        'limit': '48',
        'sort': 'market_cap',
        'includeNsfw': 'true',
        'order': 'DESC',
    }
    return params_market_cap



