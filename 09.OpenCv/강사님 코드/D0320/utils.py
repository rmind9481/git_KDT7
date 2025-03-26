import matplotlib.pyplot as plt      # 시각화 모듈

## 시각화 기능 함수
def drawImage(row, col, imgList):
    fig, axes  = plt.subplots(row, col)
    axes = axes.flatten() if col >= 2 else [axes]

    for ax, img in zip(axes, imgList):
        ax.imshow(img)
        ax.set_title(f'{img.shape}')
        
    plt.tight_layout() # 보기 좋게 행과 열의 간격 띄우기
    plt.show()