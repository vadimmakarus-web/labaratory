users = [
    {
        "login": "Ivan",
        "password": "1234",
        "grades": [1,6,3,7,4]
    },
    {
        "login": "Stepan",
        "password": "4311",
        "grades": [4,6,3,9,10]
    },
    {
        "login": "Ivan",
        "password": "0876",
        "grades": [12,2,6,7,9]
    },
    {
        "login": "Ivan",
        "password": "9999",
        "grades": [11,5,4,6,7,9]
    },
]
corrent_user = None
login = input("ведіть логін: ")
pasword = input("ведіть пароль:")
for user in users:
    if user["login"] == login and user["password"] == pasword:
        corrent_user = user
        break
if corrent_user is None:
    print("Помилка")
else:
    print("Ваші оцінки:")
    for grade in user["grades"]:
        print(grade)