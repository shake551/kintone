from pykintone import model

from setting import correct_answer_app


class CorrectAnswer(model.kintoneModel):
    def __init__(self):
        super(CorrectAnswer, self).__init__()
        self.question_id = ""
        self.answer = ""


def get_correct_answers():
    correct_answers = correct_answer_app.select().models(CorrectAnswer)

    print(vars(correct_answers[0]))

    return correct_answers


get_correct_answers()
