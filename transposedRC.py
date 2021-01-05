# test = [[x for x in range(6)] for i in range(3)]
# print(test)

matrix = [[1,2,3,4,5],
[6,7,8,9,8],
[1,2,3,4,5],
[6,5,4,3,2]
]

transposed = []
for i in range(5):
    transposed.append([row[i] for row in matrix])

print(transposed) 