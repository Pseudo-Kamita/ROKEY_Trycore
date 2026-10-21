# seaborn을 사용하여 임의의 데이터를 생성하고 히스토그램을 그림
# numpy를 사용하여 평균이 50, 표준편차가 10인 정규 분포 데이터를 1000개 생성
# seaborn.histplot()을 사용하여 히스토그램을 시각화

import numpy
import seaborn
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] ='Malgun Gothic'

# 1000개의 정규 분포 데이터 생성
data = numpy.random.normal(loc = 50, scale = 10, size = 1000)

# 히스토그램 시각화
seaborn.histplot(data, kde = True)
plt.title("정규 분포 히스토그램")
plt.xlabel("값")
plt.ylabel("빈도")
plt.show()



# 7번

# seaborn을 사용하여 tips 데이터셋의 요일(day) 별 전체금액(total_bill)의 박스플롯을 그림
# seaborn.boxplot()을 사용

# tips = seaborn.load_dataset("...tips")
# seaborn.boxplot(x = "day", y = "total_bill", data = tips)
# plt.show()



# 8번

# OpenCV를 사용하여 이미지를 불러오고 화면에 출력
import cv2

# cv2.imread()로 이미지를 로드
image = cv2.imread("D:/Coding/ROKEY/01Python/18-21DeepLearning/testjellybean.jpg")

# cv2.imshow()를 사용하여 출력
cv2.imshow("Image", image)

# cv2.waitKey(0)을 사용하여 창을 닫을 수 있도록 함
cv2.waitKey(0)
cv2.destroyAllWindows()



# 9번

# OpenCV를 사용하여 컬러 이미지를 흑백(그레이스케일)으로 변환
# cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)를 사용하여 변환
# 변환된 이미지를 출력
import cv2

# 이미지 불러오기
image = cv2.imread("D:/Coding/ROKEY/01Python/18-21DeepLearning/testjellybean.jpg")

# 흑백(그레이스케일)으로 변환
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 흑백 이미지 출력
cv2.imshow("Grayscale", grayscale_image)

# 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()



# 10번

# OpenCV의 cv2.Canny()를 사용하여 이미지의 엣지를 감지
# 엣지를 감지한 후, 결과 이미지를 출력

import cv2

# 이미지 불러오기
image = cv2.imread("D:/Coding/ROKEY/01Python/18-21DeepLearning/testjellybean.jpg")

# 엣지 감지
canny_image = cv2.Canny(image, 100, 200)

# 엣지 이미지 출력
cv2.imshow("Canny", canny_image)

# 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()