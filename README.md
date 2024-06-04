목표 : 영상 데이터에서 인물의 감정을 판별
목적 : AI를 활용한 CV 고도화 (face detection, emotion recognition)
수행 환경 : Windows 10, Pycharm
기술 스택 : Python3 / 

수행 절차
  1. 영상 데이터셋 수집
  2. 영상을 프레임 단위로 분할 : 초 단위 이미지 데이터로 변환
  3. MTCNN 
  4. dlib 모델로 얼굴 확인
  5. 프레임 Crop
  6. Hit, Miss
  7. Hit에 대해 특징점 확인 및 분석

프로젝트 구조
main
&emsp;vid_src
  


1. 영상 데이터셋 수집
  AI Hub (https://www.aihub.or.kr/) : 장면인식‧인물인식을 위한 방송 영상 콘텐츠
