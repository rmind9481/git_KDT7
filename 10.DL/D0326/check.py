# ----------------------------------------
# 개발 환경 버전 체크
# ----------------------------------------

import pandas as pd
import matplotlib as mat
import numpy as np
import sklearn
import seaborn as sns
import cv2 
import torch 



# 버전 출력
print(f'pandas v.{pd.__version__}')
print(f'seaborn v.{sns.__version__}')
print(f'scikitlean v.{sklearn.__version__}')
print(f'matplotlib v.{mat.__version__}')
print(f'open cv v.{cv2.__version__}')
print(f'torch v.{torch.__version__}')
print(f'numpy v.{np.__version__}')