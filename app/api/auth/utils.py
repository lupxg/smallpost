import jwt
from datetime import datetime, timedelta 
from jwt import ExpiredSignatureError, InvalidTokenError
from ...config import jwt_token_expires, jwt_refresh_token_expires, SECRET_KEY

def generate_token(user_id, token_type='access'):
    """Generate JWT token"""
    if token_type == 'access':
        expires_in = jwt_token_expires
    else:
        expires_in = jwt_refresh_token_expires

    payload = {
        'sub': user_id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(seconds=expires_in),
        'type': token_type
    }

    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


def verify_token(token):
    """Verify token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except ExpiredSignatureError: 
        raise Exception('Token expired')
    except InvalidTokenError:
        raise Exception('Invalid token')
