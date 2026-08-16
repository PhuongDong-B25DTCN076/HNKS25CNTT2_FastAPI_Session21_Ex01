from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "super_secret_key_change_me_in_production"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_minutes: int):
    to_encode = data.copy()
    
    # Tính toán thời gian hết hạn
    expire = datetime.now(timezone.utc) + timedelta(minutes= expires_minutes)
    
    to_encode.update({"exp": expire})
    
    # Mã hóa và ký token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token đã hết hạn.")
    except jwt.InvalidTokenError:
        raise Exception("Token không hợp lệ hoặc chữ ký bị sai.")

if __name__ == "__main__":
    token = create_access_token(
        data={
            "sub": "student01@gmail.com",
            "user_id": 1,
            "role": "student"
        },
        expires_minutes=30
    )

    print("Generated Token:")
    print(token)
    print("\nDecoded Payload:")
    print(decode_access_token(token))