def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list


result = todo_list("check the mail")
print("{0}".format(result))
result = todo_list("begin orbital transfer")
print("{0}".format(result))