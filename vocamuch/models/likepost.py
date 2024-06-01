from pydantic import BaseModel


class LikePost(BaseModel):
    user_id : int
    post_id: int 
    liked: int
