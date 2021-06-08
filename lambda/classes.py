import boto3

dynamodb = boto3.resource('dynamodb')
classes_table = dynamodb.Table('upb-classes')

classes_data = [
    {
        "subject": "SC-01",
        "student": 111,
        "grading": 100
    },{
        "subject": "SC-01",
        "student": 112,
        "grading": 90
    },{
        "subject": "SC-01",
        "student": 221,
        "grading": 60
    },{
        "subject": "SC-01",
        "student": 223,
        "grading": 50
    },{
        "subject": "SC-01",
        "student": 224,
        "grading": 80
    },{
        "subject": "SC-01",
        "student": 225,
        "grading": 85
    },{
        "subject": "SC-01",
        "student": 226,
        "grading": 89
    },{
        "subject": "LM-06",
        "student": 111,
        "grading": 95
    },{
        "subject": "TP-05",
        "student": 111,
        "grading": 90
    },{
        "subject": "TP-05",
        "student": 112,
        "grading": 100
    },{
        "subject": "TP-05",
        "student": 113,
        "grading": 88
    },{
        "subject": "TP-05",
        "student": 114,
        "grading": 90
    },
]


with classes_table.batch_writer() as batch:
    for class_item in classes_data:
        batch.put_item(
            Item=class_item
        )
print("All good")