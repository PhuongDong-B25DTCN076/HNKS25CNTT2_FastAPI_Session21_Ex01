import bcrypt

def hash_password(password: str):
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    # Thực hiện băm mật khẩu
    hashed = bcrypt.hashpw(password_bytes, salt)
    # Trả về chuỗi hash dạng str
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str):
    plain_bytes = plain_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hashed_bytes)

if __name__ == "__main__":
    password = "Rikkei@123"

    hashed_password = hash_password(password)
    print(hashed_password)
    print(verify_password("Rikkei@123", hashed_password)) # Đúng
    print(verify_password("Rikkei@456", hashed_password)) # Sai