import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb=boto3.resource('dynamodb')
teacher_table=dynamodb.Table('upb-classes')


#
#response=teacher_table.scan(
#    FilterExpression=Attr('semester').gt(4))
#items=response['Items']
#print(items)


#Query item
#response = teacher_table.query(
#    KeyConditionExpression=Key('subject').eq('SC-01')
#)
#items = response['Items']
#print(items)

#response = teacher_table.query(
#    KeyConditionExpression=Key('student').eq(111),
#    IndexName="student-subject-index"
    
#)
#items = response['Items']
#print(items)



#GEt item for pk
#response = teacher_table.get_item(
#    Key={
#        'student_id':'DS-45'
#    }
#)
#item = response['Item']
#print(item)


# Get item for PK+SK
#response = teacher_table.get_item(
#    Key={
#        'teacher_id':'AA-11',
#        'semester': 4
#    }
#)
#item = response['Item']
#print(item)