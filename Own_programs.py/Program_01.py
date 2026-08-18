class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def greeting(name):
        print(f"hello how are {name.name}")

    def response(response):
        print(f"I am good how are you {response.name}")

p1 = person("Ayush", 20)

print(p1.greeting())
print(p1.response())


dataset = {
    "Hello" : "Hello, How are you?",
    "What are you doing": "Nothing much just chatting with you",
    "How are you doing" : "Good, How are you doing",
    "How to cure fever" : "To cure fever there are several things which you should keep in mind:\n 1. Stay Hydrated \n 2. Take Rest\n 3. Check your body temperature regularly\n 4. Seek Doctor if you are having a heavy fever",
    "Who is the president of the United States of America" : "The Current President of United States of America is Donald J. Trump",
    "How are you so cool": "Ahh i think you are getting too personal but for your kind information i tell you that i am simply an Artificial intelligence who just give you the answers based on your questions, I don't have any feeling or emotions."
}

while True:
    prompt = input("Enter your prompt: ")
    if prompt.casefold() == "hello":
        print(f"{dataset['Hello']}")
    elif prompt.casefold() == "what are you doing":
        print(f"{dataset['What are you doing']}")
    elif prompt.casefold() == "how are you doing":
        print(f"{dataset['How are you doing']}")
    elif prompt.casefold() == "how to cure fever":
        print(f"{dataset['How to cure fever']}")
    elif prompt.casefold() == "who is the president of the united states of america":
        print(f"{dataset['Who is the president of the United States of America']}")
    elif prompt.casefold() == "how are you so cool":
        print(f"{dataset['How are you so cool']}")
    else:
        print("There is something wrong")

howmany = int(input("Enter how many rows you want: "))

i = 0 
while i <= howmany:
    print(f"{i * "*"}")
    i = i + 1

