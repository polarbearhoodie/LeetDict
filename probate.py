def probate_costs_CA(estate_gross):
    gross = estate_gross
    price_percents = [[0.04, 100000], [0.03, 100000], [0.02, 800000], [0.01, 9000000], [0.005, 15000000]]
    total_cost = 0

    for i in range(len(price_percents)):
        if gross > price_percents[i][1]:
            gross -= price_percents[i][1]
            total_cost += price_percents[i][0] * price_percents[i][1]
        else:
            total_cost += price_percents[i][0] * gross
            break

    return total_cost
