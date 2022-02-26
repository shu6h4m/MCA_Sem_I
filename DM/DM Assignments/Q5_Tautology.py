'''
Q5. Program to implement 
    a) Tautology
    b) Contradiction
    c) Contigency
'''
#a
p=[True,False]
q=[True,False]
print("Tautology\n---------------\n")
print("p\tq\tpvq\t(p->pvq)\n")
for i in p:
    for j in q:
        print(i,"\t",j,"\t",i|j,"\t",(not i)|(i|j))
        
#b
print("\n\nContradiction/Absurdity\n---------------\n")
print("p\tq\tp->q\t~(p->q)\t\tq^~(p->q)\n")
for i in p:
    for j in q:
        print(i,"\t",j,"\t",(not i)|j,"\t",not((not i)|j),"\t\t",j&(i&(not j)))
        
#c
print("\n\nContingency\n---------------\n")
print("p\tq\tpvq\n")
for i in p:
    for j in q:
        print(i,"\t",j,"\t",i|j)

        
        
#Submitted by Subham Sharma        