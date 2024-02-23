function getStudents(){
    //fetch w/o parameters automatically does a get request
    fetch('http://127.0.0.1:5000/get_student_data')
        .then(response => {
            return response.json();
        }).then(data => {
            console.log("GET REQUEST COMPLETE:", data)
        })
}

function postStudent() {
    //Grab data from html page
    student_name = document.getElementById('student_name').value;
    grade = parseInt(document.getElementById('grade').value);
   
    //Store into new dict/hashmap object
    data = {
        "name": student_name,
        "grade": grade
    }

    fetch('http://127.0.0.1:5000/add_student', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        console.log('New student added:', data);
    });
}