import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://pythonprojectfr-default-rtdb.firebaseio.com/",
})

ref= db.reference('students')

data = {
    "10000":
        {
            "Name": "Vedansh Kaushik",
            "Course": "B.Tech CSE",
            "Start Year": 2022,
            "total_attendance": 12,
            "Section": "A",
            "Year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "10001":
        {
            "Name": "Aastha Pandey",
            "Course": "B.Tech CSE",
            "Start Year": 2022,
            "total_attendance": 7,
            "Section": "A",
            "Year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "10002":
        {
            "Name": "Vedant Rai",
            "Course": "B.Tech CSE",
            "Start Year": 2022,
            "total_attendance": 7,
            "Section": "A",
            "Year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
