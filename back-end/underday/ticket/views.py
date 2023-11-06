import json

from django.shortcuts import render
from .models import UrMaster, UrMbship, TrMbship
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views
from .serializers import TrMbshipListSerializer, UrMbshipSerializer



# 티켓리스트
@api_view(['POST'])
def ticket_list(request):

    try:
        # 사용자ID, 권한(회원) chk - JWT 적용 후 삭제될 IF 처리.
        if UrMaster.objects.filter(user_numb=request.data["user_numb"]).exists():

            userInfo = UrMaster.objects.get(user_numb=request.data["user_numb"])
            
            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userInfo.user_abcd == "A"):
                
                ticketInfo = UrMbship.objects.filter(user_numb=userInfo.user_numb)

                serializer = UrMbshipSerializer(ticketInfo,many=True)

                return Response(serializer.data, status=200)
                # return Response([{'umem_numb': ticketInfo.umem_numb # 회원권일련번호
                #                 ,'user_numb': ticketInfo.user_numb # 사용자일련번호
                #                 ,'tmem_numb': ticketInfo.tmem_numb # 강사수업일련번호
                #                 ,'umem_stat': ticketInfo.umem_stat # 회원권이용시작일자
                #                 ,'umem_endt': ticketInfo.umem_endt # 회원권이용종료일자
                #                 ,'umem_tnum': ticketInfo.umem_tnum # 회원권등록회차
                #                 ,'umem_unum': ticketInfo.umem_unum # 회원권사용회차
                #                 ,'umem_ysno': ticketInfo.umem_ysno # 회원권사용가능여부
                #                 }], status=200)

            elif(userInfo.user_abcd == "B"):
                
                # 강사 본인이 갖고있는 강사수업 LIST 조회
                trMbshipList = TrMbship.objects.filter(user_numb=userInfo.user_numb)

                # TODO 강사가 소유하고 있는 강사수업일련번호 다건일 경우 오류 날듯 개선 필요
                ticketInfo = UrMbship.objects.filter(tmem_numb=trMbshipList.tmem_numb)
                
                serializer = UrMbshipSerializer(ticketInfo,many=True)

                return Response(serializer.data, status=200)
                # return Response([{'umem_numb': ticketInfo.umem_numb # 회원권일련번호
                #                 ,'user_numb': ticketInfo.user_numb # 사용자일련번호
                #                 ,'tmem_numb': ticketInfo.tmem_numb # 강사수업일련번호
                #                 ,'umem_stat': ticketInfo.umem_stat # 회원권이용시작일자
                #                 ,'umem_endt': ticketInfo.umem_endt # 회원권이용종료일자
                #                 ,'umem_tnum': ticketInfo.umem_tnum # 회원권등록회차
                #                 ,'umem_unum': ticketInfo.umem_unum # 회원권사용회차
                #                 ,'umem_ysno': ticketInfo.umem_ysno # 회원권사용가능여부
                #                 }], status=200)

            elif(userInfo.user_abcd == "C"):
                # TODO 기업일 경우 리스트 조회 추가 예정
                # return Response(serializer.data, status=200)
                return Response({'message': '기업의 티켓 리스트 조회 API는 추가 예정입니다.'}, status=200)
        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


# 티켓생성
@api_view(['POST'])
def create(request):

    try:
        userNumb = ""

        # 강사수업일련번호 여부 chk, 권한 chk
        if TrMbship.objects.filter(tmem_numb=request.data['tmem_numb']).exists():
            
            trMbshipInfo = TrMbship.objects.get(tmem_numb=request.data["tmem_numb"])

            # TODO JWT 토큰 연동시 강사수업일련번호 소유 여부 검증 로직 추가
#             if(trMbshipInfo.user_numb != request.data["user_numb"]):
#                return Response({'message': ''}, status=400) 

            userInfo = UrMaster.objects.get(user_numb=trMbshipInfo.user_numb)

            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userInfo.user_abcd != "B"):
                return Response({'message': '티켓 생성 권한이 없습니다.'}, status=200)
        else:
            return Response({'message': '일치하는 강사수업일련번호가 없습니다.'}, status=200)

        # 회원ID 유효여부 체크
        if UrMaster.objects.filter(user_idxx=request.data['user_idxx']).exists():
            userInfo = UrMaster.objects.get(user_idxx=request.data['user_idxx'])

            # 수강하려는 회원ID의 일련번호 조회
            userNumb = userInfo.user_numb
        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)

        # 티켓생성
        UrMbship.objects.create(
            user_numb=userNumb, # 사용자일련번호
            tmem_numb=request.data["tmem_numb"], # 강사수업일련번호
            umem_stat=request.data["umem_stat"], # 회원권이용시작일자
            umem_endt=request.data["umem_endt"], # 회원권이용종료일자
            umem_tnum=request.data["umem_tnum"], # 회원권등록회차
            umem_unum=request.data["umem_unum"], # 회원권사용회차
            umem_ysno="Y"  # 회원권사용가능여부
        )
        return Response({'message': 'OK'}, status=201)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


#  강사수업리스트 조회 API
@csrf_exempt
@api_view(['POST'])
def trMbshipList(request):

    try:
        # 강사토큰의 사용자일련번호 CHK, 권한 CHK
        if UrMaster.objects.filter(user_numb=request.data['user_numb']).exists():
            
            userInfo = UrMaster.objects.get(user_numb=request.data["user_numb"])
            
            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userInfo.user_abcd != "B"):
                return Response({'message': '조회권한이 없습니다.'}, status=200)
        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)
            
            
        # 강사 본인이 갖고있는 강사수업 LIST 조회
        if TrMbship.objects.filter(user_numb=request.data['user_numb']).exists():
            
            TrMbshipList = TrMbship.objects.filter(user_numb=request.data['user_numb'])
    
            serializer = TrMbshipListSerializer(TrMbshipList,many=True)

            return Response(serializer.data, status=200)

        else: 
            return Response({'tmem_numb': '' # 강사수업일련번호
                            ,'tmem_name': '' # 강의명
                            ,'tmem_expl': '' # 강의실명
                            }, status=400)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)