#Returns True if this frozenset is a (proper) subset of another.
a=frozenset({1,2})
b=frozenset({1,2,3})
print(a.issubset(b))
print(a<=b)
print(a<b)