import random

ANSWERS = (
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
)

# ask the user to enter a question
# note: what should be done with the question?
# note: when the user is done asking questions,
# they will type in 'done' to end the program
def ask_question():
    return input("Ask the almighty 8-ball a question ('done' to quit): ")


# generate a random answer from the list of answers
# answer = random.randint(0,len(ANSWERS)-1)
# answer = random.randrange(len(ANSWERS))
# random.shuffle(ANSWERS)
def magic_answer():
    return random.choice(ANSWERS)


# loop:
while True:

    question = ask_question()
    if question == "done":
        break
    else:
        print(question)

    # display it to the user
    print("** ", end='')
    print(magic_answer(), end='')
    print(" **")
