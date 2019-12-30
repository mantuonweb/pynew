fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

fruits.count('tangerine')

fruits.index('banana')

print(fruits.index('banana', 3))  # Find next banana starting a position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()

#dynamic generation
dylist = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(dylist)