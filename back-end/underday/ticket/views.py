import json
import jwt

from django.shortcuts import render
from .models import UrMaster, UrMbship, TrMbship
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import views
from .serializers import TrMbshipListSerializer, UrMbshipSerializer, TicketListSerializer, TicketCreateSerializer, TicketUpdateSerializer
from django.db import connection
from drf_yasg.utils import swagger_auto_schema
from underday.settings import SECRET_KEY

# 티켓리스트
class TicketListAPI(APIView):
    @swagger_auto_schema(tags=['Ticket'], operation_id='티켓리스트 API', operation_description='티켓리스트', responses={201: TicketListSerializer})
    def get(self, request):
        
        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        # 사용자ID, 권한(회원) chk
        if UrMaster.objects.filter(user_numb=userNumb).exists():
            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userAbcd == "A"):
                ticketInfo = ticketListDetailView("A", userNumb)
                return Response(ticketInfo, status=200)

            elif(userAbcd == "B"):
                # 강사 본인이 갖고있는 강사수업 LIST 조회
                ticketInfo = ticketListDetailView("B", userNumb)
                return Response(ticketInfo, status=200)

            elif(userAbcd == "C"):
                ticketInfo = ticketListDetailView("C", userNumb)
                return Response(ticketInfo, status=200)
        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)

            
# 티켓생성
class TicketCreateAPI(APIView):
    @swagger_auto_schema(tags=['Ticket'], operation_id='티켓생성 API', operation_description='티켓생성',request_body=TicketCreateSerializer, responses={201: 'OK'})
    def post(self, request):

        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        userNumb = "" # 수강하려는 회원의 사용자ID 검증후 사용자일련번호 조회.

        # 강사수업일련번호 여부 chk, 권한 chk
        if TrMbship.objects.filter(tmem_numb=request.data['tmem_numb']).exists():
            
            trMbshipInfo = TrMbship.objects.get(tmem_numb=request.data["tmem_numb"])

            # 강사수업일련번호 소유 여부 검증 로직 추가
            if(trMbshipInfo.user_numb != userNumb):
               return Response({'message': '본인이 소유하고 있는 수업권한권이 아닙니다.'}, status=200) 

            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userAbcd != "B"):
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
            user_numb=userNumb, # 사용자일련번호(수강하려는 회원일련번호)
            tmem_numb=request.data["tmem_numb"], # 강사수업일련번호(수업권한권일련번호)
            umem_stat=request.data["umem_stat"], # 회원권이용시작일자
            umem_endt=request.data["umem_endt"], # 회원권이용종료일자
            umem_tnum=request.data["umem_tnum"], # 회원권등록회차
            umem_unum=request.data["umem_unum"], # 회원권사용회차
            umem_ysno="Y"  # 회원권사용가능여부
        )
        return Response({'message': 'OK'}, status=201)


# 티켓수정
class TicketUpdateAPI(APIView):
    @swagger_auto_schema(tags=['Ticket'], operation_id='티켓수정 API', operation_description='티켓수정', request_body=TicketUpdateSerializer, responses={201: 'OK'})
    def put(self, request):
        
        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        
        # 회원권일련번호 여부 chk, 권한 chk
        if UrMbship.objects.filter(umem_numb=request.data["umem_numb"]).exists():
            
            urMbship = UrMbship.objects.get(umem_numb=request.data["umem_numb"])

            trMbshipInfo = TrMbship.objects.get(tmem_numb=urMbship.tmem_numb)

            # 회원권의 회원이거나 강사인지 CHK
            if(userNumb != urMbship.user_numb or userNumb != trMbshipInfo.user_numb):
               return Response({'message': '회원권을 수정할 권한이 없습니다.'}, status=200) 

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


#  강사수업리스트 조회 API
class trMbshipListAPI(APIView):
    @swagger_auto_schema(tags=['Ticket'], operation_id='강사수업리스트 조회 API', operation_description='강사수업리스트 조회(회원구분 강사만 조회가능 - 티켓을 강사만 생성 가능하기 때문.)', responses={201: TrMbshipListSerializer})
    def get(self, request):
        
        # access token을 decode 해서 유저 id 추출 => 유저 식별
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        userNumb = payload.get('user_numb') # 사용자 일련번호
        userAbcd = payload.get('user_abcd') # 사용자 회원구분(A:회원, B:강사, C:기업)

        # 강사토큰의 사용자일련번호 CHK, 권한 CHK
        if UrMaster.objects.filter(user_numb=userNumb).exists():
            # user_abcd 회원구분(A:회원, B:강사, C:기업)
            if(userAbcd != "B"):
                return Response({'message': '조회권한이 없습니다.'}, status=200)
        else:
            return Response({'message': '일치하는 ID가 없습니다.'}, status=200)
            
        # 강사 본인이 갖고있는 강사수업 LIST 조회
        if TrMbship.objects.filter(user_numb=userNumb).exists():
            TrMbshipList = TrMbship.objects.filter(user_numb=userNumb)
            serializer = TrMbshipListSerializer(TrMbshipList,many=True)
            return Response(serializer.data, status=200)

        else: 
            return Response([], status=200)

# 강사수업 LIST 조회
def ticketListDetailView(user_gb, user_numb):
    cursor = connection.cursor()

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