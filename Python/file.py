
# fin  = open("/Users/aroslavbezukladnikov/Desktop/GeekBrains/Буткэмп/Development/Python/input.txt")
# fout = open("/Users/aroslavbezukladnikov/Desktop/GeekBrains/Буткэмп/Development/Python/output.txt","w")
 
# a, b = map(int, fin.readline().split())
# fout.write(str(a+b))
 
# fin.close()
# fout.close()


# fin  = open("/Users/aroslavbezukladnikov/Desktop/GeekBrains/Буткэмп/Development/Python/input.txt")
# fout = open("/Users/aroslavbezukladnikov/Desktop/GeekBrains/Буткэмп/Development/Python/output.txt","w")
 
# a = list(map(int, fin.readline().split()))

# fout.write(str(a[0]+a[1]))

# fin.close()
# fout.close()


# s = input().split()

# a = int(s[0])
# b = int(s[1])

# print(a+b)

# n = int(input())

# temp = abs(n)
# sum = 0

# for el in range(temp+1):
#     sum = sum + el

# if (n>0):
#     print(sum)
# else:  
#     print((sum-1)*(-1))   



# n = abs(int(input()))

# if (n<10): print(n**2)
# else:
#     print((n//10)*((n//10)+1)*100+25)

# n = int(input())

# print(n*100+90+(9-n))

# N = int(input())

# array = list(map(int,input().split()))

# even = []
# odd = []


# for el in array:
#     if (el%2==0):
#         even.append(el)
#     else:
#         odd.append(el)    

# for index in range(len(odd)):
#     if(index ==len(odd)-1):
#         print(odd[index], end="")
#     else:
#           print(odd[index], end=" ")   

 
# print()

# for index in range(len(even)):
#     if(index ==len(even)-1):
#         print(even[index], end="")
#     else:
#           print(even[index], end=" ")     

# print()

# if (len(even)>=len(odd)): print("YES")
# else:
#     print("NO")

# ЗАДАЧА №7

# a = list(map(int, input().split()))

# max_number = max(a)

# print(max_number)

# ЗАДАЧА №8	

# a, b, c = map(int, input().split())

# if (a*b==c):
#     print("YES")
# else:
#     print("NO") 


# ЗАДАЧА №9

N = int(input())

array = list(map(int, input().split()))
sum = 0
for el in array:
    if (el >0): sum +=el

maxN = array[0]
indexMax=0
indexMin=0
minN = array[0]

for index in range(len(array)):
    if(maxN < array[index]):
        maxN = array[index]
        indexMax = index

    if(minN>array[index]):
        minN = array[index]
        indexMin = index

first = indexMin
second = indexMax

if (indexMin>indexMax):
    first= indexMax
    second = indexMin
   

P = 1
while(first+1<second):
    P *=array[first+1]
    first+=1



print(sum, P)




















