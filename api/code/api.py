from flask_restful import Api
from resources.dbconnection import GetConfig
from resources.config import Config
from resources.generate_student_name import insert_student_info, get_student_info, delete_student_info, update_student_info

app = GetConfig.app
app.config.from_object(Config)
api = Api(app)


api.add_resource(insert_student_info, '/api/insert_student_info')
api.add_resource(get_student_info, '/api/get_student_info')
api.add_resource(update_student_info, '/api/update_student_info')
api.add_resource(delete_student_info, '/api/delete_student_info')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)