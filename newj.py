import json
with open("hi.json","r") as f:
    a = json.load(f)
    print(a)
with open("newfile.json","w") as new:
    json.dump(a,new)  


    

