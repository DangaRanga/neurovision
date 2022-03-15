import jwt
from ...api import app

# Modify File to Structure How We Use JWT - TEMP File 

def decodetoken(token):
    try:
        jwt_payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jwt_payload
    except jwt.ExpiredSignatureError: 
        return 'EXPIRED'
    except jwt.InvalidTokenError: 
        return 'INVALID'

def checktoken(user, jwt_token):
    result = decodetoken(jwt_token)
    if result == 'EXPIRED' or result == 'INVALID':
        return 'Invalid token. Please login in again'
    elif type(result) == dict:
        username = result.get('username')
        if username == user.username:
            return 'OK'
        else:
            return 'Invalid token. Please login in again'
    else:
        return 'Invalid token. Please login in again'

# def tvalidate():
#     token = request.headers.get('Authorization')
#     if token == None:
#         return jsonify({'error_message': 'Invalid Credentials'})
#     else:
#         token = token.split()[1]
#         value = checktoken(current_user, token)
#         if value != 'OK': 
#             return jsonify({'error_message': value })
#         return 'OK'