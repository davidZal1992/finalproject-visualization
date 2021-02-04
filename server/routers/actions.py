from typing import List
from pydantic import BaseModel
from fastapi import APIRouter,Header,HTTPException,FastAPI, File, UploadFile,Response,Request
import json
import pandas as pd
import shutil
import json
import uuid
from utils import heatmap
import os


router = APIRouter()


@router.post('/uploadone')
async def upload_file(response: Response,files:List = File(...)):
    properties = json.loads(files[len(files)-1])

    rand_user_id = uuid.uuid4()
    # JUST FOR TEST TO AVOID A LOT OF FILES
    #
    rand_user_id='aae10d89-5fed-4fb4-b2d7-1ac709fb9534'
    #
    files_tuple = []
    filenames = []
    locations_of_files = {}

    #PREPARE ALL THE DATA
    prepare_file(rand_user_id) 

    one_heatmap_properties(files_tuple,rand_user_id,files,filenames,locations_of_files,properties) 
    copy_files(files_tuple)

    #USE INCHLIB LIBRARY
    respone_heatmap = create_heat_map(properties,properties,locations_of_files)
    
    #RESPONSE TO CLIENT UUID
    response.headers["uuid"] = str(rand_user_id)
        
    return respone_heatmap
    


  
@router.post('/upload')
async def upload_two_files(response: Response,files:List = File(...)):
    properties = json.loads(files[len(files)-1])

    rand_user_id = uuid.uuid4()
    # JUST FOR TEST TO AVOID A LOT OF FILES
    #
    rand_user_id='aae10d89-5fed-4fb4-b2d7-1ac709fb9534'
    #
    files_tuple = []
    filenames = []
    locations_of_files = {}

      
    prepare_file(rand_user_id) 

    print('propertiesssssssss,',properties)
    properties['metadata1']=properties['metadata']
    properites_first_map = get_prop(properties,'file1','1','metadata1','raw_linkage','raw_distance','both1','column_linkage','column_distance')
    two_heatmap_properties(files_tuple,rand_user_id,files,filenames,locations_of_files,properties)
    copy_files(files_tuple)

    create_connection_file(files[len(files)-2],rand_user_id)

    respone_first_heatmap = create_heat_map(properties,properites_first_map,locations_of_files)

    properites_second_map = get_prop(properties,'file2','2','metadata2','raw_linkage2','raw_distance2','both2','column_linkage2','column_distance2')
    respone_second_heatmap = create_heat_map(properties,properites_second_map,locations_of_files)
        
    print('------------------------------')
    print('respone_first_heatmap------------------------------',respone_first_heatmap)
    print('respone_second_heatmap------------------------------',respone_second_heatmap)

    twomaps={ "first": respone_first_heatmap, "second": respone_second_heatmap}; #need to get also 2 connection dict 


    response.headers["uuid"] = str(rand_user_id)
    
    return twomaps
    
    
  
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



def one_heatmap_properties(files_tuple,rand_user_id,files,filenames,locations_of_files,properties):

    files_tuple.append((files[0],f"upload_data/{rand_user_id}/heatmap1.csv"))
    locations_of_files['heatmap1']=(f"upload_data/{rand_user_id}/heatmap1.csv")
    filenames.append("heatmap1.csv")

    if(properties['metadata'] == '1'):
        files_tuple.append((files[1],f"upload_data/{rand_user_id}/metadata.csv"))
        filenames.append("metadata.csv")
        locations_of_files['metadata']=(f"upload_data/{rand_user_id}/metadata.csv")


def two_heatmap_properties(files_tuple,rand_user_id,files,filenames,locations_of_files,properties):
    index_for_second_heatmap = False
    files_tuple.append((files[0],f"upload_data/{rand_user_id}/heatmap1.csv"))
    locations_of_files['heatmap1']=(f"upload_data/{rand_user_id}/heatmap1.csv")
    filenames.append("heatmap1.csv")
    if(properties['metadata'] == '1'):
        index_for_second_heatmap = True
        files_tuple.append((files[1],f"upload_data/{rand_user_id}/metadata1.csv"))
        filenames.append("metadata1.csv")
        locations_of_files['metadata1']=(f"upload_data/{rand_user_id}/metadata1.csv")

    if index_for_second_heatmap == True:
        files_tuple.append((files[2],f"upload_data/{rand_user_id}/heatmap2.csv"))
    else:
        files_tuple.append((files[1],f"upload_data/{rand_user_id}/heatmap2.csv"))
        
    locations_of_files['heatmap2']=(f"upload_data/{rand_user_id}/heatmap2.csv")
    filenames.append("heatmap2.csv")

    if properties['metadata2'] == '1' :
        if index_for_second_heatmap == True:
            files_tuple.append((files[3],f"upload_data/{rand_user_id}/metadata2.csv"))
        else:
            files_tuple.append((files[2],f"upload_data/{rand_user_id}/metadata2.csv"))
        filenames.append("metadata2.csv")
        locations_of_files['metadata2']=(f"upload_data/{rand_user_id}/metadata2.csv")




def prepare_file(id):
    if not os.path.exists('upload_data'):
        os.makedirs('upload_data')
    if os.path.exists(f"upload_data/{id}"):
        shutil.rmtree(f"upload_data/{id}")
    os.makedirs(f"upload_data/{id}")
    
def copy_files(files):
    for file in files:
        file_location =  file[1]
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file[0].file, file_object) 

def get_prop(properties,file, file_num,metadata,raw_linkage,raw_distance,both,column_linkage,column_distance):
    properties_edit ={}
    properties_edit['file'] = properties[file]
    properties_edit['file_num'] = file_num
    print('ppppproperties', properties)
    properties_edit[metadata] = properties[metadata]
    properties_edit['raw_linkage'] = properties[raw_linkage]
    properties_edit['raw_distance'] = properties[raw_distance]
    if properties[both] == 1:
        properties_edit[both] = 1
        properties_edit['column_linkage'] = properties[column_linkage]
        properties_edit['column_distance'] = properties[column_distance] 
    else:
        properties_edit[both] = 0
    print('properties_edittttt',properties_edit)    
    return properties_edit

def create_heat_map(original_propperties, heatmap_propperties,locations_of_files):
    print('heatmap_propperties:',heatmap_propperties)
    print('locations_of_filesssss:',locations_of_files)
    try:
        map_num= int(heatmap_propperties['file_num']);
        heatmapId= 'heatmap'+str(map_num)
        metadataId= 'metadata'+str(map_num)
        bothId= 'both'+str(map_num)

    except:
        map_num=1
        heatmapId= 'heatmap1'
        metadataId= 'metadata'
        bothId= 'both1'

    print('heatmap_proppertiesssss',heatmap_propperties)
    if heatmap_propperties[metadataId] =='1':
        if original_propperties[bothId] == 1:
            heatmap_res = heatmap.create_heatmap_json(locations_of_files[heatmapId],metadata=locations_of_files[metadataId],row_distance=heatmap_propperties['raw_distance'],row_linkage=heatmap_propperties['raw_linkage'],column_distance=heatmap_propperties['column_distance'],column_linkage=heatmap_propperties['column_linkage'],properties=heatmap_propperties)
        else:
            # print('map_nummmmmm', map_num)
            # print('heatmapId', locations_of_files[heatmapId])
            # print('metadataaaaa ', locations_of_files[metadataId])
            heatmap_res = heatmap.create_heatmap_json(locations_of_files[heatmapId],metadata=locations_of_files[metadataId],row_distance=heatmap_propperties['raw_distance'],row_linkage=heatmap_propperties['raw_linkage'],properties=heatmap_propperties)
            # print('heatmap_ressss:',heatmap_res)
    else:
        if original_propperties[bothId] == 1:
            print('where is column_distance- original_propperties:', original_propperties)
            heatmap_res = heatmap.create_heatmap_json(locations_of_files[heatmapId],row_distance=heatmap_propperties['raw_distance'],row_linkage=heatmap_propperties['raw_linkage'],column_distance=heatmap_propperties['column_distance'],column_linkage=heatmap_propperties['column_linkage'],properties=heatmap_propperties)
        else:
            heatmap_res = heatmap.create_heatmap_json(locations_of_files[heatmapId],row_distance=heatmap_propperties['raw_distance'],row_linkage=heatmap_propperties['raw_linkage'],properties=heatmap_propperties)
    return heatmap_res


def create_connection_file(file,id):
    print(file)
    location = f"upload_data/{id}/connection.csv"
    with open(location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)