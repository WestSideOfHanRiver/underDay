import json

from django.shortcuts import render
from .models import UrMbship
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views



# 티켓리스트
@api_view(['POST'])
def ticket_list(request):
    try:
        
        if UrMbship.objects.filter(user_numb=request.data["user_numb"]).exists():
            
            ticketInfo = UrMbship.objects.get(user_numb=request.data["user_numb"])

        # umem_numb : "string”, — 티켓일련번호
        # umem_stat : "string”, — 회원권이용시작일시
        # umem_endt : "string”, — 회원권이용종료일시
        # tmem_numb : "string", - 강사수업일련번호
        # umem_tnum : "string”, — 회원권등록회차
        # umem_unum : "string”, — 회원권사용회차
        # umem_ysno : "string”, — 회원권사용가능여부
        # umem_inst : "string”, — 회원권등록일시

            return Response({'umem_numb': ticketInfo.umem_numb
                            ,'umem_stat': ticketInfo.umem_stat
                            ,'umem_endt': ticketInfo.umem_endt
                            ,'tmem_numb': ticketInfo.tmem_numb
                            ,'umem_tnum': ticketInfo.umem_tnum
                            ,'umem_unum': ticketInfo.umem_unum
                            ,'umem_ysno': ticketInfo.umem_ysno
                            ,'umem_inst': ticketInfo.umem_inst}, status=200)

        else :
            return Response({'message': '일치하는 ID가 없습니다.'}, status=401)
    
        return Response({'message': 'SUCCESS'}, status=201)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


# 티켓생성
@api_view(['POST'])
def create(request):
    try:
        # 입력 생성 전 필수입력체크
            # TMEM_NUMB '강사수업일련번호' 

        if UrMaster.objects.filter(user_idxx=request.data['user_idxx']).exists():
            return Response({'message': 'INVAILD_USERS'}, status=401)

        # 티켓생성
        UrMbship.objects.create(
            umem_stat=request.data["umem_stat"],
            umem_endt=request.data["umem_endt"],
            tmem_numb=request.data["tmem_numb"],
            umem_tnum=request.data["umem_tnum"],
            umem_unum=request.data["umem_unum"],
            umem_ysno=request.data["umem_ysno"],
            umem_inst=request.data["umem_inst"]
        )
    
        return Response({'message': 'SUCCESS'}, status=201)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)

        
# 티켓 조회, 추가
@api_view(['GET','POST'])
def ticket(request):

    try:
        if(request.method == 'GET'):

            user_numb = request.GET['userId']

            if UrMbship.objects.filter(user_numb=user_numb).exists():
                
                ticketInfo = UrMbship.objects.get(user_numb=user_numb)

            # umem_numb : "string”, — 티켓일련번호
            # umem_stat : "string”, — 회원권이용시작일시
            # umem_endt : "string”, — 회원권이용종료일시
            # tmem_numb : "string", - 강사수업일련번호
            # umem_tnum : "string”, — 회원권등록회차
            # umem_unum : "string”, — 회원권사용회차
            # umem_ysno : "string”, — 회원권사용가능여부
            # umem_inst : "string”, — 회원권등록일시

                return Response({'umem_numb': ticketInfo.umem_numb
                                ,'umem_stat': ticketInfo.umem_stat
                                ,'umem_endt': ticketInfo.umem_endt
                                ,'tmem_numb': ticketInfo.tmem_numb
                                ,'umem_tnum': ticketInfo.umem_tnum
                                ,'umem_unum': ticketInfo.umem_unum
                                ,'umem_ysno': ticketInfo.umem_ysno}, status=200)

            else :
                return Response({'message': '일치하는 ID가 없습니다.'}, status=401)

        elif(request.method == 'POST'):
            
            # 티켓생성
            UrMbship.objects.create(
                umem_stat=request.data["umem_stat"],
                umem_endt=request.data["umem_endt"],
                tmem_numb=request.data["tmem_numb"],
                umem_tnum=request.data["umem_tnum"],
                umem_unum=request.data["umem_unum"],
                umem_ysno=request.data["umem_ysno"]
            )
            
            return Response({'message': 'SUCCESS'}, status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)