'''
Q6. Program to Implement
    a) Modus ponens
    b) Modus tollens
'''
#a
p=[True,False]
q=[True,False]
print("\n_______________Modus Ponens_______________")
print("\nTruth table for ((p->q)^p)->q")
print("p\tq\tp->q\t(p->q)^p","  ","((p->q)^p)->q\n")
for i in p:
    for j in q:
        r=((not i)|j)&i
        print(i,"\t",j,"\t",(not i)|j,"\t",r,"\t\t",(not r)|j)
        
#b
print("\n________________Modus Tollens______________")
print("\nTruth table for (~q^(p->q))->~p\n")
print("p\tq\tp->q\t~q^(p->q)\t(~q^(p->q))->~p\n")
for i in p:
    for j in q:
        m=(not i)|j
        n=(not j)&m
        o=(not n)|(not i)
        print(i,"\t",j,"\t",m,"\t",n,"\t\t",o)



#Submitted by Subham Sharma