from fastapi import FastAPI
from routers import actions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(actions.router)
app.include_router(
    actions.router,
    prefix="/actions",
    tags=["actions"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def hello_world():
    return {"Hello":"world"}




