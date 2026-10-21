
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

# 데이터셋 불러오기
california = fetch_california_housing()
print(california.keys())

print('feature_names:', california['feature_names'])
print('target_names:', california['target_names'])
print('DESCR:', california['DESCR'])

print('data shape:', california['data'].shape)
print('target shape:', california['target'].shape)

# ==================================
# ★ 
# ==================================

# 입력 데이터와 타깃 데이터 분리
X = california['data']
y = california['target']

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 선형회귀 모델 생성 및 학습
regression = LinearRegression()
regression.fit(X_train, y_train)

# 모델 예측 및 오차 확인
train_pred = regression.predict(X_train)
test_pred = regression.predict(X_test)

train_mse = mean_squared_error(y_train, train_pred)
test_mse = mean_squared_error(y_test, test_pred)

print("Train MSE:", train_mse)
print("Test MSE:", test_mse)

# 회귀계수와 특성명 출력
print("\n회귀계수 분석")

for name, coef in zip(
    california['feature_names'], regression.coef_
):
    print(f"{name}: {coef:.6f}")

# 집값 상승 관련 상위 3개 속성
positive_coef = [
    (name, coef)
    for name, coef in zip(
        california['feature_names'], regression.coef_
    )
    if coef > 0
]

positive_coef.sort(key=lambda x: x[1], reverse=True)

print("\n집값 상승 관련 상위 3개 속성")

for rank, (name, coef) in enumerate(positive_coef[:3], 1):
    print(f"{rank}위: {name} ({coef:.6f})")
print(regression.coef_)
