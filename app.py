from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy credentials
USER_CREDENTIALS = {'admin': 'password123'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USER_CREDENTIALS.get(username) == password:
            session['username'] = username
            return redirect(url_for('food_form'))
        else:
            return "Invalid Credentials! Try again."
    return render_template('login.html')

@app.route('/food', methods=['GET', 'POST'])
def food_form():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        cuisine = request.form['cuisine']
        mealtime = request.form['mealtime']
        feedback = request.form['feedback']
        return render_template('thank_you.html', cuisine=cuisine, mealtime=mealtime, feedback=feedback)
    return render_template('food_form.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
