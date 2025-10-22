from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import matplotlib.pyplot as plt
import io, base64

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session

# -----------------------
# Dummy login credentials
# -----------------------
USERNAME = "admin"
PASSWORD = "1234"

# -----------------------
# Routes
# -----------------------

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error="Invalid username or password!")


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('home'))

    # Load CSV data
    df = pd.read_csv('data/customers.csv')

    # Group by credit rate
    grouped = df.groupby('credit_rate').size()

    # Generate chart
    img = io.BytesIO()
    grouped.plot(kind='bar')
    plt.title("Company Count by Credit Rate")
    plt.xlabel("Credit Rate")
    plt.ylabel("Number of Companies")
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode()

    return render_template('dashboard.html', username=session['username'], chart=chart_url)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

