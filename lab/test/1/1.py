# len of list => number of people who want to buy ticket
# ticket desk has $0 initially
# people only have $250 OR $500 OR $1000
# True if all can buy ticket else False

# [250, 250, 500] => True;
# TEST CASE
# [250, 500, 500] => False
# [250, 1000] => False
# [250, 250, 500, 500] => True


# when we encounter $500, we've need to check if we've 1x $250
# when we encounter $1000, we've need to check if we've 4x $250 or 2x $500


def sellMovieTickets(cash):
    """Sell move tickets to all or none"""

    cash_reserve = {250: 0, 500: 0, 1000: 0}

    def increment(k):
        cash_reserve[k] = cash_reserve[k] + 1

    can_sell_all = True
    for money in cash:
        if money == 250:
            increment(250)
        elif money == 500:
            increment(500)
        elif money == 1000:
            increment(1000)
        else:
            pass

    for money in cash:
        if money == 500:
            if 250 * cash_reserve[250] != 500 * cash_reserve[500] // 2:
                can_sell_all = False
                break
        elif money == 1000:
            if (
                250 * cash_reserve[250] != (1000 * cash_reserve[1000]) // 4
                or 500 * cash_reserve[500] != (1000 * cash_reserve[1000]) // 2
            ):
                can_sell_all = False
                break
        else:
            pass

    return can_sell_all


def main():
    print(sellMovieTickets([250, 500, 500]))
    print(sellMovieTickets([250, 1000]))
    print(sellMovieTickets([250, 250, 500, 500]))


if __name__ == "__main__":
    main()
