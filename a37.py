student_data ={
    "idi1":{"name":"sara", "class":"v","subject_integration":" english , math , scince"},
    "idi2":{"name":"sara", "class":"v","subject_integration":" english , math , scince"},
    "idi3":{"name":"sara", "class":"v","subject_integration":" english , math , scince"},
    "idi4":{"name":"sara", "class":"v","subject_integration":" english , math , scince"},
}

result ={}
seen_key =[]

for student_id, details in student_data.item():
    unique_key = (details["name"],details["class"],details["subject_interation"])

    if unique_key not in seen_key:
        seen_key.append(unique_key)
        result[student_id] = details

    for k,v in result.item():
        print(k, ":" ,v)