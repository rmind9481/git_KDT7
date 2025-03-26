# -------------------------------------------------------
#  사용자 정의함수
# -------------------------------------------------------
#
# 함수기능 : 텐서의 속성 출력
# 함수 이름 : printTensorInfo
#
# 매개변수 : tname - 텐서이름
#			tobject - 텐서객체
# 반환값 : 없음


import torch
	# 텐서의 속성 확인
def print_Tensor_into(tname, tobject):
    print(f'{tname}-----------------------')
    print(f'shape  : {tobject.shape}        {tobject.size()}')
    print(f'ndim   : {tobject.shape}        {tobject.dim()}')
    print(f'device : {tobject.device}')
    print(f'dtype  : {tobject.dtype}')
    print(f'tensor   : \n{tobject}')