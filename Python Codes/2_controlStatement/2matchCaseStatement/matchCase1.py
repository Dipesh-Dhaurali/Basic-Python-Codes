a=34

match a:

    case int():
        print("It is integer Number")

    case float():
        print("It is an float number")

    case str():
        print("It is an 1_String ")

    case list():
        print("It is an list")

    case tuple():
        print("It is an tuple")

    case _:
        print("Unknown type error !!!!")
