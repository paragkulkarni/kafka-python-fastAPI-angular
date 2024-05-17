# from fastapi import FastAPI
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# app = FastAPI()

# database_url = "postgresql://root:root@localhost:5433/vocamuch"
# try:
#     engine = create_engine(database_url)
# except:
#   print("Something else went wrong")
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# db = SessionLocal()


# def dbEngine():
#     return engine

# def dbSession():
#     return db

# def get_db():
#     try:
#         yield db
#     finally:
#         db.close()




# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
from sqlalchemy import text

# DEFINE THE DATABASE CREDENTIALS
user = 'root'
password = 'root'
host = '127.0.0.1'
port = 5433
database = 'vocamuch'
 
# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

 
# if __name__ == '__main__':
 
#     try:
#         # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#         engine = get_connection()
#         print(
#             f"Connection to the {host} for user {user} created successfully.")
#     except Exception as ex:
#         print("Connection could not be made due to the following error: \n", ex)