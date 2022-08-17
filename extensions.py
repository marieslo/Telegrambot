import requests
import json
from config import keys

class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base_key, sym_key, amount):
        try:
            base_key = keys[base_key.lower()]
        except KeyError:
            raise APIException(f"Валюта {base_key} не найдена!")

        try:
            sym_key = keys[sym_key.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym_key} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base_key}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        r = requests.get(
            f"https://currate.ru/api/?get=rates&pairs={base_key}{sym_key}&key=bbe2a1ac0b909431aa237bffff3c4fca")
        print(r.content)
        resp = json.loads(r.content)
        new_price = float(resp['data'][base_key+sym_key]) * amount
        new_price = round(new_price, 2)
        message =  f"Цена {amount} {base_key} в {sym_key} : {new_price}"
        return message
