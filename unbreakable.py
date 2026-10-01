def get_age(text):
    try:
        return int(text)
    except ValueError:
        return "Invalid age"


print(get_age("25"))
print(get_age("abc"))