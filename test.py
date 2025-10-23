raw_list = "I:Item A|A1|A2|A3\nI:Item B|A2|A3|A4".split('\n')
items = [entry for entry in raw_list if entry.startswith("I:")]
item_names = [entry[2:].split('|')[0] for entry in items if entry[0] == 'I']

print(item_names)