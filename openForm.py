from csv import reader

data = open("AppleStore.csv", "r", encoding="utf8")


#print(data)

data_read = reader(data)

#print(data_read)

data_set = list(data_read)

# suma de el precio del dataset
total_price = 0

for data in data_set[1:7]:
    total_price += float(data[5])
    
print(total_price)

for data in data_set:
    print(data[-1])


#print(data_set[1][5])