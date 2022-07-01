import os
import random

from data_manager import Data_Manager


class Test_Manager:
    def __init__(self):
        self.data_manager = Data_Manager()

        self.question_set = []
        self.answer_set = []
        self.number_of_questions = None
        
        self.questions_to_be_asked = 10
        self.correct_answers = 0
        self.number_of_answers_to_be_shown = 16

    def init_test(self):
        self.get_new_question_set()
        self.set_number_of_questions()
        self.set_answer_set()

        self.display_welcome()

        # Test
        for q in range(1, self.questions_to_be_asked + 1):
            os.system('clear')
            self.question(q)
            input('\n<enter> continue...')

        self.display_mark()

    def get_new_question_set(self):
        self.question_set = self.data_manager.data.copy()

    def set_number_of_questions(self):
        self.number_of_questions = len(self.question_set)

    def set_answer_set(self):
        for question in self.question_set:
            for answer in question['answer']:
                if answer not in self.answer_set:
                    self.answer_set.append(answer)

    def get_new_question(self):
        return self.question_set.pop(random.randint(0, len(self.question_set) - 1))

    def get_answers_to_display(self, correct_answers):
        answers_to_display = correct_answers.copy()
        while len(answers_to_display) < self.number_of_answers_to_be_shown:
            answer = random.choice(self.answer_set)
            if answer not in answers_to_display:
                answers_to_display.append(answer)
        return answers_to_display
        
    def question(self, q):
        question = self.get_new_question()
        correct_answers = question['answer']
        answers_to_display = self.get_answers_to_display(correct_answers)
        random.shuffle(answers_to_display)
        correct_indexes = [str(answers_to_display.index(answer)) for answer in correct_answers]

        print('- {}. '.format(q) + question['question'] + '...\n')

        for i in range(len(answers_to_display)):
            print('\t{}.\t{}'.format(i, answers_to_display[i]))

        user_answers_indexes = self.get_user_answers()

        if ','.join(sorted(user_answers_indexes)) == ','.join(sorted(correct_indexes)):
            print('\n\tCORRECT')
            self.correct_answers += 1
        else:
            try:
                user_answers = [answers_to_display[int(index)] for index in user_answers_indexes]
            except ValueError:
                user_answers = 'Invalid'

            print('\n\tINCORRECT\n\nCorrect answers: {}\nYour answers: {}'.format(correct_answers, user_answers))

    @staticmethod
    def get_user_answers():
        user_answers = input('\nAnswers: ')
        return [answer for answer in user_answers.split(',')]

    def display_welcome(self):
        os.system('clear')
        print('''=== Welcome to the Buddhist Test ===

Number of questions: {}

Type your answers separated by colon (e.g: 1,2,3),
then hit <enter>.'''.format(self.questions_to_be_asked))
        input('\n<enter> to start...')
    
    def display_mark(self):
        os.system('clear')
        print('''=== Test completed ===

Your mark: {}/{}

Thanks.'''.format(self.correct_answers, self.questions_to_be_asked))
        input('\n<enter> to exit...')

