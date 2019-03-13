#jadoo and dna transcription program (hackerarank)
lis=[]
name=input()
for j in name:
    if(j=="C"):
        lis.append("G")
    if(j=="G"):
        lis.append("C")
    if(j=="T"):
        lis.append("A")
    if(j=="A"):
        lis.append("U")
if(len(''.join(lis))==len(name)):
    print(''.join(lis))
else:
    print("Invalid Input")
   
