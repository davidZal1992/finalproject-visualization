from typing import List
from pydantic import BaseModel
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile,Response,Request
import pandas as pd
import shutil
import json
import uuid
from utils import heatmap
import os


router = APIRouter()


@router.post('/uploadone')
async def upload_file(files:List = File(...)):
    if not os.path.exists('upload_data'):
        os.makedirs('upload_data')
    temp_files_array = []    
    rand_folder_name = uuid.uuid4()
    os.makedirs(f"upload_data/{rand_folder_name}")
    file_location = f"upload_data/{rand_folder_name}/heatmap.csv"
    print(file_location)
    temp_files_array.append(file_location)    
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(files[0].file, file_object)
    row_distance= str(files[1]).lower()
    row_linkage= str(files[2]).lower()
    
    respone_heatmap = heatmap.create_heatmap_json(file_location,row_distance=row_distance,row_linkage=row_linkage)
        
    return respone_heatmap
    


  
@router.post('/upload')
async def upload_two_files(files:List = File(...)):
    if not os.path.exists('upload_data'):
        os.makedirs('upload_data')
    temp_files_array = []  
    index_file = ['1','2','connections']
    only_files=list(filter(lambda x: (type(x) is not str) ,files))
    rand_folder_name = uuid.uuid4()
    os.makedirs(f"upload_data/{rand_folder_name}")
    for file in only_files:
        file_location =  f"upload_data/{rand_folder_name}/heatmap_{index_file.pop()}.csv"
        temp_files_array.append(file_location)
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object) 
    row_distance= 'canberra'
    row_linkage= 'single'
    try:
        # respone_first_heatmap = heatmap.create_heatmap_json('Mirim.csv',row_distance=row_distance,row_linkage=row_linkage)
        # respone_second_heatmap = heatmap.create_heatmap_json('Geneim.csv',row_distance=row_distance,row_linkage=row_linkage)
        respone_first_heatmap = heatmap.create_heatmap_json(temp_files_array[0],row_distance=row_distance,row_linkage=row_linkage)
        respone_second_heatmap = heatmap.create_heatmap_json(temp_files_array[1],row_distance=row_distance,row_linkage=row_linkage)
        twomaps={ "first": respone_first_heatmap, "second": respone_second_heatmap };
        return twomaps;
    except Exception as e:
        print(e)
  
@router.post('/union')
async def union(request: Request):
    # row_distance= 'canberra'
    # row_linkage= 'single'
    data_json =   await request.body()
    df_con =  pd.read_csv('conections.csv')
    df_gene =  pd.read_csv('Geneim.csv')
    df_mirim =  pd.read_csv('Mirim.csv')
    obj = json.loads(data_json)
    type_action = obj['type']
    search_for_src = [x['name'] for x in  obj['data']]
    if type_action == "union1":
        result = df_con[df_con['mir_num'].str.contains('|'.join(search_for_src))] 
        result = result.iloc[:,1:]
        search_for_trg = result.stack().tolist()
        print(search_for_trg)
        heatmap_values = df_gene[df_gene['id'].str.contains('|'.join(search_for_trg))]
        heatmap_values =  [heatmap_values.columns.values.tolist()]+heatmap_values.values.tolist()
    else:
        result = df_con[df_con.isin(search_for_src).any(1)].mir_num.tolist()
        print(result)
        heatmap_values = df_mirim[df_mirim['id'].isin(list_mir)]
        heatmap_values =  [heatmap_values.columns.values.tolist()]+heatmap_values.values.tolist()
    print(heatmap_values)
    # return heatmap.create_heatmap_json_without_cluster(heatmap_values,csv=False)
    return heatmap_values
    


@router.post('/intersection')
async def intersection(request: Request):
    data_json =   await request.body()
    df_con =  pd.read_csv('conections.csv')
    df_gene =  pd.read_csv('Geneim.csv')
    df_mirim =  pd.read_csv('Mirim.csv')
    obj = json.loads(data_json)
    type_action = obj['type']
    search_for_src = [x['name'] for x in  obj['data']]
    df_con = df_con.set_index('mir_num')
    if type_action == "intersection1":
        gen_find = df_con.loc[search_for_src].values
        gen_find_inter = list(set.intersection(*[set(x) for x in result]))
        gen_find_inter = [s for s in gen_find_inter if str(s) != 'nan']
        heatmap_values = df_gene[df_gene['id'].str.contains('|'.join(gen_find_inter))]
        heatmap_values =  [heatmap_values.columns.values.tolist()]+heatmap_values.values.tolist()
    else:
        mir_find = []
        for g in gen:
            mir_find.append(df_con[df_con.eq(g).any(1)].mir_num.tolist())
        result = set(mir_find[0]).intersection(*mir_find[:1])
        heatmap_values = df_mirim[df_mirim['id'].isin(list_mir)]
        heatmap_values =  [heatmap_values.columns.values.tolist()]+heatmap_values.values.tolist()
    print(heatmap_values)
    return heatmap_values


@router.get('/vis_matrix/{id}')
async def generate_heatmap(id: str,request :Request):
    data_json =   await request.body()
    print(data_json)


    