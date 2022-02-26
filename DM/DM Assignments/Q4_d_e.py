'''
Q4. This program is to impliment 
    d) Demorgan's Laws
    e) Associative Laws
'''

p=[True,False]
q=[True,False]
print("Demorgan law\n----------\n")
print("p\tq\tpvq\t~(pvq)\t~pv~q\n")
for i in p:
    for j in q:
        print(i,"\t",j,"\t",(i|j),"\t",not(i|j),"\t",(not i) & (not j))
        
p=[True,False,True,False]
q=[True,True,False,False]
r=[False,True,False,True]
print("\nAssociative law\n----------\n")
print("p\tq\tr\tpv(qvr)\t(pvq)vr\n")
n=len(p)
for i in range(n):
    print(p[i],"\t",q[i],"\t",r[i],"\t",p[i]|(q[i]|r[i]),"\t",(p[i]|q[i])|r[i])