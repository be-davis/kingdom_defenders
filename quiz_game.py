import random
import numpy as np
import quiz_player
import json
import pandas as pd

q1 = {
    'question': ['1','2','3','4'],
    'answer': '5',
    'points': 1
}
q2 = {
    'question': ['2','4','6','8'],
    'answer': '10',
    'points': 1
}
q3 = {
    'question': ['100','91','83','76','70','65','61','58'],
    'answer': '56',
    'points':1
}
q4 = {
    'question': ['0','1','3','7','15','31'],
    'answer': '63',
    'points': 1
}
q5 = {
    'question': ['0','1','1','2','3','5','8','13'],
    'answer': '21',
    'points': 1
}
q6 = {
    'question': ['2','4','8','16','32','64'],
    'answer': '128',
    'points': 2
}
q7 = {
    'question': ['M','T','W','T','F','S'],
    'answer': 'S',
    'points': 2
}
q8 = {
    'question': ['A','D','G','J'],
    'answer': 'M',
    'points': 2
}
q9 = {
    'question': ['O','T','T','F','F','S','S','E','N','T'],
    'answer': 'E',
    'points': 3
}
q10 = {
    'question': ['80', '44', '26', '17'],
    'answer': '12.5',
    'points': 2
}
q11 = {
    'question': ['5','7','11','13','17','19'],
    'answer': '23',
    'points': 3
}
q12 = {
    'question': ["-/-/", "/--/", '/-/-', "-//-"],
    'answer': "-/-/",
    'points': 3
}
q13 = {
    'question': ["Q","S","E","F","T"],
    'answer': 'H',
    'points': 3
}
q14 = {
    'question': ["V", 'Y',"C", 'H'],
    'answer': 'N',
    'points': 3
}
q15 = {
    'question': ['0', '1', '32', '243', '1024', '3125'],
    'answer': '3125',
    'points': 3
}

question_list = [
    q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15
]

def run_game(player=quiz_player.QuizPlayer()):
    i = 0
    while i < len(question_list):
        
        sequence = question_list[i]['question']
        answer = question_list[i]['answer']
        points = question_list[i]['points']
        user_answer = input(f"What is the next element in this sequence below?\n{sequence}\nThe next in sequence is: ")
        if user_answer == answer:
            player.add_points(points)
            player.caputure_answer(question_list[i], user_answer, True)
            print('CORRECT')
        else:
            player.caputure_answer(question_list[i], user_answer, False)
            print('INCORRECT')
        
        i +=1
    with open('sequence_quiz_responses.txt','w') as data:  
      data.write(str(player.player_responses))
    print('===================================================')
    print('GAME IS OVER! YOU GOT ' + str(player.points) + ' POINTS')
    
run_game()

