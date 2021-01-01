from typing import List
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()

import pandas as pd

@router.post('/upload')
def upload_file(files: List[UploadFile] = File(...)):
    miRNA_data = pd.read_csv(files[0].file)
    targets_data = pd.read_csv(files[1].file)
    connections_data = pd.read_csv(files[2].file)
    print('get data')
    return {"hello": "world"}


@router.get('/upload2')
def upload_file2():
    print('success')
    return {"hello": "world"}
  

