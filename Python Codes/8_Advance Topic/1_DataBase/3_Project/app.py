from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)
conn = mydb.cursor()

# Create database and table
conn.execute("CREATE DATABASE IF NOT EXISTS form")
conn.execute("USE form")

conn.execute("""
    CREATE TABLE IF NOT EXISTS emp (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        position VARCHAR(100),  -- Here you’re storing email as position
        salary FLOAT,
        DOB DATE,
        interests TEXT,
        gender VARCHAR(10),
        country VARCHAR(50),
        comments TEXT
    )
""")
mydb.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['email']  # still labeled "position" in DB
        salary = float(request.form['phno'])
        dob = request.form['dob']

        # Use getlist for checkboxes with the same name
        interests = request.form.getlist('interests')
        interests_str = ', '.join(interests)

        gender = request.form.get('gender', '')
        country = request.form['country']
        comments = request.form['comments']

        # Insert into database
        sql = """
            INSERT INTO emp (name, position, salary, DOB, interests, gender, country, comments)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, position, salary, dob, interests_str, gender, country, comments)
        conn.execute(sql, values)
        mydb.commit()

        return redirect('/success')

    return render_template('index.html')

@app.route('/success')
def success():
    return "✅ Data saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)
