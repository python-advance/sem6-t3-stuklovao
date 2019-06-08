    
from urllib.request import urlopen
from xml.etree import ElementTree as ET
import xml
import xmltodict
from json import dumps
from pprint import pprint
from abc import ABCMeta, abstractmethod

class Interface(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_data(self):
        pass

class CurrenciesXMLData(Interface):
    """
    Данные с сайта ЦБ в XML формате
    """
    def get_data(self):
        cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
        return ET.tostring(ET.parse(cur_res_str).getroot(),encoding="unicode")

class CurrenciesJSONData(Interface):
    """
    Данные с сайта ЦБ в XML формате
    """
    def __init__(self, obj):
        self.obj = obj

    def get_data(self):
        """
        Данные в JSON формат
        """
        cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
        root = ET.tostring(ET.parse(cur_res_str).getroot(),encoding="unicode")
        return dumps(xmltodict.parse(root, encoding='utf-8'), ensure_ascii=False)

    def serialize(self):
        """
        Сохранение данных в файл с расшерением .json
        """
        with open('result.json', 'w', encoding='utf-8') as f:
            f.write(self.get_data())

a = CurrenciesXMLData()
b = CurrenciesJSONData(a)
print(a.get_data())
print(b.get_data())
b.serialize()
