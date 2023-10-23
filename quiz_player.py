class QuizPlayer:
    def __init__(self,points=0):
        self.points=points
        self.player_responses = []
    def add_points(self,point_value):
        self.points += point_value
    def caputure_answer(self,question, player_answer, correct):
        player_response = {
            'question': question['question'],
            'player_answer': player_answer,
            'correct_answer': correct
        }
        self.player_responses.append(player_response)
