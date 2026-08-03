# from uuid import UUID

from fastapi import APIRouter, Depends # HTTPException
from pydantic import BaseModel, EmailStr

from database import get_supabase_connection

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

class UserCreate(BaseModel):
    name: str
    email: EmailStr

# @router.get("/{user_id}")
# def get_user_data(
#     user_id: UUID,
#     supabase = Depends(get_supabase_connection)
# ):

#     response = supabase.from_('users').select('id').eq('id', str(user_id)).execute()

#     if not response.data:
#         raise HTTPException(status_code=404, detail="User not found")

#     return response.data[0]

@router.post("/")
def post_user_data(
    user: UserCreate,
    supabase = Depends(get_supabase_connection)
):

    response = supabase.from_('users').insert({
        "name": user.name,
        "email": user.email
        }).execute()

    new_user = response.data[0]

    return new_user