import os
import datetime
import requests


api_key = os.environ.get('api_key')
valid_collections = ['USCOURTS', 'BILLS', 'CHRG', 'FR', 'GAOREPORTS', 'GOVPUB', 'CPD', 'CZIC', 'CFR', 'PLAW', 'CREC',
                     'CCAL', 'GPO', 'CDOC', 'CRECB', 'CPRT', 'PAI', 'USCODE', 'ERIC', 'BUDGET', 'ECONI', 'LSA', 'PPP',
                     'STATUTE', 'HOB', 'ERP', 'GOVMAN', 'CDIR', 'HMAN', 'HJOURNAL', 'SMAN']


def get_date():
    print('Enter date in YYYY-MM-DD format: ')
    date = input()
    validate_date(date)
    return date


def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Incorrect date format')


def get_collection():
    print('Enter collection: ')
    collection = input()
    if collection not in valid_collections:
        print(f'{collection} is not valid, please choose a valid collection.')


# def validate_collection(collection):
#     try:
#         collection in valid_collections


collection = input()
start_date = get_date()
end_date = get_date()
url = f'https://api.govinfo.gov/published/{start_date}{end_date}?offset=0&pageSize=10&collection={collection}&api_key={api_key} '
billz = requests.get()
print(billz.text)
