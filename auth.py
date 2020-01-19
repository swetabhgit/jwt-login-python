import jwt
def jwtEncode(payload):
  encoded_jwt = jwt.encode(payload, 'secret', algorithm='HS256')
  return encoded_jwt
def decode(token):
 decoded_value= jwt.decode(token,'secret', algorithms=['HS256'])
 return decoded_value
