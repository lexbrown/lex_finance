import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def stock_exchange_gain(buy, sell, qty=1, lot=10, fee=0.0004, lev =1.0 , kind='long'):
    def bprint(str1, str2):
        diap = 50
        print(str1,'-'*(diap-len(str1)), str2)
    if kind =='long':
        investment = buy*qty*lot
        own_share = investment / lev
        buy_fee = max(investment*fee, 41.3) + investment*0.0001  #минимум 50р за сделку + Комиссия за урегулирование сделок
        selling = sell*qty*lot
        sell_fee = max(selling*fee, 41.3) + selling*0.0001 #selling*fee 
        profit =  selling - investment - buy_fee - sell_fee
        #print(f'Инвестировал {investment} рублей')
        #print(f'Из них собственных {own_share} рублей')
        #print(f'Комиссия за инвестиции {buy_fee} рублей')
        #print(f'Изменение стоимости актива составило {round(((selling/investment)-1)*100, 2)} %')
        #print(f'Комиссия за продажу актива {sell_fee} рублей')
        #print(f'Вложения увеличились на {selling - investment} рублей до комиссии')
        #print(f'Доход от инвестиции составил {profit} рублей')
        #print(f'Чистая доходность инвестиции {round((profit/own_share)*100, 2)} %')
        bprint('Инвестировал', f'{investment} рублей')
        bprint('Из них собственных', f'{own_share} рублей')
        bprint('Комиссия за инвестиции', f'{buy_fee} рублей')
        bprint('Изменение стоимости актива составило', f'{round(((selling/investment)-1)*100, 2)} %')
        bprint('Комиссия за продажу актива', f'{sell_fee} рублей')
        bprint('Вложения до комиссии увеличились на', f'{selling - investment} рублей ')
        bprint('Доход от инвестиции составил', f'{profit} рублей')
        bprint('Чистая доходность инвестиции', f'{round((profit/own_share)*100, 2)} %')