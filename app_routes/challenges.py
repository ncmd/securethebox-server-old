import subprocess
from subprocess import check_output
import requests
import json
from flask_restful import reqparse,Resource

academy_parser = reqparse.RequestParser()
academy_parser.add_argument('courseId', help='{error_msg}')
academy_parser.add_argument('courseHandle', help='{error_msg}')
academy_parser.add_argument('data', help='{error_msg}')

# categories, courses = main()
# print(courses,categories)


# Create Course
class ApiAcademyCourseCreate(Resource):
    def post(self):
        try:
            return "created course", 201 , {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "POST"} 
        except:
            return 404

# Get All Courses
class ApiAcademyCourses(Resource):
    def get(self):
        try:
            return "all courses", 201 ,  {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "GET"} 
        except:
            return 404

# Get Single Course information
class ApiAcademyCourse(Resource):
    def get(self):
        args = academy_parser.parse_args()
        try:
            for i in courses:
                print(i["id"],args['courseId'])
                if i["id"] == args['courseId']:
                    return i, 201 ,  {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "GET"} 
        except:
            return 404

# Save Course
class ApiAcademyCourseSave(Resource):
    def post(self):
        args = academy_parser.parse_args()
        data = args['data']
        course = None
        try:
            for i in courses:
                if i["id"] == data["id"]:
                    course = data
                    return course, 201 ,  {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "POST"} 
                return course, 201 ,  {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "POST"} 
            if course is not None:
                course = data
                courses.append(course)
            return course, 201 ,  {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "POST"} 
        except:
            return 404

# Update Course Progress
class ApiAcademyCourseUpdate(Resource):
    def post(self):
        args = academy_parser.parse_args()
        data = args["data"]
        try:
            for i in courses:
                if i["id"] == data["id"]:
                    return courses.update(data), 201 ,  {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "POST"} 
                else:
                    return i
        except:
            return 404

# Get all Course Categories
class ApiAcademyCategories(Resource):
    def get(self):
        try:
            return categories, 201 , {'Access-Control-Allow-Origin': '*', "Access-Control-Allow-Methods": "GET"} 
        except:
            return 404