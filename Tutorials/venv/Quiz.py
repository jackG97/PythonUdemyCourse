from Quiz_Question import Question

question_prompt = [
    "What color are Apples?\n (a)Red \n (b)Green \n (c)Blue \n (d)Voilet\n",
    "What color are Bananas?\n (a)Teal \n (b)Yellow \n (c)Magenta \n (d)Orange\n",
    "What color are Strawberries?\n (a)Red\n (b)Green\n (c)Blue\n (d) Purple\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " +str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)