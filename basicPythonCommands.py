#if statment
is_hot= False
if is_hot:
    print("Hot Day")
print("enjoy your day")
#loop
secret_number=7
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

#empji converter for loop
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

#emoji converter function
def emoji_converter(message)
    words = message.split(' ')
    print(words)
    emojis = {
        ":)": "😊",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output)
message = input(">")
emoji_converter(message)

#exceptions
try:
    age= int(input("age: "))
    imcome= 20000
    risk= income/age
    print(age)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
   print("error")
