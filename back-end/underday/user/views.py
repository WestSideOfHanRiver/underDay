import json
import bcrypt

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse
from .models import UrMaster
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from . import views

# 회원가입
@csrf_exempt
@api_view(['POST'])
def signup(request):
    try:
        # 필수 입력값 회원구분(회원, 강사, 기업)에 따라 입력
        # exists() 중복 record 찾는 함수
        if UrMaster.objects.filter(user_idxx=request.data['user_idxx']).exists():
            return Response({'message': 'INVAILD_USERS'}, status=200)

        if request.data["password1"] != request.data["password2"]:
            return Response({'message': 'INVAILD_USERS'}, status=200)


        # 비밀번호 암호화
        hashed_password = bcrypt.hashpw(
            request.data["password1"].encode('utf-8'), bcrypt.gensalt())
        decoded_password = hashed_password.decode('utf-8')
        
        ## user_abcd 회원구분(A:회원, B:강사, C:기업)
        if(request.data["user_abcd"] == "A"):

            UrMaster.objects.create(
                user_idxx=request.data["user_idxx"],
                user_pasw=decoded_password,
                user_phon=request.data["user_phon"],
                user_name=request.data["user_name"],
                user_abcd=request.data["user_abcd"],
                user_pwer=0,
                user_rptt="Y",
                user_sumo="SUN"
            )
        
        elif(request.data["user_abcd"] == "B"):

            UrMaster.objects.create(
                user_idxx=request.data["user_idxx"],
                user_pasw=decoded_password,
                user_phon=request.data["user_phon"],
                user_name=request.data["user_name"],
                user_abcd=request.data["user_abcd"], #사용자구분 (회원,강사, 기업(A,B,C 알파벳 한자리)
                user_pwer=0,
                user_rptt="Y",
                user_sumo="SUN",
                user_orig=request.data["user_orig"], #소속명
            )

        elif(request.data["user_abcd"] == "C"):

            UrMaster.objects.create(
                user_idxx=request.data["user_idxx"],
                user_pasw=decoded_password,
                user_phon=request.data["user_phon"],
                user_name=request.data["user_name"],
                user_abcd=request.data["user_abcd"], #사용자구분 (회원,강사, 기업(A,B,C 알파벳 한자리)
                user_pwer=0,
                user_rptt="Y",
                user_sumo="SUN",
                user_orig=request.data["user_orig"], #소속명
                user_conb=request.data["user_conb"], #사업자등록번호
                user_add1=request.data["user_add1"], #우편번호
                user_add2=request.data["user_add2"], #주소
            )
            
        else:
            return Response({'message': 'INVAILD_USERS'}, status=401)

        return Response({'message': 'OK'}, status=201)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


# 로그인 ID, PW 로 로그인시.
# JWT Access Token 15m, 7day
# 로그인
@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication,))
def login(request):
    try:

        # 아이디 검증 - PYTHON에서 선처리하는 공간 or JWT 검증하는 공간에서 아이디 검증하므로 제외될 예정.
        if UrMaster.objects.filter(user_idxx=request.data["user_idxx"]).exists():
            
            userInfo = UrMaster.objects.get(user_idxx=request.data["user_idxx"])

            # 비밀번호 오류 count 체크
            # 5회 이상이면 휴대폰 인증 추가!
            if(userInfo.user_pwer > 5):
                return Response({'message': '비밀번호 5회 이상 오류!!. 휴대폰번호를 인증해주세요.'}, status=200)
            
            # PW 검증
            # db에 저장된 암호화 PW == 입력받고 암호화된 PW 비교
            if bcrypt.checkpw(request.data['password'].encode('utf-8'), userInfo.user_pasw.encode('utf-8')) == True:
                return Response({'message': 'OK'}, status=200)
            else:
                # 비밀번호 오류 count 추가
                userPwer = userInfo.user_pwer + 1

                UrMaster.objects.filter(user_idxx=request.data["user_idxx"]).update(user_pwer=userPwer)
                
                return Response({'message': '비밀번호 오류!!'}, status=200)
        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


# 아이디 중복 체크 API
@csrf_exempt
@api_view(['POST'])
def chkUserId(request):
    try:
        if UrMaster.objects.filter(user_idxx=request.data["user_idxx"]).exists():
            return Response({'message': '중복된 ID입니다.'}, status=200)
        else:
            return Response({'message': 'OK'}, status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


# 마이페이지 조회, 추가, 수정, 삭제
@api_view(['GET','POST','DELETE'])
def mypage(request):
    try:
        if(request.method == 'GET'):
            return Response({'message': 'OK'}, status=200)

        elif(request.method == 'POST'):
            return Response({'message': 'OK'}, status=200)

        elif(request.method == 'DELETE'):
            return Response({'message': 'OK'}, status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)

## 임시 API - 로직만 구현. JWT 구현 후 수정 예정

# 마이페이지 조회
@api_view(['POST'])
def mypageSel(request):
    try:
        # 사용자일련번호 CHK
        if UrMaster.objects.filter(user_numb=request.data['user_numb']).exists():
            
            userInfo = UrMaster.objects.get(user_numb=request.data["user_numb"])
        
            ## user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userInfo.user_abcd == "A"):

                return Response({'user_idxx': userInfo.user_idxx # 사용자ID
                                ,'user_name': userInfo.user_name # 사용자명
                                ,'user_phon': userInfo.user_phon # 사용자휴대폰번호
                                ,'user_abcd': userInfo.user_abcd # 사용자구분
                                ,'user_tknm': userInfo.user_tknm # 사용자토큰키명
                                ,'user_nick': userInfo.user_nick # 사용자닉네임
                                ,'user_sumo': userInfo.user_sumo # 달력시작요일
                                ,'user_pref': userInfo.user_pref # 선호운동
                                ,'user_memo': userInfo.user_memo # 메모
                                }, status=200)
            
            elif(userInfo.user_abcd == "B"):
                
                return Response({'user_idxx': userInfo.user_idxx # 사용자ID
                                ,'user_name': userInfo.user_name # 사용자명
                                ,'user_phon': userInfo.user_phon # 사용자휴대폰번호
                                ,'user_abcd': userInfo.user_abcd # 사용자구분
                                ,'user_tknm': userInfo.user_tknm # 사용자토큰키명
                                ,'user_nick': userInfo.user_nick # 사용자닉네임
                                ,'user_sumo': userInfo.user_sumo # 달력시작요일
                                ,'user_pref': userInfo.user_pref # 선호운동
                                ,'user_memo': userInfo.user_memo # 메모
                                ,'user_orig': userInfo.user_orig # 소속명
                                }, status=200)

            elif(userInfo.user_abcd == "C"):
                
                return Response({'user_idxx': userInfo.user_idxx # 사용자ID
                                ,'user_name': userInfo.user_name # 사용자명
                                ,'user_phon': userInfo.user_phon # 사용자휴대폰번호
                                ,'user_abcd': userInfo.user_abcd # 사용자구분
                                ,'user_tknm': userInfo.user_tknm # 사용자토큰키명
                                ,'user_nick': userInfo.user_nick # 사용자닉네임
                                ,'user_sumo': userInfo.user_sumo # 달력시작요일
                                ,'user_pref': userInfo.user_pref # 선호운동
                                ,'user_memo': userInfo.user_memo # 메모
                                ,'user_orig': userInfo.user_orig # 소속명
                                ,'user_conb': userInfo.user_conb # 사업자등록번호
                                ,'user_add1': userInfo.user_add1 # 우편번호
                                ,'user_add2': userInfo.user_add2 # 주소
                                }, status=200)
                
            return Response({'message': 'OK'}, status=200)  

        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


# 마이페이지 수정
@api_view(['POST'])
def mypageUpdate(request):
    try:
        # 사용자일련번호 CHK
        if UrMaster.objects.filter(user_numb=request.data['user_numb']).exists():
            
            userInfo = UrMaster.objects.filter(user_numb=request.data["user_numb"])
        
            ## user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userInfo.user_abcd == "A"):
                UrMaster.objects.filter(user_numb=request.data["user_numb"]).update(
                    user_nick=request.data["user_nick"], #닉네임
                    user_sumo=request.data["user_sumo"], #달력시작요일
                    user_pref=request.data["user_pref"], #선호운동
                    user_memo=request.data["user_memo"], #메모
                )
            
            elif(userInfo.user_abcd == "B"):
                UrMaster.objects.filter(user_numb=request.data["user_numb"]).update(
                    user_nick=request.data["user_nick"], #닉네임
                    user_sumo=request.data["user_sumo"], #달력시작요일
                    user_pref=request.data["user_pref"], #선호운동
                    user_memo=request.data["user_memo"], #메모
                    user_orig=request.data["user_orig"], #소속명
                )

            elif(userInfo.user_abcd == "C"):
                UrMaster.objects.filter(user_numb=request.data["user_numb"]).update(
                    user_nick=request.data["user_nick"], #닉네임
                    user_sumo=request.data["user_sumo"], #달력시작요일
                    user_pref=request.data["user_pref"], #선호운동
                    user_memo=request.data["user_memo"], #메모
                    user_orig=request.data["user_orig"], #소속명
                    user_conb=request.data["user_conb"], #사업자등록번호
                    user_add1=request.data["user_add1"], #우편번호
                    user_add2=request.data["user_add2"], #주소
                )
            
            return Response({'message': 'OK'}, status=201) 

        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)