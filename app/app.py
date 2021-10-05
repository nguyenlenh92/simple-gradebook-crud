from flask import Flask, render_template, request, url_for, current_app
from werkzeug.utils import redirect
from models import db, studentModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/getdata")
def get_data():
    students = studentModel.query.all()
    return students

@app.route("/")
def index():
    students = get_data()
    return render_template("index.html", table=students)
    
@app.route("/add-entry", methods=["POST", "GET"])
def add_entry():
    if request.method == "POST":
        name = request.form["name"]
        student_id = request.form["id"]
        points = request.form["points"]
        new_student = studentModel(student_name=name, student_id=student_id, student_points=points)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template("add_form.html")


@app.route('/edit/<int:id>', methods=["POST", "GET"])
def edit_entry(id):
    student = studentModel.query.get_or_404(id)
    if request.method == "POST":
        student.student_name = request.form["name"]
        student.student_id = request.form["student_id"]
        student.student_points = request.form["points"]
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template("edit_form.html", student=student)
    

@app.route("/remove/<int:id>", methods=["POST", "GET"])
def remove_entry(id):
    student = studentModel.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index')) 

@app.route("/init")
def init_db():
    """Clear existing data and create new tables."""
    with current_app.open_resource("schema.sql") as f:
        for statement in f.read().decode("utf8").split(';'):
            if len(statement.strip()) > 0:
                db.session.execute(statement + ';')
        db.session.commit()
    
    return redirect(url_for('index'))