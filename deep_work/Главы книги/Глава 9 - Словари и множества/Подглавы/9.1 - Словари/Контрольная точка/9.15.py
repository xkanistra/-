phonebook = {'Крис':'919-555-1111', 'Кэти':'828-555-2222',
             'Джоанна':'704-555-3333', 'Курт':'919-555-3333'}
sort_phonenumber = {k:v for k,v in phonebook.items() if v.startswith('919')}
print(sort_phonenumber)