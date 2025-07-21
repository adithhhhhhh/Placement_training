students = [
    {"name": "Raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "Vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "Pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "Rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "Virat", "dept": "ece", "marks": [16, 90, 43]}
]
for i in students:
    sum1=sum(i["marks"])
    per=sum1/3
    i['per']=per
    
des=["First","Second","Third","Fourth","Fifth"]
b=sorted(students, key=lambda x:x["per"],reverse=True)
index=1
for i in b:
    print("{}) {} is {} with {:.2f}%".format(index+1,i["name"],des[index-1],i["per"]))
    index=index+1