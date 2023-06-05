basket=['Apple', 'Bun', 'Cola']
crate = ['Egg', 'Fig', 'Grape']
print('Basket List:', basket)
print('Basket Elements:', len(basket))
basket.append('Damson')
print('Appended:', basket)
print('Last Item Removed:', basket.pop())#Удаляем последний элемент из basket
print('Basket List:', basket)
basket.extend(crate)#расширяем первый список элементами второго.
print('Extended:', basket)
del basket[1]#Удаляем второй злемент из списка.
print('Item Removed:', basket)
del basket[1:3]#Удаляем со 2го по 3ий элемент из списка.
print('Slise Removed:', basket)
"""del[] - Удаляем элемент из списка
append-добавляем элемент в конец списка.
extend-Добавляем все элементы в конец списка.
insert(i,x)-вставляет элемент Х перед индексом i.
remove-Удаляет первый элемент из списка
pop-Удаляет элемент и возвращает его.
index-Возвращает индекс первого элемента в списке.
count-Возвращает количество вхождений элемента Х в список.
sort-Сортирует элементы списка по возрастанию.
revers-Обращает порядок следования элементов."""