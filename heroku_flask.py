from flask import Flask, render_template, request, url_for, redirect
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('predict'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        data1 = request.form.get('a')
        data2 = int(request.form.get('b'))
        data3 = int(request.form.get('c'))
        data4 = int(request.form.get('d'))
        data5 = int(request.form.get('e'))
        data6 = int(request.form.get('f'))
        data7 = int(request.form.get('g'))
        data8 = int(request.form.get('h'))
        data9 = int(request.form.get('i'))
        data10 = int(request.form.get('j'))
        data11 = int(request.form.get('k'))
        data12 = int(request.form.get('l'))
        data13 = int(request.form.get('m'))
        data14 = int(request.form.get('n'))
        data15 = int(request.form.get('o'))
        data16 = int(request.form.get('p'))
        arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8,
                       data9, data10, data11, data12, data13, data14, data15, data16]])
        print(arr)
        pred = model.predict(arr)
        if pred[0] == 1:
            val_html = "You are Diabetic. Visit your nearest hospital for suggestions."
        elif pred[0] == 0:
            val_html = "You are not diabetic. Keep it up!"
        else:
            val_html = "Interesting"
        return render_template('prediction.html', data=val_html)

    return render_template('home.html')


if __name__ == "__main__":
    app.run()
