phone = input("phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + "!"
print(output)