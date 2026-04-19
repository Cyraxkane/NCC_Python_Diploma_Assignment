from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = "crud_secret_key"
DB_FILE = "user_data.txt"

def load_data():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as file:
            data = json.load(file)
            # Ensure keys are integers for consistency
            return {int(k): v for k, v in data.items()}
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

#READ 
@app.route('/')
def index():
    users = load_data()
    return render_template('index.html', users=users)

#CREATE
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        users = load_data()
        
        # Logic to generate next ID
        new_id = max(users.keys()) + 1 if users else 1
        
        users[new_id] = {
            "r_username": request.form['username'],
            "r_password": request.form['password'], # Store as raw for this assignment
            "amount": int(request.form['amount'])
        }
        
        save_data(users)
        flash(f"User {request.form['username']} created successfully!")
        return redirect(url_for('index'))
    
    return render_template('create.html')

#UPDATE
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    users = load_data()
    user = users.get(user_id)
    
    if not user:
        flash("User not found!")
        return redirect(url_for('index'))

    if request.method == 'POST':
        user['r_username'] = request.form['username']
        user['r_password'] = request.form['password']
        user['amount'] = int(request.form['amount'])
        
        users[user_id] = user
        save_data(users)
        flash("User updated successfully!")
        return redirect(url_for('index'))
    
    return render_template('edit.html', user=user, user_id=user_id)

#DELETE
@app.route('/delete/<int:user_id>')
def delete(user_id):
    users = load_data()
    if user_id in users:
        deleted_name = users[user_id]['r_username']
        del users[user_id]
        save_data(users)
        flash(f"User {deleted_name} deleted!")
    else:
        flash("User not found!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)