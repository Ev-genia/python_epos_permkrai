auto_list = [
    ['skoda', 2019, 47000],
    ['kia', 2013, 78000],
    ['lada', 2010, 30000],
]
print('auto_list: ', auto_list)
for i in auto_list:
    if i[0] == 'skoda':
        print('best auto: ', i)
auto_dict = {
    'skoda': {'year': 2019, 'distance': 47000},
    'kia': {'year': 2013, 'distance': 78000},
    'lada': {'year': 2010, 'distance': 30000}
}
print('auto_dict: ', auto_dict)
for key, val in auto_dict.items():
    if key == 'skoda':
        print('best auto: ', key, val)
print('skoda: ', auto_dict['skoda'])
auto_set = set()
auto_set.add(('skoda', 2019, 47000))
auto_set.add(('kia', 2013, 78000))
auto_set.add(('lada', 2010, 30000))
print('auto_set: ', auto_set)
for i in auto_set:
    if i[0] == 'skoda':
        print('best auto: ', i)

"""В словаре ключ должен быть уникальным, соответственно нельзя туда занести 
два автомобиля разных лет выпуска, множества и списки для этого больше подходят.
По части сортировки не возникло трудности ни со списком, ни со словарем, 
ни со множеством. Для целей хранения списка автомобилей на базе, скорее всего 
подойдет множество, особенно если добавить поле 'количество'."""