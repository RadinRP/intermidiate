vots =["Ali","Ali","Ali","Reza","Amir"]
ali = 0
reza = 0
amir = 0
last_vots = [vot.lower() for vot in vots]
for vote in last_vots:
    if (vote == "ali"):
        ali += 1
    elif (vote == "reza"):
        reza += 1
    elif (vote == "amir"):
        amir += 1
print("Amir votes : " ,amir,"ali votes :" , ali,"reza votes : " ,reza)