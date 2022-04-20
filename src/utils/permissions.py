
def get_permissions(user_type):
    if (user_type == 'c'): # Client
        return [1000]
    elif (user_type == 'u'): # User
        return [1000, 2000]
    elif (user_type == 'a'): # Admin
        return [1000, 2000, 3000]
    