import pykintone

# kintone APIの設定（全処理共通）
subdomein = "ajrl2h58jbtu"

question_app_id = "1"
question_app_token = "1mdpHFfPZXm2BEDIqOeKtdgb9H4SJHpEvzKbTZE6"
question_app = pykintone.app(subdomein, question_app_id, question_app_token)

correct_answer_app_id = "2"
correct_answer_app_token = "XmnYoSkvWWetnQKjqzjBqRI7ZX4NBVeg5Y560vct"
correct_answer_app = pykintone.app(subdomein, correct_answer_app_id, correct_answer_app_token)
