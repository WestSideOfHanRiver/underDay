import json
import bcrypt

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import UrMaster
from . import views

from .serializers import UserSignupSerializer, UserChkSerializer, UserLoginSerializer, MypageSelSerializer, MypageUpdateSerializer
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.jwt_claim_serializer import MyTokenObtainPairSerializer

# 회원가입
@permission_classes([AllowAny]) #모든 사용자 접근가능
class UserSignupAPI(APIView):
    @swagger_auto_schema(tags=['User'], operation_id='회원가입 API', operation_description='회원가입', request_body=UserSignupSerializer, responses={201: 'OK'})
    def post(self, request):
        # 필수 입력값 회원구분(회원, 강사, 기업)에 따라 입력
        # exists() 중복 record 찾는 함수
        if UrMaster.objects.filter(user_idxx=request.data['user_idxx']).exists():
            return Response({'message': 'INVAILD_USERS'}, status=200)

        # 휴대폰번호 PK로 중복 체크
        # 하나의 번호로 여러개 프로필 생성 가능(아이디 별도 입력)

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
                user_conb=request.data["user_conb"], #사업자등록번호
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

    
# 로그인 ID, PW 로 로그인시.
@permission_classes([AllowAny]) #모든 사용자 접근가능
class UserLoginAPI(APIView):
    @swagger_auto_schema(tags=['User'], operation_id='로그인 API', operation_description='JWT 토큰 없이 모든 사용자 접근 가능', request_body=UserLoginSerializer, responses={201: 'OK'})
    def post(self, request):
        # 아이디 검증
        if UrMaster.objects.filter(user_idxx=request.data["user_idxx"]).exists():
            
            userInfo = UrMaster.objects.filter(user_idxx=request.data["user_idxx"]).first()

            # 비밀번호 오류 count 체크
            # 5회 이상이면 휴대폰 인증 추가!
            if(userInfo.user_pwer > 5):
                return Response({'message': '비밀번호 5회 이상 오류!!. 휴대폰번호를 인증해주세요.'}, status=200)
            
            # PW 검증
            # db에 저장된 암호화 PW == 입력받고 암호화된 PW 비교
            if bcrypt.checkpw(request.data['password'].encode('utf-8'), userInfo.user_pasw.encode('utf-8')) == True:
                token = MyTokenObtainPairSerializer.get_token(userInfo) # refresh 토큰 생성
                refresh_token = str(token) # refresh 토큰 문자열화
                access_token = str(token.access_token) # access 토큰 문자열화
                response = Response({"message": "OK"}, status=200)

                # JWT 토큰 => 쿠키에 저장
                response.set_cookie("access", access_token, httponly=True)
                response.set_cookie("refresh", refresh_token, httponly=True)

                return response
            else:
                # 비밀번호 오류 count 추가
                userPwer = userInfo.user_pwer + 1

                UrMaster.objects.filter(user_idxx=request.data["user_idxx"]).update(user_pwer=userPwer)
                
                return Response({'message': '비밀번호 오류!!'}, status=200)
        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)


# 아이디 중복 체크 API
@permission_classes([AllowAny]) #모든 사용자 접근가능
class ChkUserAPI(APIView):
    @swagger_auto_schema(tags=['User'], operation_id='아이디 중복 체크 API', operation_description='JWT 토큰 없이 모든 사용자 접근 가능', request_body=UserChkSerializer, responses={201: 'OK'})
    def post(self, request):
        if UrMaster.objects.filter(user_idxx=request.data["user_idxx"]).exists():
            return Response({'message': '중복된 ID입니다.'}, status=200)
        else:
            return Response({'message': 'OK'}, status=200)


# 마이페이지 조회
class MypageSelAPI(APIView):
    @swagger_auto_schema(tags=['Mypage'], operation_id='마이페이지 조회 API', operation_description='마이페이지 조회', responses={201: MypageSelSerializer})
    def get(self, request):
        
        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        # 사용자일련번호 CHK
        if UrMaster.objects.filter(user_numb=userNumb).exists():
            userInfo = UrMaster.objects.get(user_numb=request.data["user_numb"])

            ## user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userAbcd == "A"):
                return Response({'user_idxx': userInfo.user_idxx # 사용자ID
                                ,'user_name': userInfo.user_name # 사용자명
                                ,'user_phon': userInfo.user_phon # 사용자휴대폰번호
                                ,'user_abcd': userInfo.user_abcd # 사용자구분
                                ,'user_nick': userInfo.user_nick # 사용자닉네임
                                ,'user_sumo': userInfo.user_sumo # 달력시작요일
                                ,'user_pref': userInfo.user_pref # 선호운동
                                ,'user_memo': userInfo.user_memo # 메모
                                }, status=200)

            elif(userAbcd == "B"):
                return Response({'user_idxx': userInfo.user_idxx # 사용자ID
                                ,'user_name': userInfo.user_name # 사용자명
                                ,'user_phon': userInfo.user_phon # 사용자휴대폰번호
                                ,'user_abcd': userInfo.user_abcd # 사용자구분
                                ,'user_nick': userInfo.user_nick # 사용자닉네임
                                ,'user_sumo': userInfo.user_sumo # 달력시작요일
                                ,'user_pref': userInfo.user_pref # 선호운동
                                ,'user_memo': userInfo.user_memo # 메모
                                ,'user_orig': userInfo.user_orig # 소속명
                                }, status=200)

            elif(userAbcd == "C"):
                return Response({'user_idxx': userInfo.user_idxx # 사용자ID
                                ,'user_name': userInfo.user_name # 사용자명
                                ,'user_phon': userInfo.user_phon # 사용자휴대폰번호
                                ,'user_abcd': userInfo.user_abcd # 사용자구분
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
            

# 마이페이지 수정
class MypageUpdateAPI(APIView):
    @swagger_auto_schema(tags=['Mypage'], operation_id='마이페이지 수정 API', operation_description='마이페이지 수정', request_body=MypageUpdateSerializer, responses={201: 'OK'})
    def post(self, request):

        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        # 사용자일련번호 CHK
        if UrMaster.objects.filter(user_numb=userNumb).exists():
        
            ## user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userAbcd == "A"):
                UrMaster.objects.filter(user_numb=userNumb).update(
                    user_nick=request.data["user_nick"], #닉네임
                    user_sumo=request.data["user_sumo"], #달력시작요일
                    user_pref=request.data["user_pref"], #선호운동
                    user_memo=request.data["user_memo"], #메모
                )
            
            elif(userAbcd == "B"):
                UrMaster.objects.filter(user_numb=userNumb).update(
                    user_nick=request.data["user_nick"], #닉네임
                    user_sumo=request.data["user_sumo"], #달력시작요일
                    user_pref=request.data["user_pref"], #선호운동
                    user_memo=request.data["user_memo"], #메모
                    user_orig=request.data["user_orig"], #소속명
                )

            elif(userAbcd == "C"):
                UrMaster.objects.filter(user_numb=userNumb).update(
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
