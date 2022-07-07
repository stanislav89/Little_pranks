''' Банкомат выдаёт сумму мелкими купюрами, но не больше 10 штук каждой купюры '''
''' The ATM dispenses the amount in small bills, but not more than 10 pieces of each bill '''

bill_20 = [10, 20]  # 10 bills of 20 hryvnia
bill_50 = [10, 50]
bill_100 = [10, 100]
bill_200 = [10, 200]
bill_500 = [10, 500]
withdraw_amount = int(input('*** Enter the amount you want to withdraw: '))

while withdraw_amount >= 0:
    if withdraw_amount > bill_20[1] and bill_20[0] > 0:
        print('...20...')
        withdraw_amount -= bill_20[1]
        bill_20[0] -= 1
    elif withdraw_amount > bill_50[1] and bill_50[0] > 0:
        print('...50...')
        withdraw_amount -= bill_50[1]
        bill_50[0] -= 1
    elif withdraw_amount > bill_100[1] and bill_100[0] > 0:
        print('...100...')
        withdraw_amount -= bill_100[1]
        bill_100[0] -= 1
    elif withdraw_amount > bill_200[1] and bill_200[0] > 0:
        print('...200...')
        withdraw_amount -= bill_200[1]
        bill_200[0] -= 1
    elif withdraw_amount > bill_500[1] and bill_500[0] > 0:
        print('...500...')
        withdraw_amount -= bill_500[1]
        bill_500[0] -= 1
    else:
        print('*** You got your money! \n Remaining amount = ' + str(withdraw_amount))
        break
