import json

# json - {"name" : "Radek"}
# obiekt typu para klucz-wartość
# odpowiednikiem jsona w pythonie jest słownik

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
# {"name": "Radek", "age": 40, "czy_pali": null}

# upiekszenie
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# upiększony i posortowany
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

# zamiana słownika na json
json_text = json.dumps(data)
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_text))  # <class 'str'>

# zamian jsona (str) na słownik
dict_json = json.loads(json_text)
print(dict_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>
