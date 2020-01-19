import boto3
from botocore.exceptions import ClientError
# configuring dnamoDB
dynamodb= boto3.resource('dynamodb')
# choosing the table
table = dynamodb.Table('users')
#getting all users
def getUsers(username):
 try:
  response = table.get_item(
         Key={
             "username":username
         } 
     )
    
  item = response['Item']
  return item
 except NameError:
   return {"username":"invalid username"}
 except KeyError:
    return {"username":"invalid username"}  
     
# write user
def putUser(username, password):
    try:
        table.put_item(
            Item={
                'username':username,
                'password':password
            }
        )
    except:
        print("please try again error")
    print('put user')

# 