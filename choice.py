from pykintone import model

from setting import choice_app


class Choice(model.kintoneModel):
    def __init__(self):
        super(Choice, self).__init__()
        self.id = ""
        self.question_id = ""
        self.content = ""


def get_choices():
    choices = choice_app.select().models(Choice)

    print(vars(choices[0]))

    return choices


def get_question_choices(question_id):
    question_choices = choice_app.select("question_id = {0}".format(question_id)).models(Choice)

    print(vars(question_choices[0]))

    return question_choices


get_question_choices(1)
