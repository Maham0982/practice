
'''is_hot= False
if is_hot:
    print("Hot Day")
print("enjoy your day")'''
'''secret_number=7
i=0
while i<3:
    number = int(input("guess"))
    if number== secret_number:
        print("correct")
        break
    else:
        print("try again")
        i = i+1
        continue
     '''
message=input(">")
words=message.split(' ')
print(words)
emojis = {
    ":)": "😊",
    ":(": "😞"
}
output=""
for word in words:
    output+= emojis.get(word,word) + " "
print(output)

#functions
def greet_user():
    print("Hi there!")
    print("welcome back")

print("start")
greet_user()
print("goodbye")

#parametrized
def greet_user2(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    print("goodbye")

print("start")
greet_user2("John", "Smith")
print("finished")

def square(number):
    print(number*number)
    return None

print(square(3))

