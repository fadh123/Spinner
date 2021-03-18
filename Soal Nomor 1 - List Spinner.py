#List Awal
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

#Function
result = list(map(list, zip(*m)))[::-1]
print(result)

#List Awal
n = [[1,2,3],
     [4,5,6],
     [7,8,9]]


#Function
#def counterClockwise : list(map(list, zip(*n)))[::-1  ]
#print(result)