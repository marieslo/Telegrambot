import requests

r = requests.get(f"https://currate.ru/api/?get=rates&pairs={base_key}{sym_key}&key=bbe2a1ac0b909431aa237bffff3c4fca")
print(r.content)
