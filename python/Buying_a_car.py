def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    keep_saving = True
    month_count = 1
    savings_account = 0

    while keep_saving:

        money_left = (startPriceOld + savings_account) - startPriceNew

        if month_count % 2 == 0 and month_count > 0:
            percentLossByMonth += 0.5

        if money_left >= 0:
            return [month_count - 1, round(money_left)]
        else:
            startPriceNew -= (startPriceNew * (percentLossByMonth / 100))
            startPriceOld -= (startPriceOld * (percentLossByMonth/ 100))
            savings_account += savingperMonth
            month_count += 1