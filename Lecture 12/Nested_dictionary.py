students={
    "student1":{
        "Name":"Alice",
        "Age":20,
        "Grade":"A"
    },
    "Student2":{
        "Name":"Bob",
        "Age":22,
        "Grade":"B"
    },
    "Student3":{
        "Name":"Charlie",
        "Age":23,
        "Grade":"A+"
    }
}
for s_key, s_info in students.items():
    print("Information of ",s_key)
    for key,value in s_info.items():
        print(f"{key} : {value}")
