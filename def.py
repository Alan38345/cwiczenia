def greet_user(user):
    print(f"hi there {user["name"]} you are {user["age"]}")
    print('welcome aboard')
print("start")
maciek = {
    "name" : "maciek",
    "age" : "28"

}
michal = {
    "name" : "michal",
    "age" : "24"
}
greet_user(maciek)
greet_user(michal)
print("finish")