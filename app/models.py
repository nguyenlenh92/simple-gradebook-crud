from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class studentModel(db.Model):
    __tablename__ = "student_table"
    
    id = db.Column(db.Integer, primary_key = True)
    student_name = db.Column(db.String(), nullable=False)
    student_id = db.Column(db.String(), nullable=False)
    student_points = db.Column(db.Integer, nullable=True)
 
    def __init__(self, student_name, student_id, student_points):
        self.student_name = student_name
        self.student_id = student_id
        self.student_points = student_points
    
    def __repr__(self):
        return f"{self.id}:{self.student_name}:{self.student_id}:{self.student_points}"