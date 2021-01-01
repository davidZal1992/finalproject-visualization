from typing import List
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile,Response
import pandas as pd
import shutil
import json
from utils import heatmap
router = APIRouter()




@router.post('/upload')
async def upload_file(files: List[UploadFile] = File(...)):
    # miRNA_data = pd.read_csv(files[0].file)
    # targets_data = pd.read_csv(files[1].file)
    # connections_data = pd.read_csv(files[2].file)
    for file in files:
        file_location = f"{file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(files[0].file, file_object)
    a = [x.filename for x in files]
    try:
        respone_heatmap = heatmap.create_heatmap_json(a[0],a[1],a[2])
        print(respone_heatmap)
    except expression as e:
        print(e)
    
    data = respone_heatmap
    return  data







