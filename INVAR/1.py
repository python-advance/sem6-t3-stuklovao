from urllib.request import urlopen
from xml.etree import ElementTree as ET
import time

def get_currencies(currencies_ids_lst=['R01235', 'R01239', 'R01820']):
    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
    result = {}
    cur_res_xml = ET.parse(cur_res_str)
    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')
        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            result[valute_id] = valute_cur_val
    time.clock()
    return result

class CurrencyBoard():

    def __init__(self):

        self.currencies = ['R01235','R01239','R01820']
        self.rates = get_currencies(self.currencies)

    def get_from_cache(self, code):
        return self.currencies[code]

    def get_new_currency(self, code):
        self.currencies.append(code)
        self.rates.update(get_currencies([code]))
        return self.rates[code]

    def update(self):
        new = get_currencies(self.currencies)
        self.rates.update(dict(zip(sorted(self.currencies),new.values())))
        return self.rates

    def check(self):
        if (time.clock() > 5*60):
            return get_currencies(self.currencies)
        else:
            print('Обновление не требуется')

cur_vals = get_currencies()

print("\ndollar = USD = R01235 \neuro = EUR = R01239 \niena = GBP = R01820  \n", cur_vals)
