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


#get_questions()

def get_question_text(id):
    select = "id = {0}".format(id)
    
    question_text = question_app.select(select)

    records = question_text.records

    #print(records)

    for record in records:
        print(record['question']['value'])

    #print(question_text)

    return question_text

get_question_text(1)
