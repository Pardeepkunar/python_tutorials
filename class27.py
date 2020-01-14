name = input("eneter name")
temp = ""
for deep in range(len(name)):
    if name[deep] not in temp:
        temp = temp + name[deep]
        print(f"{name[deep]} : {name.count(name[deep])}")
    