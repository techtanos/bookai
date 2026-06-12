@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('invoices.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        conn.close()
        if check_password_hash(user[2], password):
            login_user(User(user[0], user[1]))
            return redirect('/app')
        else:
            return "Wrong email or password. <a href='/login'>try again</a>"
    return render_template('login.html')
           
