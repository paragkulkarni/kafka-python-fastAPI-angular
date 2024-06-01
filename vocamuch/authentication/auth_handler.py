from datetime import datetime, timedelta, timezone
import jwt
import time



def encoderToken(user):
    payload={
        "name": user,
        "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=24*60*60)
        }
    encoded_data = jwt.encode(payload,
                              key='secret',
                              algorithm="HS256")
    return encoded_data

def decoderToken(token):
    decoded_data = jwt.decode(jwt=token,
                              key='secret',
                              algorithms=["HS256"])

    print("csdsdsds233 ",decoded_data)
    return decoded_data

def endTokenSession(user):
    return {"logout": True}


