import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import TrMbship
from . import views

from .serializers import SelClassSerializer, NewClassSerializer, UpdateClassSerializer, DeleteClassSerializer
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response


# 수업권한권 조회
class ClassManagementAPI(APIView):
    @swagger_auto_schema(tags=['Class_Management'], operation_id='수업권한권 조회 API', operation_description='수업권한권 조회', responses={201: SelClassSerializer})
    def get(self, request):
        
        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        # 수업권한관리는 회원 접근 불가능
        if(userAbcd == "A"):
            return Response({'message': '회원은 접근 불가능합니다.'}, status=200)

        if TrMbship.objects.filter(user_numb=userNumb).exists():
            trMbshipInfo = TrMbship.objects.filter(user_numb=userNumb)
            serializer = SelClassSerializer(trMbshipInfo,many=True)
            return Response(serializer.data)

        else:
            return Response({'message': '일치하는 수업권한권이 없습니다.'}, status=200)


    @swagger_auto_schema(tags=['Class_Management'], operation_id='수업권한권 생성 API', operation_description='수업권한권 생성', request_body=NewClassSerializer, responses={201: 'OK'})
    def post(self, request):

        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        # 수업권한관리는 회원 접근 불가능
        if(userAbcd == "A"):
            return Response({'message': '회원은 접근 불가능합니다.'}, status=200)

        userInfo = UrMaster.objects.get(user_idxx=request.data["user_idxx"])

        # 수업권한권 생성
        TrMbship.objects.create(
            user_numb=userInfo.user_numb, # 사용자일련번호
            tmem_name=request.data["tmem_name"], # 수업명
            tmem_expl=request.data["tmem_expl"], # 수업장소
            tmem_cate=request.data["tmem_cate"], # 운동구분코드
            tmem_grop=request.data["tmem_grop"], # 개인/단체구분
            tmem_alr1=request.data["tmem_alr1"], # 기본예약확인알림시간
            tmem_alr2=request.data["tmem_alr2"], # 기본수강확정알림시간
            tmem_maxx=request.data["tmem_maxx"], # 기본정원
            tmem_wait=request.data["tmem_wait"], # 기본대기인원
            tmem_ysno="Y", # 강사수강권사용여부
        )
        return Response({'message': 'OK'}, status=201) 


    @swagger_auto_schema(tags=['Class_Management'], operation_id='수업권한권 수정 API', operation_description='수업권한권 수정', request_body=UpdateClassSerializer, responses={201: 'OK'})
    def put(self, request):

        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        tmemNumb = request.data["tmem_numb"] # 수업권한권일련번호

        # 수업권한관리는 회원 접근 불가능
        if(userAbcd == "A"):
            return Response({'message': '회원은 접근 불가능합니다.'}, status=200)

        # 수업권한권 일련번호 CHK
        if TrMbship.objects.filter(tmem_numb=tmemNumb).exists():
            trMbshipInfo = TrMbship.objects.get(tmem_numb=tmemNumb)

            # 해당 수업권한권의 강사와 수정 처리한 사용자 일련번호 CHK
            if(trMbshipInfo.user_numb != userNumb)
                return Response({'message': '수업권한권 수정 권한이 없습니다.'}, status=200)
            
            # 수업권한권 수정.
            TrMbship.objects.filter(tmem_numb=tmemNumb).update(
                tmem_name=request.data["tmem_name"], # 수업명
                tmem_expl=request.data["tmem_expl"], # 수업장소
                tmem_cate=request.data["tmem_cate"], # 운동구분코드
                tmem_grop=request.data["tmem_grop"], # 개인/단체구분
                tmem_alr1=request.data["tmem_alr1"], # 기본예약확인알림시간
                tmem_alr2=request.data["tmem_alr2"], # 기본수강확정알림시간
                tmem_maxx=request.data["tmem_maxx"], # 기본정원
                tmem_wait=request.data["tmem_wait"], # 기본대기인원
                tmem_ysno=request.data["tmem_ysno"], # 강사수강권사용여부
            )
            return Response({'message': 'OK'}, status=201) 

        else:
            return Response({'message': '일치하는 수업권한권이 없습니다.'}, status=200)


    @swagger_auto_schema(tags=['Class_Management'], operation_id='수업권한권 삭제 API', operation_description='수업권한권 삭제', request_body=DeleteClassSerializer, responses={201: 'OK'})
    def delete(self, request):

        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        tmemNumb = request.data["tmem_numb"] # 수업권한권일련번호

        # 수업권한관리는 회원 접근 불가능
        if(userAbcd == "A"):
            return Response({'message': '회원은 접근 불가능합니다.'}, status=200)

        # 수업권한권 일련번호 CHK
        if TrMbship.objects.filter(tmem_numb=tmemNumb).exists():
            trMbshipInfo = TrMbship.objects.get(tmem_numb=tmemNumb)

            # 해당 수업권한권의 강사와 삭제 처리한 사용자 일련번호 CHK
            if(trMbshipInfo.user_numb != userNumb)
                return Response({'message': '수업권한권 삭제 권한이 없습니다.'}, status=200)
            
            # 수업권한권 삭제.
            trMbshipInfo.delete()
            return Response({'message': 'OK'}, status=201) 

        else:
            return Response({'message': '일치하는 수업권한권이 없습니다.'}, status=200)