from typing import List
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile

router = APIRouter()

import pandas as pd

@router.post('/upload')
def upload_file(files: List[UploadFile] = File(...)):
    miRNA_data = pd.read_csv(files[0].file)
    targets_data = pd.read_csv(files[1].file)
    connections_data = pd.read_csv(files[2].file)

    