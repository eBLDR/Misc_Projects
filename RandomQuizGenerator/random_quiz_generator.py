# randomQuizGenerator.py - creates randomized quizzes along with the anser keys

import random

# the quiz data
USA_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
                'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
                'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
                'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
                'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
                'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
                'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
                'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
                'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
                'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate n quiz files
n = 5
for quizNum in range(1, n + 1):

    # initializing files
    quizFile = open('./USA_capitalsQuiz{}.txt'.format(quizNum), 'w')
    answerKeyFile = open('./USA_capitalsQuiz{}_answerKey.txt'.format(quizNum), 'w')

    # writing headers
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' '*20) + 'USA State Capitals Quiz (Form {})'.format(quizNum) + '\n\n')

    # shuffle order of states
    states = list(USA_capitals.keys())
    random.shuffle(states)

    # make a question for each state
    for questionNum in range(1, len(USA_capitals.items()) + 1):

        # set correct and wrong answers
        correctAnswer = USA_capitals[states[questionNum-1]]
        wrongAnswersList = list(USA_capitals.values())
        del wrongAnswersList[wrongAnswersList.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswersList, 3)

        # using list comprehension for the same
        # wrongAnswers = random.sample(
        #     [v for v in USA_capitals.values() if v != correctAnswer], 3)

        # getting set of answers
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # writing question and answer options to quiz file
        quizFile.write('{:2}. What is the capital of {}?\n'.format(questionNum, states[questionNum-1]))
        for i in range(4):
            quizFile.write('\t{}. {}'.format('ABCD'[i], answerOptions[i]) + '\n')

        quizFile.write('\n')  # nice new line

        # writing the answer to answer key file
        answerKeyFile.write('{:2}. {}\n'.format(questionNum, 'ABCD'[answerOptions.index(correctAnswer)]))

    # closing file's access
    quizFile.close()
    answerKeyFile.close()
