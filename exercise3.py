users = [{'admin': True,'active':True,'name': "Mayank"},
        {'admin': True,'active':False,'name': "Sakshi"},
        {'admin':False,'active':False,'name': "Inu"}]

line_num = 1

for user in users:
    if user['admin'] is True and user['active'] is True:
        print(str(line_num) + " ACTIVE - (ADMIN) "+ user['name'] )

    elif user['admin'] is True:
        print(str(line_num) + " (ADMIN) "+ user['name'] )

    elif user['active'] is True:
        print(str(line_num) + " ACTIVE "+ user['name'] )

    else:
        print(str(line_num) +" "+ user['name'])

    line_num += 1
