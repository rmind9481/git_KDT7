# ----------------------------------------------------
# CSV File ==> DataFrame 으로 가져오기
# - 함수 : pandas.read_csv
# ----------------------------------------------------

import pandas as pd

# -------------------------------------
# 데이터 준비
# ------------------------------------

DATA_PATH = r'C:\Users\KDP-17\Desktop\KDT_7\02.PANDAS\DATA\member.csv'

memberDF =pd.read_csv(DATA_PATH)
print(f"[memberDF]----\n{memberDF}")