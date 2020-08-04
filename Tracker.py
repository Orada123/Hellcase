items = {'https://hellcase.com/en/profile/7279625': 'Negev Loudmouth', 'https://hellcase.com/en/profile/7279625': 'Negev Loudmouth'}

if identifier not in items.keys():
    items[identifier] = weapon_full
if identifier in items.keys() and weapon_full not in items.values():
    items[identifier] = weapon_full