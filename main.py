from flask import Flask, request, url_for, redirect, render_template, request
import sqlite3

# DATABASE HANDLING
# define connection
connection1 = sqlite3.connect('school.db')
cursor1 = connection1.cursor()

cursor1.execute("SELECT * FROM GRADES")
results = cursor1.fetchall()
print(results)
print(type(results))





app = Flask(__name__)

@app.route("/")
def initial():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/grades", methods=["POST", "GET"])
def grades():
    global results
    if request.method == "POST":
        input_name = request.form['nm']
        input_score = request.form['sc']
        insert_text = f"INSERT INTO GRADES VALUES ('{input_name}','{input_score}');"
        conn2 = sqlite3.connect('school.db')
        cursor2 = conn2.cursor()
        cursor2.execute(insert_text)
        conn2.commit()
        cursor2.execute("SELECT * FROM GRADES")
        results = cursor2.fetchall()
        return render_template("grades.html", input_name=input_name, input_score=input_score, datalist =results)
    else:
        return render_template("grades.html", datalist =results)



# needed in every flask app; this is the run function
if __name__ == "__main__":
    app.run(debug=True)
