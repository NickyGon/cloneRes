import boto3

dynamodb = boto3.resource('dynamodb')
teacher_table = dynamodb.Table('upb-teachers')

teacher_data = [
    {
        "teacher_id": "AA-11",
        "teacher_name": "Lambo Rodriguez",
        "semester": 2,
        "class": "Optics"
    },{
        "teacher_id": "AA-11",
        "teacher_name": "Lambo Rodriguez",
        "semester": 4,
        "class": "Fluids"
    },{
        "teacher_id": "AA-11",
        "teacher_name": "Lambo Rodriguez",
        "semester": 7,
        "class": "Advanced Physics"
    },{
        "teacher_id": "BB-22",
        "teacher_name": "Michel Suarez",
        "semester": 1,
        "class": "Math"
    },{
        "teacher_id": "BB-22",
        "teacher_name": "Michel Suarez",
        "semester": 3,
        "class": "Math 2"
    },{
        "teacher_id": "BB-22",
        "teacher_name": "Michel Suarez",
        "semester": 6,
        "class": "Advanced Math"
    },{
        "teacher_id": "CC-33",
        "teacher_name": "Sophie Duran",
        "semester": 2,
        "class": "Tematical Linguistics"
    },{
        "teacher_id": "CC-33",
        "teacher_name": "Sophie Duran",
        "semester": 4,
        "class": "Adcanced Linguistics"
    },{
        "teacher_id": "CC-33",
        "teacher_name": "Sophie Duran",
        "semester": 6,
        "class": "Grammar for University Students"
    },{
        "teacher_id": "CC-33",
        "teacher_name": "Sophie Duran",
        "semester": 10,
        "class": "Spiral"
    },{
        "teacher_id": "AA-33",
        "teacher_name": "Sophie Duran",
        "semester": 1,
        "class": "Grammar for newbies"
    },
]

with teacher_table.batch_writer() as batch:
    for teacher in teacher_data:
        batch.put_item(
            Item=teacher
        )

print("Done!")