n = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_freq = max(freq.values())

count = 0
for value in freq.values():
    if value == max_freq:
        count += 1

if count == 1:
    print("YES")
else:
    print("NO")