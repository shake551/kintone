import pykintone

# kintone APIの設定（全処理共通）
subdomein = "ajrl2h58jbtu"

question_app_id = "1"
question_app_token = "1mdpHFfPZXm2BEDIqOeKtdgb9H4SJHpEvzKbTZE6"
question_app = pykintone.app(subdomein, question_app_id, question_app_token)

correct_answer_app_id = "2"
correct_answer_app_token = "XmnYoSkvWWetnQKjqzjBqRI7ZX4NBVeg5Y560vct"
correct_answer_app = pykintone.app(subdomein, correct_answer_app_id, correct_answer_app_token)

choice_app_id = "3"
choice_app_token = "U8pmeJFoXbtZCWoVJf63JtjlOVUdBsK2B4sxnbWu"
choice_app = pykintone.app(subdomein, choice_app_id, choice_app_token)

answer_app_id = "4"
answer_app_token = "ZDir6XLriA5VAxRZ7BUhg1K0zNwIKUL2x8E8NvvP"
answer_app = pykintone.app(subdomein, answer_app_id, answer_app_token)
