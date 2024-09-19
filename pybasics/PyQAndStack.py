stck = []

for i in range(10):
    stck.append(i) # insert == push
    print(stck)

print(stck[-1]) # top

for i in range(10):
    print(stck.pop()) # remove


print("======= queue======")
q = []
for i in range(10):
    q.append(i) # insert == push
    print(q)
print(q[0]) # front/peek

for i in range(10):
    print(q.pop(0)) # remove

