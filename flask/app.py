from flask import Flask, render_template, request
import pickle
import os
import numpy as np

path_model = os.path.join(os.getcwd(), 'src', 'model')

def func(_):
    if _.argmax() == 0 and _.sum() == 0:
        ClassName = 'Ничего из перечисленных'
    elif _.argmax() == 0:
        ClassName = 'Оскорбление (INSULT)'
    elif _.argmax() == 1:
        ClassName = 'Нормальный комментарий'
    elif _.argmax() == 2:
        ClassName = 'Непристойность (OBSCENITY)'
    elif _.argmax() == 3:
        ClassName = 'Угроза (THREAT)'
    else:
        ClassName = 'Ошибка'
    return ClassName


model = pickle.load(open(path_model, 'rb'))  # load model
app = Flask(__name__)  # Flask application


# ClassName = '...'
@app.route('/', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        a = request.form['comment']
        a = model.predict([a])
        ClassNameNew = func(a)

        return render_template("index.html", ClassName=ClassNameNew)
    return render_template("index.html", ClassName='...')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')