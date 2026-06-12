#.........BITWISE...........#
#&,|,^,~,<<,>>
#Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
#AND 1 & 1 → 1, 1 & 0 → 0, 0 & 0 → 0(Result is 1 only if BOTH bits are 1)
print(7 & 7)
print(4 & 5)
print(0 & 1)
print(1 & 0)
a=11
b=6
print(a & b)

#or  0 | 1 → 1 ,1 | 0 → 1,1 | 0 → 1(Result is 1 if ANY bit is 1)
a=5
b=6
print(3|4)
print(5|5)
print(a|b)

#exclusive or(XOR returns 1 only when the two bits are DIFFERENT If both bits are same, result is 0.)
print(5^3)
print(4^3)
print(a^b)

#left shift <<(remove the two values in left hand  and move the value in left hand side and add zeros to the right hamd side )
print(10<<2)
print(14<<2)
print(5<<1)

#Right shift
print(10>>2)
print(14>>2)
print(10<<1)

#not or complement (-n + 1)
print(~0)