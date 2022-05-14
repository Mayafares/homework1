Gradute_Student=["MAYA","GHADEER","NERMEN","NOOR","MAZEN ","HUSSEIN "]
name= input ("Welcome..... Enter your name ")
a_name=name.strip()
a_name=a_name.upper() 
if a_name in Gradute_Student:
    print("Bravo you are graduated")
else:
    print("sorry you are failed")    