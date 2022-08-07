from pykintone import model

from setting import app


class CorrectAnswer(model.kintoneModel):
    def __init__(self):
        super(CorrectAnswer, self).__init__()
        self.id = ""

