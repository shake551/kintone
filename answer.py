from pykintone import model

from setting import answer_app


class Answer(model.kintoneModel):
    def __init__(self):
        super(Answer, self).__init__()
        self.id = ""
        self.content = ""
        self.user_id = ""
        self.question_id = ""
        self.created_at = ""
        self.updated_at = ""


def get_answers():
    questions = answer_app.select().models(Answer)

    print(vars(questions[0]))

    return questions


get_answers()
