import requests
import pprint

url='https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
if response.status_code != requests.codes.ok :
    '''
    если запрос к странице не успешен 
    '''
    print(f'{url} not aviable')
    exit()

response=response.json()

currents=[] # список строк о валютах по отношению к рублю

# словарь валют, информация о каждой валюте - словарь. Например
# "ID": "R01010",
# "NumCode": "036",
# "CharCode": "AUD",
# "Nominal": 1,
# "Name": "Австралийский доллар",
# "Value": 37.1232,
# "Previous": 37.3252
current_dict=response['Valute']  # словарь валют

for code in current_dict.keys():
    '''
    проход по словарю валют и формирование строки для записи в список
    '''
    item = str(current_dict[code]['Nominal']) +' '+ \
           current_dict[code]['Name'] + ' '+\
           ' = '+ str(current_dict[code]['Value']) + ' руб. ' +\
           ' ('+ \
           str(round(current_dict[code]['Value'] / current_dict[code]['Previous'] *100 -100  ,2)) + \
           ' %)'

    currents.append(item)

pprint.pprint(currents)
