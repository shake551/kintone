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
    answers = answer_app.select().models(Answer)

    print(vars(answers[0]))

    return answers


# get_answers()

# 回答時間を取得する関数
def get_answer_times(question_id):
    select = "question_id = {0}".format(question_id)
    answer_times = answer_app.select(select)

    records = answer_times.records

    print(records)

    for record in records:
        print(record['created_at']['value'])

    return answer_times


get_answer_times(1)
