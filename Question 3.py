import json
question={}
mark=0
user_name=input("Enter your name: ")
with open ("file_of_question.json","r") as p :
    question=json.load(p)
print("Welcome" + " "+user_name+ " " + "Answer This Question below with T or F ")
for x in question.keys():
    print(x)
    i=input("The Answer: ")
    i=i.strip()
    if i ==question[x]:
        mark=mark + 1
        print("True")
    else:
        print("Fulse")
print("well done  your mark is : " , mark )        
with open("user.json","w") as o:
    user_name=user_name + " " + str(mark)
    u=json.dump(user_name,o) 
    