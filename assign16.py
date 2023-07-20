# Write a Python program to implement Set Union and Intersection operations.

set1 = set([1, 2, 3, 5, 7, 10])
set2 = set([5, 6, 2, 6, 1, 0])

#print(type(set1))

union_set1 = set1.union(set2)
union_set2 = set1|set2

print(union_set1)
print(union_set2)

intesection_set1 = set1.intersection(set2)
intesection_set2 = set1&set2

print(intesection_set1)
print(intesection_set2)