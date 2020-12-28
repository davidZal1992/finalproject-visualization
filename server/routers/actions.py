from fastapi import APIRouter,Header,HTTPException
router = APIRouter()


@router.get("/")
async def generate_process():
    return [{"Test": "Test"}, {"Test": "Test"}]