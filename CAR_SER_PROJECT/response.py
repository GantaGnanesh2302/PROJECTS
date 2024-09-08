l=[]
with open("C:/Users/GNANESH GANTA/Downloads/personal.csv","r") as f:
    for i in f:
        l.append(i)
l[1]=l[1].split(",")
print(l[1])
