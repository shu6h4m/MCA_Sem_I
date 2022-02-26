'''
Q4. This program is to impliment 
    a) Identity Laws
    b) Domination Laws
    c) Double Negation laws
'''
print("\nIdentity Laws\n-----------\n")
print("\n1.P^T=P")
print("P\t^\tT\tResult\n")
p=[True,True,False,False]
for i in p:
     print(i,"\t^\tTrue\t",(i&True))
print("\n2.PvF=P")
print("\nP\tv\tT\tResult\n")
for i in p:
     print(i,"\tv\tFalse\t",(i|False))
     
print("\nDomination Laws\n-----------\n")
print("\n1.PvT=T")
print("P\tv\tT\tResult\n")
for i in p:
    print(i,"\tv\tTrue\t",(i|True))
print("\n2.P^F=F")
print("\nP\tv\tT\tResult\n")
for i in p:
    print(i,"\t^\tFalse\t",(i&False))
    
print("\nDoubleNegation Laws\n-----------\n")
print("P\t~P\t~(~P)\n")
p=[True,False]
for i in p:
    if i==True:
        print(i,"\t",bool(0),"\t",bool(1))
    else:
        print(i,"\t",bool(1),"\t",bool(0))
        

   
	
    

    

    


#Submitted by Subham Sharma