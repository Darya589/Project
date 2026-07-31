def check_password(s, chars = "$%!?@#"):
    if len(s) < 8:
        return False
    for i in s:
        if i in chars:
            return True
    return False
check_password("Hello") 




