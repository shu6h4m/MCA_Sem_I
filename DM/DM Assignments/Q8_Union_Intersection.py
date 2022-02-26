'''
Q8. Program to find Union and Intersection of Two Sets
'''
55
p=set({})
q=set({})
n=int(input("Enter no. of elements in set A :"))
for i in range(n):
    ele=input()
    p.add(ele)
n=int(input("Enter no. of elements in set B :"))
for i in range(n):
    ele=input()
    q.add(ele)
print("Set A:",p)
print("Set B:",q)
print("Union of A and B is: ",p|q)
print("Intersection of A and B is: ",p&q)

#Submitted by Subham Sharma