"""

Set:
    - a collection
    - unordered
    - unindexed, you cannot access then throgh index
    - created with {}
    - don't allow duplicates
 """

myset = {'mangoes', 'guaves', 'berries', 'honeydew', 'mangoes'}
print(myset)
print(len(myset))

for x in myset:
    print(x)

print("honeydew" in myset)

"""
Add items in a set:

"""
myset.add('cantaloup')
print(myset)

nuts = {'chasew', 'peanut'}
myset.update(nuts)
print(myset)

citrus = ['orange', 'tangerine']
myset.update(citrus)
print(myset)

"""
removing elements from a set:
    - remove <<set>>(<<item>>) this generates an error if the item doesn't exist
    - pop: removes the last item in the set, but remember that the set is unordered, thus you have no idea/control of what is removed
    - discard: doesnt return error if item isnt fount
    - clear 

"""





myset.discard('passion')

myset.pop()
print(myset)

"""
Joining of sets:
- union - (like venn diagram) creaete a new set with item from the 2 sets
union also removes duplicates if it occurs

"""
set1 = {'honeydew', 'mangoes', 'berries', 'guavas'}
set2 = {'berries', 'tangerine', 'peanut'}

set3 = set1.union(set2)
print(set3)

"""
to get common values within a set
-intersection
"""
set1.intersection_update(set2)
print(set1)
print(set2)
print(set3)
set3.symmetric_difference_update(set2)
print(set3)

print(set3.isdisjoint(set2))
