from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Necessary for session management

# Dummy login credentials
users = {"admin": "password123"}

# Store machine data in memory (for simplicity)
machine_data = []

# Login route


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# Dashboard route


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', machines=machine_data)

# Route to handle adding machine data


@app.route('/add_machine', methods=['POST'])
def add_machine():
    if 'username' in session:
        # Retrieve form data from the request
        machine_name = request.form.get('machineName')
        machine_type = request.form.get('machineType')
        description = request.form.get('description')
        temperature = float(request.form.get('temperature'))
        damage = float(request.form.get('damage'))

        # Calculate quality
        quality = "Excellent" if damage >= 80 else "Action Required" if damage >= 50 else "Quick Action Required"

        # Add machine data to the list
        machine_data.append({
            "name": machine_name,
            "type": machine_type,
            "description": description,
            "temperature": temperature,
            "damage": damage,
            "quality": quality
        })
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# Logout route


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
