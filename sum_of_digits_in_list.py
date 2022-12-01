# list = [123,456,789,'apple']
#
# print("The original list is " + str(list))
# res=[]
# for i in list:
#     sum=0
#     for j in str(i):
#         sum+=int(j)
#     res.append(sum)
# print("sum is : " + str(res))
# a='appl3' #finding element in list
# print(list)
# if a in list:
#     print(a)

# tpl=(1,2,[3,4,5])
# tpl[2].append(9)
# print(tpl)
# tpl[2].insert(2,6)
# print(tpl)
# tpl[2].remove(9)
# print(tpl)
# tpl[2].clear()
# print(tpl)
#
# tpl1=(1,2,3,4)
# print(type(tpl1))


std={"name":"amol","study":"data engg","age":26}
print(std)

#dic11 = dict(name:"amol", age =30)
#print(dic11)

#create dict using dict keyword use '=' for assignment
sy1= dict(name='pst', age=30, phno=84374837, address='Aurangabad')
print(sy1)
print(type(sy1))
x=std["name"]
print(x)

std["name"]
for i in std:
    print(i)

for d1 in std.values():
    print(d1)

for k,v in std.items():
    print(k,v)

if 'name' in std:
    print("yes, 'key' is one of the keys")

#finding the length of dictionary
print(len(std))

#adding element in the dictionary
std["mob"]=12345
print(std)

#removing elements from dictionary
std.pop("mob")
print(std)

#removing elements from dictionary without providing key
std.popitem()
print(std)

# std.clear()
# print(std)

#creating the copy of dictionary
std_copy = dict(std)
print(std_copy)

#dictionary inside a dictionary / nested dictionary
dic = {1:'geeks',2:'for',3:{'A':'welcome','B':'to','C':'geeks'}}
print(dic)



#SETS

s1 = {1,2,3,4,5,6}
print(s1)
print(type(s1))

s2= {2,3,4,4,3,5}
print(s2)

print(s1 | s2)
print(s1 & s2)

#removing elements from set
s1.remove(2)
print(s1)
s1.discard('amol')
print(s1)

s = {1,2,3,3,4,5}
print(s)

#converting list to set
l = [1,1,1,2,2,3,4,5]
print(l)
l1 = list(set(l))
print(l1)

#or,and operation on list
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3={6,5,8,7,2}
print(set1 | set2) #similar like union operation
print(set1 & set2) #gives only matching values

#update set values
print(set3)
set3.update([4,3])
print(set3)

#combination of string,float,int in set
#adding and removing elements
set4 = {1,2,2.3,'string'}
print(set4)
set4.add('next string')
print(set4)
set4.discard('string')
print(set4)
set4.discard('string amol')
print(set4)

