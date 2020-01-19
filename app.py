from flask import Flask,request

import json
import db
import auth

# import jwt
# encoded_jwt = jwt.encode({'username':'swetabh'}, 'secret', algorithm='HS256')
# print("jwt encoded value ", encoded_jwt)

# decoded_value= jwt.decode(encoded_jwt,'secret', algorithms=['HS256'])
# print(decoded_value)
# from .controller.ok import HelloFromController

# x = HelloFromController()
# print(x)
# import boto3

# # Get the service resource.
# dynamodb = boto3.resource('dynamodb')

# # Instantiate a table resource object without actually
# # creating a DynamoDB table. Note that the attributes of this table
# # are lazy-loaded: a request is not made nor are the attribute
# # values populated until the attributes
# # on the table resource are accessed or its load() method is called.
# table = dynamodb.Table('user')
# table.put_item(
#    Item={
#         'username': 'janedoe',
#         'password': '23',
#     }
# )

app = Flask(__name__)
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
     data = request.json
     username = data["username"]
     password = data["password"]
     dbData = db.getUsers(username)  
     dbUsername = dbData["username"]
    #  print(type(dbData))
     if dbUsername==username :
        return "user exists"  
      #print(type(data["username"]))
     else:
       db.putUser(username,password)
       return "user created"

@app.route('/token',methods=['POST'])
def getToken():
    if request.method == 'POST':
     data = request.json
     username = data["username"]
     password = data["password"]
     dbData = db.getUsers(username)  
     dbUsername = dbData["username"]
     dbPassword = dbData["password"]
     if dbUsername == username and dbPassword == password :
        return auth.jwtEncode({"username":dbUsername,"password":dbPassword})
     else:
       return "user not resgistered"
@app.route('/verify', methods=['GET'])
def verifyToken():
  accessTokenWithBearer = request.headers["Authorization"]
  #print(accessTokenWithBearer)
  accessToken = accessTokenWithBearer.split(" ")
  #print(str.encode(accessToken[1]))
  decodedValue = auth.decode(str.encode(accessToken[1]))
  #print(decodedValue," ----> decoded value")
  username = decodedValue["username"]
  password = decodedValue["password"]
  #print(username)
  item = db.getUsers(username)
  if item["username"] == username and item["password"] == password :
     return 'true'
  else:
    return 'false'     

if __name__== '__main__':
    app.run("localhost", 5001)
# import boto3
# # # configuring dnamoDB
# dynamodb= boto3.resource('dynamodb')
# table = dynamodb.Table('users')
# try:
#         table.put_item(
#             Item={
#                 'username':"amit",
#                 'password':"ssyo"
#             }
#         )
# except:
#     print("please try again error")
#     print('put user')