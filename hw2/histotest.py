from homework2 import histogram, addressbook

data = [-2, -2.2, 0, 5.6, 8.3, 10.1, 30, 4.4, 1.9, -3.3, 9, 8]
hist = histogram(data, 10, -5, 10)
print(hist)

data = [-4, -3.2, 0, 7.6, 1.0, 2.2, 30, 2.2, 1.9, -8.3, 6, 5]
hist = histogram(data, 10, -5, 10)
print(hist)

data = [2,2,2]
hist = histogram(data, 3, -2, 3)
print(hist)

data = [-1,-1,-1,10,10]
hist = histogram(data, 5, -1, 10)
print(hist)


name_to_phone = {'alice': 5678982231, 'bob': '111-234-5678', 'christine': 5556412237, 'daniel': '959-201-3198', 'edward': 5678982231}
name_to_address = {'alice': '11 hillview ave', 'bob': '25 arbor way', 'christine': '11 hillview ave', 'daniel': '180 ways court', 'edward': '11 hillview ave'}
address_to_all = addressbook(name_to_phone, name_to_address)
print(address_to_all)

name_to_phone = {'alice': 5678982231, 'bob': 5678982231, 'christine': 5678982231, 'daniel': '959-201-3198', 'edward': 5678982231}
name_to_address = {'alice': '25 arbor way', 'bob': '25 arbor way', 'christine': '25 arbor way', 'daniel': '25 arbor way', 'edward': '25 arbor way'}
address_to_all_Stu = addressbook(name_to_phone, name_to_address)
print(address_to_all_Stu)