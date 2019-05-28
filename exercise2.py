user = {'admin': True,
        'active':True,
        'name': "Mayank"}


if user['admin'] is True and user['active'] is True:
    print("ACTIVE - (ADMIN) "+ user['name'] )

elif user['admin'] is True:
    print("(ADMIN) "+ user['name'] )

elif user['active'] is True:
    print("ACTIVE "+ user['name'] )


