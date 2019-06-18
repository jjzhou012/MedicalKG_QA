from flask import Flask, render_template, url_for, request
from QA.chatbot_graph import ChatBotGraph

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# 医药助手
@app.route('/medical', methods=['GET', 'POST'])
def medical_bot():
    question = ''
    answer = ''
    if request.method == 'POST':
        print(request.form)
        print(request.form['question'])
        question = request.form['question']

        answer = handler.chat_main(question)
        print(answer)
    return render_template('medical_bot.html', name=[answer, question])


# 就医助手
@app.route('/doctor', methods=['GET', 'POST'])
def doctor_bot():
    question = ''
    answer = ''
    return render_template('doctor_bot.html', name=[answer, question])


@app.route('/layout', methods=['GET', 'POST'])
def about():
    return render_template('layout.html')


if __name__ == '__main__':
    handler = ChatBotGraph()
    app.run(debug=True)
