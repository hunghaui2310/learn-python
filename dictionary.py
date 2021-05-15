# dictionary: A changeable, unordered collection of unique key: value pairs.
#     Fast because they use hashing, allow us to access a value quickly

capitals = {
    'USA': 'Washington DC',
    'India': 'New Dehli',
    'China': 'Beijing',
    'Russia': 'Moscow',
}

print(capitals.get('VN'))
print(capitals.keys())
print(capitals.values())

for key,val in capitals.items():
    print(key, val)

capitals.update({'VN': 'Ha Noi'})
capitals.update({'China': 'Tau khua'})
print(capitals)