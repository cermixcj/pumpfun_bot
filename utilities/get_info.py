def token_ca(data: list):
    result = []
    for mint in data:
        ca = mint.get('mint')
        result.append(ca)
    return result


def name_token(data: list):
    result = []
    for names in data:
        name = names.get('name')
        result.append(name)
    return result


def twitter(data: list):
    result = []
    for items in data:
        twitters = items.get('twitter')
        result.append(twitters)
    return result


def telegram(data: list):
    result = []
    for items in data:
        telegrams = items.get('telegram')
        result.append(telegrams)
    return result


def website_token(data: list):
    result = []
    for websites in data:
        website = websites.get('website')
        result.append(website)
    return result


def creator_token(data: list):
    result = []
    for creators in data:
        creator = creators.get('creator')
        result.append(creator)
    return result


def market_cap_usdt(data: list):
    result = []
    for market_caps in data:
        market_cap = market_caps.get('usd_market_cap')
        result.append(market_cap)
    return result


def market_cap_sol(data: list):
    result = []
    for market_caps_sol in data:
        market_cap = market_caps_sol.get('market_cap')
        result.append(market_cap)
    return result