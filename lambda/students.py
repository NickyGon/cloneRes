import boto3

dynamodb = boto3.resource('dynamodb')
student_table = dynamodb.Table('upb-students')

student_data = [
    {
        "student_id": "JS-32",
        "identity_number": 342,
        "name": "Jonh Smith"
    },{
        "student_id": "LH-37",
        "identity_number": 343,
        "name": "Laura Hopkins"
    },{
        "student_id": "DS-56",
        "identity_number": 344,
        "name": "Damiel Simons"
    },{
        "student_id": "ML-94",
        "identity_number": 345,
        "name": "Monica Lindsay"
    },{
        "student_id": "ET-72",
        "identity_number": 346,
        "name": "Erick Torner"
    },{
        "student_id": "SC-82",
        "identity_number": 347,
        "name": "Susan Cox"
    },{
        "student_id": "DS-45",
        "identity_number": 348,
        "name": "Delia Sanchez"
    },{
        "student_id": "AL-34",
        "identity_number": 349,
        "name": "Angela Lamp"
    },{
        "student_id": "LH-42",
        "identity_number": 350,
        "name": "Luna Hills"
    },{
        "student_id": "HS-93",
        "identity_number": 351,
        "name": "Hector Sullivan"
    }
]
with student_table.batch_writer() as batch:
    for student in student_data:
        batch.put_item(
            Item=student
        )
print("Done!")