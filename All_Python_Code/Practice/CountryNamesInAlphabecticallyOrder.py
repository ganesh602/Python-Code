country = {}

for i in range(5):
    name = input("Enter Country Name : ")
    if name[0].upper() not in country:
        country[name[0].upper()] = [name]
    else:
        country[name[0].upper()].append(name)
print(country)