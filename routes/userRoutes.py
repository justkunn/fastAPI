from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database_session import get_db
from database.modelsTable import dataUsers
from schema.usersSchema import responseData, responseDelete, responseUsers, updateDataUsers

userRoute = APIRouter()

@userRoute.get(path='/getDataUsers', response_model=responseUsers, summary="Get all data users")
async def getAllDataUsers(db: Session = Depends(get_db)):
    try:
        showDataUsers = db.query(dataUsers).all()
        if not showDataUsers:
            raise HTTPException(status_code=404, detail="user not found")

        response = [
            {
                "id": data.id,
                "name": data.name,
                "job": data.job,
                "salary":data.salary
            }
            for data in showDataUsers     
        ]
        return responseUsers(status="success", message="data showed", data=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@userRoute.post(path='/addNewUsers', response_model=responseUsers, summary="add new users")
async def addUsers(users: responseData, db: Session = Depends(get_db)):
    try:
        check_data = db.query(dataUsers).filter(dataUsers.id == users.id).first()
        if check_data:
            raise HTTPException(status_code=999, detail="user was exist")
        
        new_users = dataUsers(
            name=users.name,
            job=users.job,
            salary=users.salary
        )
        db.add(new_users)
        db.commit()
        
        return responseUsers(status="success", message="success add new users", data=[new_users])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}')
    

@userRoute.put(path='/userUpdate/{user_id}', response_model=responseUsers, summary="update data")
async def updateData(user_id: int ,updateData: updateDataUsers, db: Session = Depends(get_db)):
    try:
        update_data = db.query(dataUsers).filter(dataUsers.id == user_id).first()
        if not update_data:
            raise HTTPException(status_code=500, detail="user not found")
        
        if updateData.name:
            update_data.name = updateData.name
        if updateData.job:
            update_data.job = updateData.job
        if updateData.salary:
            update_data.salary = updateData.salary
            
        db.commit()
        db.refresh(update_data)
        return responseUsers(status="success", message="berrhasil", data=[update_data])
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    

@userRoute.delete(path='/userDelete/{user_id}', response_model=responseUsers, summary='delete users')
async def deleteUsers(user_id: int, db: Session = Depends(get_db)):
    try:
        delete_user = db.query(dataUsers).filter(dataUsers.id == user_id).first()
        if not delete_user:
            raise HTTPException(status_code=500, detail="user not found")
        
        data_delete = {
            'id': delete_user.id,
            'name': delete_user.name,
            'job': delete_user.job,
            'salary': delete_user.salary
        }
        
        
        db.delete(delete_user)
        db.commit()
        
        return responseUsers(status="success", message="users success to delete", data=[data_delete])
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'{e}') 