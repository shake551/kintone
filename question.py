from pykintone import model

from setting import question_app


class Question(model.kintoneModel):
    def __init__(self):
        super(Question, self).__init__()
        self.id = ""
        self.question = ""
        self.type = ""
        self.publish_date = ""


def get_questions():
    questions = question_app.select().models(Question)

    print(vars(questions[0]))

    return questions


get_questions()
