import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

#config
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB") 
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

#print(server.config["MYSQL_HOST"])

@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization #must have basic authorization header (username + password)
    if not auth:
        return "Missing credentials", 401
    
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email FROM user WHERE email=%s", (auth.username)
    )
    if res > 0:
        user_row = cur.fetchOne()
        email = user_row[0]
        password = user_row[1]

        if email != auth.username or password != auth.password :
            return "Invalid credentials", 401
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
    else:
        return "Invalid credentials", 401
    
@server.route("/validate", methods=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "Missing credentials (JWT token)", 401
    
    encoded_jwt = encoded_jwt.split(" ")[0]

    try: 
        decoded = jwt.decode(
            encoded_jwt,
            os.environ.get("JWT_SECRET"),
            algorithm="HS256"
        )
    except:
        return "Not authorized", 403
    
    return decoded, 200

    
def createJWT(username, secret, authz):
    """
    Create a JSON Web Token (JWT) for authentication.

    This function generates a JWT containing user information and expiration details.

    Args:
        username (str): The username to be included in the JWT payload.
        secret (str): The secret key used to sign the JWT.
        authz (bool): A flag indicating whether the user has admin privileges.

    Returns:
        str: An encoded JWT string.
    """
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
             + datetime.timedelta(days=1),
            "iat": datetime.datetime.now(tz=datetime.timezone.utc),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )

if __name__ == "__main__": #when this file is executed
    server.run(host="0.0.0.0", port=5000)