import json

from django.shortcuts import render
from .models import UrMaster, UrMbship, TrMbship
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views
from .serializers import TrMbshipListSerializer, UrMbshipSerializer
from django.db import connection


# 티켓리스트
@api_view(['POST'])
def ticket_list(request):

    try:
        # 사용자ID, 권한(회원) chk - JWT 적용 후 삭제될 IF 처리.
        if UrMaster.objects.filter(user_numb=request.data["user_numb"]).exists():

            userInfo = UrMaster.objects.get(user_numb=request.data["user_numb"])
            
            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userInfo.user_abcd == "A"):
                ticketInfo = ticketListDetailView("A", userInfo.user_numb)

                return Response(ticketInfo, status=200)

            elif(userInfo.user_abcd == "B"):
                # 강사 본인이 갖고있는 강사수업 LIST 조회
                ticketInfo = ticketListDetailView("B", userInfo.user_numb)

                return Response(ticketInfo, status=200)

            elif(userInfo.user_abcd == "C"):
                ticketInfo = ticketListDetailView("C", userInfo.user_numb)

                return Response(ticketInfo, status=200)
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


# 티켓 수정
@api_view(['POST'])
def update(request):

    try:
        # 회원권일련번호 여부 chk, 권한 chk
        if UrMbship.objects.filter(umem_numb=request.data["umem_numb"]).exists():
            
            urMbship = UrMbship.objects.get(umem_numb=request.data["umem_numb"])

            userInfo = UrMaster.objects.get(user_numb=urMbship.user_numb)
# 티켓 수정을 할 수 있는 권한 정해야할듯.

            # TODO JWT 토큰 연동시 강사수업일련번호 소유 여부 검증 로직 추가
#             if(trMbshipInfo.user_numb != request.data["user_numb"]):
#                return Response({'message': ''}, status=400) 

            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            # if(userInfo.user_abcd != "B"):
            #     return Response({'message': '티켓 생성 권한이 없습니다.'}, status=200)
        else:
            return Response({'message': '일치하는 강사수업일련번호가 없습니다.'}, status=200)

        # 회원권일련번호로 티켓 수정
        UrMbship.objects.filter(umem_numb=request.data["umem_numb"]).update(
            umem_stat=request.data["umem_stat"], # 회원권이용시작일자
            umem_endt=request.data["umem_endt"], # 회원권이용종료일자
            umem_tnum=request.data["umem_tnum"], # 회원권등록회차
            umem_unum=request.data["umem_unum"], # 회원권사용회차
            umem_ysno=request.data["umem_ysno"]  # 회원권사용가능여부
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
            return Response([], status=200)

    except KeyError:
        return Response({'message': 'KEY_ERROR'}, status=400)


# 강사수업 LIST 조회
def ticketListDetailView(user_gb, user_numb):

    cursor = connection.cursor()

# 회원권일련번호, 사용자일련번호(회원), 사용자ID(회원), 사용자명(회원), 강사수업일련번호, 강의명, 회원권이용시작일자, 회원권이용종료일자, 회원권등록회차, 회원권사용회차, 회원권사용가능여부, 사용자일련번호(강사), 사용자ID(강사), 사용자명(강사)
# membership_seq, user_member_seq, user_member_id, user_member_nm, class_seq, class_nm, membership_stat_date, membership_end_date, membership_join_number, membership_use_number, membership_use_yn, user_teach_seq, user_teach_id, user_teach_nm
    if (user_gb == "A"):
        strSql = '''SELECT Z.umem_numb as membership_seq, Z.user_numb as user_member_seq, Z.user_idxx as user_member_id, Z.user_name as user_member_nm, Z.tmem_numb as class_seq
                         , X.tmem_name as class_nm, Z.umem_stat as membership_stat_date, Z.umem_endt as membership_end_date, Z.umem_tnum as membership_join_number
                         , Z.umem_unum as membership_use_number, Z.umem_ysno as membership_use_yn, X.user_numb as user_teach_seq, X.user_numb as user_teach_id, X.user_name as user_teach_nm
                      FROM (SELECT A.umem_numb, A.user_numb, B.user_idxx, B.user_name, A.tmem_numb, A.umem_stat, A.umem_endt, A.umem_tnum, A.umem_unum, A.umem_ysno
                              FROM ur_mbship A, ur_master B 
                             WHERE A.user_numb = B.user_numb
                               AND A.user_numb = NVL((%s),A.user_numb)
                        ) Z
                        , (SELECT C.tmem_numb, C.tmem_name, C.user_numb, D.user_idxx, D.user_name 
                             FROM tr_mbship C, ur_master D 
                            WHERE C.user_numb = D.user_numb 
                        ) X 
                    WHERE Z.tmem_numb = X.tmem_numb'''
    elif (user_gb == "B"):
        strSql = '''SELECT Z.umem_numb as membership_seq, Z.user_numb as user_member_seq, Z.user_idxx as user_member_id, Z.user_name as user_member_nm, Z.tmem_numb as class_seq
                         , X.tmem_name as class_nm, Z.umem_stat as membership_stat_date, Z.umem_endt as membership_end_date, Z.umem_tnum as membership_join_number
                         , Z.umem_unum as membership_use_number, Z.umem_ysno as membership_use_yn, X.user_numb as user_teach_seq, X.user_numb as user_teach_id, X.user_name as user_teach_nm
                      FROM (SELECT A.umem_numb, A.user_numb, B.user_idxx, B.user_name, A.tmem_numb, A.umem_stat, A.umem_endt, A.umem_tnum, A.umem_unum, A.umem_ysno
                              FROM ur_mbship A, ur_master B 
                             WHERE A.user_numb = B.user_numb
                        ) Z
                        , (SELECT C.tmem_numb, C.tmem_name, C.user_numb, D.user_idxx, D.user_name 
                             FROM tr_mbship C, ur_master D 
                            WHERE C.user_numb = D.user_numb 
                              AND D.user_numb = NVL((%s),D.user_numb)
                        ) X 
                    WHERE Z.tmem_numb = X.tmem_numb'''
    elif (user_gb == "C"):
        strSql = '''Z.umem_numb as membership_seq, Z.user_numb as user_member_seq, Z.user_idxx as user_member_id, Z.user_name as user_member_nm, Z.tmem_numb as class_seq
                         , X.tmem_name as class_nm, Z.umem_stat as membership_stat_date, Z.umem_endt as membership_end_date, Z.umem_tnum as membership_join_number
                         , Z.umem_unum as membership_use_number, Z.umem_ysno as membership_use_yn, X.user_numb as user_teach_seq, X.user_numb as user_teach_id, X.user_name as user_teach_nm
                      FROM (SELECT A.umem_numb, A.user_numb, B.user_idxx, B.user_name, A.tmem_numb, A.umem_stat, A.umem_endt, A.umem_tnum, A.umem_unum, A.umem_ysno
                              FROM ur_mbship A, ur_master B 
                             WHERE A.user_numb = B.user_numb
                        ) Z
                        , (SELECT C.tmem_numb, C.tmem_name, C.user_numb, D.user_idxx, D.user_name 
                             FROM tr_mbship C, ur_master D 
                            WHERE C.user_orig = D.user_orig 
                              AND D.user_numb = NVL((%s),D.user_numb)
                        ) X 
                    WHERE Z.tmem_numb = X.tmem_numb'''
    
    params = [user_numb]
    
    with connection.cursor() as cursor:
        cursor.execute(strSql, params)
        queryset = dictfetchall(cursor)

    return queryset


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]