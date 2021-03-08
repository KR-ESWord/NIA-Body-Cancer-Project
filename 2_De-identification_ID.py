import pandas as pd
import os
import random
import numpy as np
from tqdm.notebook import tqdm
import warnings
warnings.filterwarnings(action='ignore')

# 엑셀 파일 정의
load_excel = os.path.join(os.getcwd(), '<Excel_Name>.xlsx')
save_excel = os.path.join(os.getcwd(), 'De-identification_ID.xlsx')

# 엑셀 파일 호출
id_df = pd.read_excel(load_excel,
                       dtype={
                           'Section' : str,
                            'De-identification_ID' : str,
                            'Patient_ID' : str,
                            'Modality' : str  
                             },
                      engine = 'openpyxl')

# Creat De-identification_ID Algorithm
def create_id():
    string_pool = '0123456789'
    new_id = ''
    for i in range(7):
        new_id += random.choice(string_pool)
    return str(new_id)
  
# Main
for df_index in tqdm(range(len(id_df))):
    # 새로운 Patient ID에 대하여 De-identification ID 할당
    if id_df['De-identification_ID'][df_index] == 'N':
        while True:
            di_id = create_id()
            # 비식별 ID가 중복되지 않을 경우에만 할당
            if di_id not in list(id_df['De-identification_ID'][0:df_index].values):
                ori_df['De-identification_ID'][df_index] = str(di_id).zfill(7)
                break
            else :
                continue

# 비식별 ID 생성한 엑셀 파일 저장
id_df.to_excel(save_excel, index = False)
