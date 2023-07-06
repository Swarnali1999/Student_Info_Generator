from flask import request, jsonify, make_response
from flask_restful import Resource
from resources.dbconnection import GetConfig
from resources.dbmodel.tbl_student import tblstudent

obj = GetConfig()
db = obj.db

class insert_student_info(Resource):
    def post(self):
        data = request.form
        if data:
            try:
                rollno = data['rollno']
                name= data['name']
                get_roll_no = db.session.query(tblstudent).filter(tblstudent.rollno==rollno).first()

                if get_roll_no:
                    return make_response(jsonify({'msg': "roll_no {}, whose name is {} is already present".format(rollno,name)}),400)
                else:
                    db.session.begin()
                    add_student=tblstudent(
                        rollno = data['rollno'],
                        name = data['name'],
                        class_name = data['class_name'],
                        section = data['section']
                    )
                    db.session.add(add_student)
                    db.session.commit()
                    return make_response(jsonify({'message': "Student added successfully"}),200)

            except Exception as e:
                return make_response(jsonify({'msg': str(e)}), 400)


class get_student_info(Resource):    
    def post(self):
        data = request.form
        if data:
            try:
                rollno = data['rollno']
                result = db.session.query(tblstudent).filter(tblstudent.rollno==rollno).all()

                results = []
                for j in result:
                    data = {
                        'rollno' : j.rollno,
                        'name' : j.name,
                        'class_name' : j.class_name,
                        'section' : j.section
                    }
                    results.append(data)

                if not result:
                    return make_response(jsonify({"msg": "No Record Found for rollno: {}".format(rollno)}),200) 
                else:
                    return make_response(jsonify({"message": results}),200)  

            except Exception as e:
                return make_response(jsonify({'msg': str(e)}), 400)        

class update_student_info(Resource):
    def put(self):
        data=request.form
        if data:
            try:
                rollno=data['rollno'] 
                result = db.session.query(tblstudent).filter(tblstudent.rollno==rollno).all()
                
                if result:                   
                    db.session.begin()
                    db.session.query(tblstudent).filter(tblstudent.rollno==rollno).update({
                        'rollno' : data['rollno'],
                        'name' : data['name'],
                        'class_name' : data['class_name'],
                        'section' : data['section']
                    })
                    db.session.commit()
                    db.session.close()                    
                    return make_response(jsonify({'message':"Student info updated successfully."}),200)
                else:
                    return make_response(jsonify({"msg": "No Record Found for rollno: {}".format(rollno)}),200) 

            except Exception as e:
                return make_response(jsonify({'msg': str(e)}),400)       

class delete_student_info(Resource):    
    def delete(self):
        data = request.form 
        if data:
            try:
                rollno = data['rollno']
                result = db.session.query(tblstudent).filter(tblstudent.rollno==rollno).first()

                if result:  
                    db.session.begin()
                    db.session.delete(result)
                    db.session.commit()
                    return make_response(jsonify({'message': "Student info deleted successfully"}),200)
                else:
                    return make_response(jsonify({'msg': "No Record Found for rollno: {}".format(rollno)}), 400)
            except Exception as e:
                return make_response(jsonify({'msg': str(e)}), 400)              