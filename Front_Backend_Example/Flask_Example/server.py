from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allows for access between local hosts 

students = {
    'Jon': 100,
    'Steven': 70,
    'Danny': 20,
    'Hoang': 5
}

#app.route determines what code runs with string at end of url. 
#Example: http://127.0.0.1:5000/get_student_data runs the code block below (returning list of students)
@app.route('/get_student_data', methods=['GET'])
def get_student_data():
    json_data = jsonify(students)
    return json_data

@app.route('/get_student_data/<string:name>', methods=['GET'])
def get_student(name):
    #Loop through each student
    #Looping through a dict gives us the names ('Jon', 'Steven', 'Danny', 'Hoang')
    for student in students:
        if student == name:
            #students[student] returns grade
            #{student: students[student]} returns a single key-value dict 
            return jsonify( {student: students[student]} )
    return jsonify({'error': 'Name not found'})

#Method to update server
#Post Requests come with data already
@app.route('/add_student', methods=['POST'])
def add_student():
    #parse data from json to python 
    data = request.json
    print(f"Data received: {data}")
    #create new student key-value
    new_name = data['name']
    new_grade = data['grade']
    students[new_name] = new_grade
    
    #201 = resource has been successfully created
    return jsonify(students), 201

if __name__ == '__main__':
    app.run(debug=True)
