import json
import bcrypt

from django.shortcuts import render, redirect
from .models import UrMaster
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views



# 회원가입
@csrf_exempt
@api_view(['POST'])
def signup(request):
    try:

        # 필수 입력값 회원구분(회원, 강사, 기업)에 따라 입력
        # exists() 중복 record 찾는 함수
        if UrMaster.objects.filter(user_numb=request.data['user_numb']).exists():
            return Response({'message': 'INVAILD_USERS'}, status=401)

        if request.data["password1"] != request.data["password2"]:
            return Response({'message': 'INVAILD_USERS'}, status=401)

        
        ## 필수 입력값 모두 체크 후 회원가입 진행

        # 비밀번호 암호화
        hashed_password = bcrypt.hashpw(
            request.data["password1"].encode('utf-8'), bcrypt.gensalt())
        decoded_password = hashed_password.decode('utf-8')
        
        # 회원가입
        UrMaster.objects.create(
            user_numb=request.data["user_numb"],
            user_pasw=decoded_password,
            #user_pasw=request.data["password1"],
            user_phon=request.data["user_phon"],
            user_name=request.data["user_name"],
            user_abcd=request.data["user_abcd"] #사용자구분 (회원,강사, 기업(A,B,C 알파벳 한자리)
            #USER_ORIG=data.POST['user_orig'], #소속명
            #USER_ADDR=data.POST['user_addr'], #도로명주소
        )
    
        return Response({'message': 'SUCCESS'}, status=200)
        #return Response(data, status=200)

    except KeyError:
       return Response({'message': 'KEY_ERROR'}, status=400)




# 로그인 ID, PW 로 로그인시.
# JWT Access Token 15m, 7day
@csrf_exempt
@api_view(['POST'])
def login(request):

    try:
        # 로그인 경로마다 다르게 해야할듯 ?
        # 네이버 로그인, 아이디로 로그인,


        print(request.data["user_numb"])
        print(request.data["password"])

        # 아이디 검증
        if UrMaster.objects.filter(user_numb=request.data["user_numb"]).exists():
            
            user = UrMaster.objects.get(user_numb=request.data["user_numb"])
            # 비밀번호 오류 count 체크
            # 5회 이상이면 휴대폰 인증 추가!
            
            # PW 검증
            # db에 저장된 암호화 PW == 입력받고 암호화된 PW 비교
            if bcrypt.checkpw(request.data['password'].encode('utf-8'), user.user_pasw.encode('utf-8')) == True:
                return Response({'message': 'SUCCESS'}, status=200)
            else :
                # 비밀번호 오류 count 추가
                print("비밀번호 오류!!")
                print(decoded_password)
                print(user.user_pasw)
                return Response({'message': '비밀번호 오류!!'}, status=401)

        else :
            return Response({'message': '일치하는 ID가 없습니다.'}, status=401)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)