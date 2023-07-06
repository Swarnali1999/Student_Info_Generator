import sys
sys.path.append("resources")
from resources.dbconnection import GetConfig
db = GetConfig.db

class tblstudent(db.Model):
   __tablename__ = 'student_info'
   __table_args__ = {"schema":"public"}

   rollno = db.Column(db.Integer, primary_key=True)
   name=db.Column(db.String)
   class_name=db.Column(db.Integer)
   section=db.Column(db.String)