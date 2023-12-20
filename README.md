\_Day

<<<<<<< HEAD
| <img src="https://avatars.githubusercontent.com/u/60081286?s=96&v=4" width="100" height="100" /> | <img src="https://avatars.githubusercontent.com/u/127229564?s=96&v=4" width="100" height="100" /> | <img src="https://avatars.githubusercontent.com/u/87363088?s=96&v=4" width="100" height="100" /> | <img src="https://avatars.githubusercontent.com/u/84326278?s=96&v=4" width="100" height="100" /> |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| 조완석                                                                                           | 김도완                                                                                            | 김부건                                                                                           | 진가영                                                                                           |
=======
| <img src="https://avatars.githubusercontent.com/u/60081286?s=96&v=4" width="100" height="100" /> | <img src="https://avatars.githubusercontent.com/u/127229564?s=96&v=4" width="100" height="100" /> | <img src="https://avatars.githubusercontent.com/u/87363088?s=96&v=4" width="100" height="100" /> | <img src="https://avatars.githubusercontent.com/u/84326278?s=96&v=4" width="100" height="100" /> |<img src="https://avatars.githubusercontent.com/u/43087664?s=64&v=4" width="100" height="100" /> |
|:---:|:---:|:---:|:---:|:---:|
|조완석|김도완|김부건|진가영|최흥수|
# 모두 화이팅!

### django 셋팅 전에 가상환경 설정 필요, 
1. (가상환경 없을때만)python -m venv myvenv

## 항상 가상환경 키고 시작
win - source myvenv/Scripts/activate 
mac - source myvenv/bin/activate 
## 가상환경 끌때
deactivate
## 기본셋팅
1. 버전관리 $ pip freeze > requirements.txt
2. 버전관리파일 설치 $ pip install -r requirements.txt


## model변동에, 데이터베이스 연동에 해야하는것들
mac - python -> python3
1. $ python manage.py makemigrations  -> app의 모델 변경 사항을 체크
2. $ python manage.py migrate -> 변경사항을 DB에 반영
3. $ python manage.py inspectdb > models.py  ->mariadb를 models.py 생성


## 서버실행
1. (manage.py 경로에서)python manage.py runserver

>>>>>>> origin
