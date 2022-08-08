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


class AnswerPost(model.kintoneModel):
    def __init__(self):
        super(AnswerPost, self).__init__()
        self.content = ""
        self.user_id = ""
        self.question_id = ""


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


def post_answer(question_id, content, user_id):
    answer = AnswerPost()

    answer.question_id = question_id
    answer.content = content
    answer.user_id = user_id

    created_id = answer_app.create(answer).record_id

    print(vars(answer))
    print(created_id)


post_answer(1, 1, 1)
