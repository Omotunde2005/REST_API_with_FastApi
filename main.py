from fastapi import FastAPI, HTTPException, Header, Request, Depends
from starlette.templating import Jinja2Templates
from models import User, UpdateUserInfo, Users, Base
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import secrets


Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory='templates')


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def authorize_user(api_key: str = Header(...), db: Session = Depends(get_db)):
    key = db.query(Users).filter_by(key=api_key).first()
    if not key:
        raise HTTPException(status_code=404, detail=f'No user with key: {api_key}')
    else:
        return api_key


@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('base.html',
                                      {'request': request})


@app.get('/api/v1/users')
async def fetch_users(db: Session = Depends(get_db)):
    all_users = db.query(Users).all()

    # Returns all users and exclude the 'key' from the response
    all_users_new = []
    for user in all_users:
        user.__dict__.__delitem__('key')
        all_users_new.append(user)

    return all_users_new


@app.post('/api/v1/users/add')
async def post_users(user: User, db: Session = Depends(get_db)):
    key = secrets.token_hex(32)
    new_user = Users(
        first_name=user.first_name,
        second_name=user.last_name,
        age=user.age,
        gender=str(user.gender),
        key=key,
        status=str(user.status)
    )
    db.add(new_user)
    db.commit()
    return {'Your api_key': key,
            'message': 'Ensure you keep this key secured'}


@app.delete("/api/v1/delete/user")
async def delete_user(api_key: str = Depends(authorize_user), db: Session = Depends(get_db)):
    user = db.query(Users).filter_by(key=api_key).first()
    db.delete(user)
    db.commit()
    return {'api_key': api_key,
            'message': 'User info successfully deleted'}


@app.put("/api/v1/update/user")
async def update_user(user_update: UpdateUserInfo, api_key: str = Depends(authorize_user),
                      db: Session = Depends(get_db)):
    user = db.query(Users).filter_by(key=api_key).first()
    user_update_dict = user_update.__dict__
    for key, value in user_update_dict.items():
        if value is not None:
            user.__dict__[key] = value

    return {'api_key': api_key,
            'message': f'User info has been successfully updated'}