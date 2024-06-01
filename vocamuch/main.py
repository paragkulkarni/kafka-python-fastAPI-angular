import json
from requests import Session
from database.db import get_connection
from fastapi import Depends, FastAPI, Request
from models.user import Item
from models.word import Word
from sqlalchemy.orm import Session,sessionmaker, scoped_session
from sqlalchemy import insert
from sqlalchemy.sql import text
from fastapi.middleware.cors import CORSMiddleware
import authentication.auth_handler as auth_handler
import authentication.auth_bearer as auth_bearer
from fastapi.responses import JSONResponse

import rabbitmq.connect as rabbitMQ
from models.likepost import LikePost



origins = [
    "http://localhost:4200"
]

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True})

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

engine = get_connection()

scoped_session = scoped_session(sessionmaker(bind=engine))
session = scoped_session()


# rabbitMQ.RabbitMQConnect()
@app.post("/user/")
async def login(item: Item):
    print("body",item)
    # q = "SELECT enable FROM user_details where username='root' and pwd='root'"
    q = ("SELECT enable,id FROM user_details where username='%s' and pwd='%s'"%(item.username, item.password))
    rs = session.execute(text(q))
    for r in rs.fetchall():
        print("2",r)
        if r[0]==True:
            token = auth_handler.encoderToken(item.username)
            return {
                "user-exists":r[0],
                "token": token
            }
    return {"message": "User is not found"}

@app.get("/share-word", dependencies=[Depends(auth_bearer.JWTBearer()),])
async def getWord():
    q = ("select * from public.vw_word_details order by id desc ")
    rs = session.execute(text(q))
    datas = rs.fetchall()
     
    objects = [{
        "id": data[0],
        "userId": data[1],
        "fistName": data[2],
        "word": data[3],
        "description": data[4]
    } for data in datas]
    print(objects)
    return objects



@app.post("/share-word", dependencies=[Depends(auth_bearer.JWTBearer()),])
async def postWord(data: Word):
    print(323232, data) 
    q = ("INSERT INTO voc_details (user_id, word, description) VALUES ('%d', '%s', '%s')"%(data.user_id, data.word, data.description))
    insert_sql = text(q)
    print("223d",insert_sql)
    # with engine.connect() as connection:
    # with session_local.session() as connection:
    session.execute(insert_sql)
    # user=word.user_id
    session.commit()
    return {"message": "success"}


@app.post("/like", dependencies=[Depends(auth_bearer.JWTBearer()),])
async def likePost(data: LikePost):
    # -------write function to insert like and return like count for that post
    insert_sql = text("INSERT INTO public.like_details(user_id, post_id, liked) VALUES ('%d', '%d', '%d')"%(data.user_id,data.post_id,data.liked))
    session.execute(insert_sql)
    session.commit()
    return {"post-like": "success"}

@app.post("/getpost", dependencies=[Depends(auth_bearer.JWTBearer()),])
async def getPostData():
    getdata_sql = text("select * from public.voc_details")
    data = session.execute(getdata_sql)
    posts = data.mappings().all()
    return posts
    
@app.post("/logout")
async def logout():
    print('logout*************************************************')
    logoutMessage = auth_handler.endTokenSession('root')
    return JSONResponse(logoutMessage)