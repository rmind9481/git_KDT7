import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import *
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score
from sklearn.preprocessing import *
import math

# 함수 목차
# 1) 단일 피쳐의 상관계수 확인 및 산점도 그래프화                                 
# 2) 데이터 전처리                                                              !! 다른 전처리 함수 추가
# 3) 피쳐와 타겟 입력받아 학습용과 테스트용으로 데이터 분리
# 4) 학습 데이터와 테스트 데이터 입력받아 회귀분석및 결과값 데이터프레임으로 반환 (릿지,라쏘,엘라스틱,선형,로지스틱)  !! KNN추가
# 5) 4에서 반환받은 데이터 프레임을 입력하여 score와 loss 시각화
# 6) 모델과 테스트 데이터를 받아 예측 후 r2_score와 RMSE를 계산·출력하고 반환
# 7) 사용자 입력 -> float 변환 -> DataFrame 구성 -> 예측 -> 결과 출력하는 함수    !! 데이터 입력받은 값 체크하는 기능 추가

###############################################################################
# 1) feature와 target을 입력받아 subplot으로 시각화 + 각 그래프에 상관계수 출력
def plot_features_and_target(df, feature_cols, target_col):
    """
    df           : pandas DataFrame
    feature_cols : 시각화할 feature(컬럼)들의 리스트
    target_col   : 단일 target 컬럼 이름
    """
    # 몇 행이 필요한지 계산
    nrows = math.ceil(len(feature_cols) / 3)
    ncols = 3
    X=0
    Y=0
    if len(feature_cols)/3<len(feature_cols)/nrows:
        X=10
        Y=3
    elif len(feature_cols)/3>len(feature_cols)*1.5/nrows:
        X=len(feature_cols)
        Y=len(feature_cols)**2/13.55
    

    # 서브플롯 생성
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=( X, Y))
    
    # axes를 1차원 배열로 만듦(예: shape=(nrows*ncols,))
    # nrows*ncols가 1인 경우도 일관되게 처리하기 위해 리스트로 감싸는 로직 추가
    if isinstance(axes, np.ndarray):
        axes = axes.flatten()
    else:
        axes = [axes]  # axes가 단 하나인 경우
    
    # feature별로 반복
    for i, feature in enumerate(feature_cols):
        ax = axes[i]
        ax.scatter(df[feature], df[target_col])
        
        # 상관계수
        corr_value = df[feature].corr(df[target_col])
        ax.set_title(f'{feature} vs {target_col} (corr={corr_value:.2f})')
        ax.set_xlabel(feature)
        ax.set_ylabel(target_col)
    
    # 만약 feature 개수보다 subplot 수가 많은 경우, 남는 축은 숨긴다.
    for j in range(len(feature_cols), len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()

###############################################################################
###### 데이터 preprocessing 함수 사용
# 2-1) DataFrame을 입력받아 PowerTransformer로 데이터를 정규화 후 반환
def power_transform_dataframe(df):
    """
    df: pandas DataFrame
    """
    # PowerTransformer 객체 생성
    pt = PowerTransformer()
    
    # fit_transform 수행
    transformed_data = pt.fit_transform(df)
    
    # 원본 컬럼명 유지한 DataFrame으로 변환
    df_transformed = pd.DataFrame(transformed_data, columns=df.columns, index=df.index)
    
    return df_transformed

# 2-2) DataFrame을 입력받아 modified Z-score로 이상치 처리
##     modified Z-score는 이상치를 감지하는 용도지만 추가로 이상치를 중앙값으로 대체하는 기능을 넣음
def fill_outliers_with_median_modified_zscore(df, threshold=3.5):
    """
    1) 숫자형 컬럼(each numeric column)에 대해:
       - 중앙값(median) 계산
       - MAD(median absolute deviation) 계산
       - Modified Z-Score(M_i) = 0.6745 * (x_i - median) / MAD
       - abs(M_i) > threshold 인 경우 → “이상치”로 간주
       - 이상치인 해당 셀의 값을 “그 컬럼의 중앙값”으로 대체
    2) 반환: outlier가 처리된 새로운 DataFrame
    """
    df_copy = df.copy()
    numeric_cols = df_copy.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        col_data = df_copy[col]
        
        # 중앙값
        median_val = col_data.median()
        # MAD: median of absolute deviations
        mad_val = np.median(np.abs(col_data - median_val))
        if mad_val == 0:
            # 모든 값이 동일하거나 MAD가 0이면 이상치 식별 불가능
            continue
        
        # Modified Z-Score
        M_i = 0.6745 * (col_data - median_val) / mad_val
        
        # threshold 초과시 이상치로 간주
        outlier_mask = np.abs(M_i) > threshold
        
        # 이상치 → 해당 컬럼의 중앙값으로 대체
        df_copy.loc[outlier_mask, col] = median_val
    
    return df_copy

# 2-3) DataFrame을 입력받아 MinMaxScaler로 데이터를 정규화 후 반환
def MinMaxScaler_dataframe(df):
    """
    df: pandas DataFrame
    """
    # MinMaxScaler 객체 생성
    mm = MinMaxScaler()
    
    # fit_transform 수행
    transformed_data = mm.fit_transform(df)
    
    # 원본 컬럼명 유지한 DataFrame으로 변환
    df_transformed = pd.DataFrame(transformed_data, columns=df.columns, index=df.index)
    
    return df_transformed

# 2-4) DataFrame을 입력받아 RobustScaler로 데이터를 정규화 후 반환
##     modified Z-score와 다르게 이상치를 따로 처리하는 것이 아니라 이상치에 영향을 덜 받으며 데이터 정규화
def RobustScaler_dataframe(df):
    """
    df: pandas DataFrame
    """
    # RobustScaler 객체 생성
    rb = RobustScaler()
    
    # fit_transform 수행
    transformed_data = rb.fit_transform(df)
    
    # 원본 컬럼명 유지한 DataFrame으로 변환
    df_transformed = pd.DataFrame(transformed_data, columns=df.columns, index=df.index)
    
    return df_transformed

###############################################################################
# 3) feature와 target 변수를 입력받아 train/test로 분리
def split_train_test(features, target, test_size=0.2, random_state=42):
    """
    features : 2차원(여러 feature) 데이터 (DataFrame 또는 2D array)
    target   : 1차원(단일 target) 데이터 (Series 또는 1D array)
    """
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, 
        test_size=test_size, 
        random_state=random_state
    )
    return x_train, x_test, y_train, y_test

###############################################################################
# 4-1) x_train, x_test, y_train, y_test를 받아서
#    Ridge, Lasso, ElasticNet 각각에 대해 KFold 학습/테스트 후 결과 DataFrame과 모델 반환
def regression_kfold_analysis(x_train, x_test, y_train, y_test, alpha_list=None):
    """
    x_train, x_test, y_train, y_test : 학습/테스트용 데이터
    alpha_list                       : 하이퍼파라미터 alpha 후보 리스트(예: [0.01, 0.1, 1, 10])
    
    반환값: (ridge_df, lasso_df, elastic_df)
            -> 각 모델별로 train_score/test_score, train_loss/test_loss가 담긴 DataFrame
    """
    if alpha_list is None:
        alpha_list = [0.01, 0.1, 1.0, 10.0]
    
    # 결과 저장용 DataFrame 생성
    ridge_df = pd.DataFrame(columns=['alpha','train_score','test_score','train_loss','test_loss'])
    lasso_df = pd.DataFrame(columns=['alpha','train_score','test_score','train_loss','test_loss'])
    elastic_df = pd.DataFrame(columns=['alpha','train_score','test_score','train_loss','test_loss'])
    
    # KFold 객체 생성
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    # Ridge
    for alpha in alpha_list:
        ridge_model = Ridge(alpha=alpha)
        
        train_scores = []
        train_losses = []
        for train_idx, val_idx in kf.split(x_train):
            X_tr, X_val = x_train.iloc[train_idx], x_train.iloc[val_idx]
            Y_tr, Y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
            
            ridge_model.fit(X_tr, Y_tr)
            
            pred_tr = ridge_model.predict(X_tr)
            train_r2 = r2_score(Y_tr, pred_tr)
            train_mse = mean_squared_error(Y_tr, pred_tr)
            
            train_scores.append(train_r2)
            train_losses.append(train_mse)
        
        # cross-validation 평균
        avg_train_score = np.mean(train_scores)
        avg_train_loss = np.mean(train_losses)
        
        # 전체 train으로 다시 학습 후 test 데이터 평가
        ridge_model.fit(x_train, y_train)
        pred_test = ridge_model.predict(x_test)
        test_score = r2_score(y_test, pred_test)
        test_loss = mean_squared_error(y_test, pred_test)
        
        # 결과 저장
        ridge_df.loc[len(ridge_df)] = [alpha, avg_train_score, test_score, avg_train_loss, test_loss]

    # Lasso
    for alpha in alpha_list:
        lasso_model = Lasso(alpha=alpha)
        
        train_scores = []
        train_losses = []
        for train_idx, val_idx in kf.split(x_train):
            X_tr, X_val = x_train.iloc[train_idx], x_train.iloc[val_idx]
            Y_tr, Y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
            
            lasso_model.fit(X_tr, Y_tr)
            
            pred_tr = lasso_model.predict(X_tr)
            train_r2 = r2_score(Y_tr, pred_tr)
            train_mse = mean_squared_error(Y_tr, pred_tr)
            
            train_scores.append(train_r2)
            train_losses.append(train_mse)
        
        avg_train_score = np.mean(train_scores)
        avg_train_loss = np.mean(train_losses)
        
        lasso_model.fit(x_train, y_train)
        pred_test = lasso_model.predict(x_test)
        test_score = r2_score(y_test, pred_test)
        test_loss = mean_squared_error(y_test, pred_test)
        
        lasso_df.loc[len(lasso_df)] = [alpha, avg_train_score, test_score, avg_train_loss, test_loss]

    # ElasticNet
    for alpha in alpha_list:
        elastic_model = ElasticNet(alpha=alpha)
        
        train_scores = []
        train_losses = []
        for train_idx, val_idx in kf.split(x_train):
            X_tr, X_val = x_train.iloc[train_idx], x_train.iloc[val_idx]
            Y_tr, Y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
            
            elastic_model.fit(X_tr, Y_tr)
            
            pred_tr = elastic_model.predict(X_tr)
            train_r2 = r2_score(Y_tr, pred_tr)
            train_mse = mean_squared_error(Y_tr, pred_tr)
            
            train_scores.append(train_r2)
            train_losses.append(train_mse)
        
        avg_train_score = np.mean(train_scores)
        avg_train_loss = np.mean(train_losses)
        
        elastic_model.fit(x_train, y_train)
        pred_test = elastic_model.predict(x_test)
        test_score = r2_score(y_test, pred_test)
        test_loss = mean_squared_error(y_test, pred_test)
        
        elastic_df.loc[len(elastic_df)] = [alpha, avg_train_score, test_score, avg_train_loss, test_loss]

    # 결과 DataFrame 출력(필요시)
    print("=== Ridge 결과 ===")
    print(ridge_df, "\n")
    print("=== Lasso 결과 ===")
    print(lasso_df, "\n")
    print("=== ElasticNet 결과 ===")
    print(elastic_df, "\n")
    
    return ridge_df, lasso_df, elastic_df,ridge_model,lasso_model,elastic_model

# 4-2) x_train, x_test, y_train, y_test를 받아서
#    LogisticRegression에 대해 KFold 학습/테스트 후 결과 DataFrame과 모델 반환
def LogisticRegression_kfold_analysis(x_train, x_test, y_train, y_test, alpha_list=None):
    """
    x_train, x_test, y_train, y_test : 학습/테스트용 데이터
    alpha_list                       : 하이퍼파라미터 alpha 후보 리스트(예: [0.01, 0.1, 1, 10])
    
    반환값: (logistic_df)
            -> 각 모델별로 train_score/test_score, train_loss/test_loss가 담긴 DataFrame
    """
    if alpha_list is None:
        alpha_list = [0.01, 0.1, 1.0, 10.0]
    
    # 결과 저장용 DataFrame 생성
    logistic_df = pd.DataFrame(columns=['alpha','train_score','test_score','train_loss','test_loss'])
   
    # KFold 객체 생성
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    # logistic regression
    for alpha in alpha_list:
        logistic_model = LogisticRegression(alpha=alpha)
        
        train_scores = []
        train_losses = []
        for train_idx, val_idx in kf.split(x_train):
            X_tr, X_val = x_train.iloc[train_idx], x_train.iloc[val_idx]
            Y_tr, Y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
            
            logistic_model.fit(X_tr, Y_tr)
            
            pred_tr = logistic_model.predict(X_tr)
            train_r2 = r2_score(Y_tr, pred_tr)
            train_mse = mean_squared_error(Y_tr, pred_tr)
            
            train_scores.append(train_r2)
            train_losses.append(train_mse)
        
        # cross-validation 평균
        avg_train_score = np.mean(train_scores)
        avg_train_loss = np.mean(train_losses)
        
        # 전체 train으로 다시 학습 후 test 데이터 평가
        logistic_model.fit(x_train, y_train)
        pred_test = logistic_model.predict(x_test)
        test_score = r2_score(y_test, pred_test)
        test_loss = mean_squared_error(y_test, pred_test)
        
        # 결과 저장
        logistic_df.loc[len(logistic_df)] = [alpha, avg_train_score, test_score, avg_train_loss, test_loss]
    
    # 결과 DataFrame 출력(필요시)
    print("=== LogisticRegression 결과 ===")
    print(logistic_df, "\n")

    
    return logistic_df,logistic_model 
        
# 4-3) x_train, x_test, y_train, y_test를 받아서
#    LinearRegression에 대해 KFold 학습/테스트 후 결과 DataFrame과 모델 반환
def LinearRegression_kfold_analysis(x_train, x_test, y_train, y_test, alpha_list=None):
    """
    x_train, x_test, y_train, y_test : 학습/테스트용 데이터
    alpha_list                       : 하이퍼파라미터 alpha 후보 리스트(예: [0.01, 0.1, 1, 10])
    
    반환값: (logistic_df)
            -> 각 모델별로 train_score/test_score, train_loss/test_loss가 담긴 DataFrame
    """
    if alpha_list is None:
        alpha_list = [0.01, 0.1, 1.0, 10.0]
    
    # 결과 저장용 DataFrame 생성
    linear_df = pd.DataFrame(columns=['alpha','train_score','test_score','train_loss','test_loss'])
   
    # KFold 객체 생성
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    # linear regression
    for alpha in alpha_list:
        linear_model = LinearRegression(alpha=alpha)
        
        train_scores = []
        train_losses = []
        for train_idx, val_idx in kf.split(x_train):
            X_tr, X_val = x_train.iloc[train_idx], x_train.iloc[val_idx]
            Y_tr, Y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]
            
            linear_model.fit(X_tr, Y_tr)
            
            pred_tr = linear_model.predict(X_tr)
            train_r2 = r2_score(Y_tr, pred_tr)
            train_mse = mean_squared_error(Y_tr, pred_tr)
            
            train_scores.append(train_r2)
            train_losses.append(train_mse)
        
        # cross-validation 평균
        avg_train_score = np.mean(train_scores)
        avg_train_loss = np.mean(train_losses)
        
        # 전체 train으로 다시 학습 후 test 데이터 평가
        linear_model.fit(x_train, y_train)
        pred_test = linear_model.predict(x_test)
        test_score = r2_score(y_test, pred_test)
        test_loss = mean_squared_error(y_test, pred_test)
        
        # 결과 저장
        linear_df.loc[len(linear_df)] = [alpha, avg_train_score, test_score, avg_train_loss, test_loss]
    
    # 결과 DataFrame 출력(필요시)
    print("=== LinearRegression 결과 ===")
    print(linear_df, "\n")

    
    return linear_df,linear_model 

###############################################################################
# 5) DataFrame을 입력받아 x축=alpha, 첫 그래프=(train_score, test_score), 두 번째=(train_loss, test_loss) 시각화
def plot_regression_results(df):
    """
    df: 위에서 만든 result DataFrame(예: ridge_df, lasso_df, elastic_df)
    """
    fig, axes = plt.subplots(nrows=2, figsize=(8, 10))
    
    # 1) alpha vs (train_score, test_score)
    axes[0].plot(df['alpha'], df['train_score'],'o-', label='train_score')
    axes[0].plot(df['alpha'], df['test_score'],'o-' ,label='test_score')
    axes[0].set_xlabel('alpha')
    axes[0].set_ylabel('score')
    axes[0].legend()
    axes[0].set_title('Score')
    
    # 2) alpha vs (train_loss, test_loss)
    axes[1].plot(df['alpha'], df['train_loss'],'o-', label='train_loss')
    axes[1].plot(df['alpha'], df['test_loss'],'o-', label='test_loss')
    axes[1].set_xlabel('alpha')
    axes[1].set_ylabel('loss')
    axes[1].legend()
    axes[1].set_title('Loss')
    
    plt.tight_layout()
    plt.show()

###############################################################################
# 6) 모델과 테스트 데이터를 받아 예측 후 r2_score와 RMSE를 계산·출력하고 반환하는 함수
def predict_and_evaluate_model(model, X_test, y_test):
    """
    model  : 학습된 모델 (예: Ridge, Lasso, ElasticNet, etc.)
    X_test : 테스트용 feature 데이터
    y_test : 테스트용 target 데이터
    
    반환값: (score, rmse)
            score = r2_score
            rmse  = Root Mean Squared Error
    """
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)
    # mean_squared_error의 squared=False 옵션으로 RMSE 계산
    rmse = root_mean_squared_error(y_test, predictions)
    
    print(f"R2 Score: {score:.4f}, RMSE: {rmse:.4f}")
    return score, rmse

###############################################################################
# 7) 사용자 입력 -> float 변환 -> DataFrame 구성 -> 예측 -> 결과 출력하는 함수 
def predict_with_user_input(model, feature_cols, df):
    """
    model        : 학습 완료된 모델 (Ridge, Lasso, ElasticNet 등)
    feature_cols : 모델 학습에 사용한 feature 컬럼명 리스트
    df           : 원본 데이터프레임 (또는 feature_cols를 포함한 데이터프레임)
                   -> 각 컬럼의 중앙값 계산용
    
    동작 요약:
    1) df에서 feature_cols의 중앙값 리스트를 구함
    2) 예: 3,4,5 형태로 표시하여 입력 예시를 보여줌
    3) 사용자의 실제 입력값을 받아 DataFrame 생성 후 예측
    """
    print('[예측값 출력]')

    # 각 컬럼의 중앙값
    medians = df[feature_cols].median()

    # 예시 문자열 생성 (예: "3,4,5")
    example_str = ",".join([f"{medians[col]:.3g}" for col in feature_cols])
    
    # 콘솔에 예시 출력 + 실제 입력
    user_input_str = input(f'입력 (예: {example_str}) : ').split(',')
    
    # float 변환
    new_data = [float(data.strip()) for data in user_input_str]
    print(new_data)  # 요청에 따라 입력값 출력

    # DataFrame 생성
    dataDF = pd.DataFrame([new_data], columns=feature_cols)
    
    # 예측
    prediction = model.predict(dataDF)
    
    # 예측값 출력
    print("예측값:", prediction[0])
    return prediction


    
