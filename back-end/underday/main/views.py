from django.shortcuts import render, redirect
from .models import UrMaster,UrMbship, TrMbship, TrClass, ReMaster
from .serializers import UrMasterSerializer,TrClassSerializer,TrMbshipSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.db import connection
from django.http import HttpResponse

@csrf_exempt
@api_view(['GET'])
def user_list(request):
    users = UrMaster.objects.all()
    serializer = UrMasterSerializer(users,many=True)
    return Response(serializer.data)


# ######################    SQL을 사용한 class_list 함수   ###########################
# @csrf_exempt
# @api_view(['GET'])
# def class_list(request):
#     data = request.data
#     Nick = data['nick']
#     date = data['date']
#     time = data['time']
#     sql_query = '''SELECT 
#     A.USER_NUMB, 
#     A.USER_NAME,
#     A.USER_NICK,
#     B.UMEM_NUMB,
#     B.TMEM_NUMB,
#     C.CLAS_NUMB,
#     C.CLAS_DATE,
#     C.CLAS_TIME
#     FROM ur_master A
#     LEFT JOIN ur_mbship B ON A.USER_NUMB = B.USER_NUMB
#     LEFT JOIN tr_class C ON B.TMEM_NUMB = C.TMEM_NUMB
#     WHERE A.USER_NICK = %s AND C.CLAS_DATE = %s AND C.CLAS_TIME >= %s ''' 

#     params = [Nick,date,time]


#     # 원시 SQL 쿼리를 실행합니다.
#     with connection.cursor() as cursor:
#         cursor.execute(sql_query)

#         # 쿼리 결과를 가져옵니다.
#         queryset = cursor.fetchall()   

#     return Response(queryset)



# 제목 : 캘린더 메인페이지  
# 로직 : 월/일 에 해당하는 모든 데이터, 수강가능한 일정
# 요청 : id, date, time
# 리턴 : 수강가능 강의 리스트
# id, date20230303, time1430
# ur_master -> ur_mbship -> tr_class
######################    Serializer 사용한 class_list 함수   ###########################
# API : http://127.0.0.1:8000/classlist/
@csrf_exempt
@api_view(['GET'])
def class_list(request):
    usernumb = request.GET.get('usernumb', None)
    date = request.GET.get('date', None)

    # 현재시간 이후에 보이는건 나중에 시간 데이터 추가

    mbsh_ob = UrMbship.objects.filter(user_numb=usernumb)# 유저 맴버쉽 가져오기
    accumulated_queryset = [] # 쿼리셋 쌓을곳

    sql_query = '''SELECT 
    A.clas_list,
    A.clas_numb,
    A.clas_date,
    A.clas_time,
    A.clas_clos,
    A.clas_nmax,
    A.clas_wait,
    A.resv_stat,
    A.resv_last,
    A.resv_alr1,
    A.clas_ysno,
    A.clas_inst,
    A.clas_updt,
    A.tmem_numb
    FROM tr_class A
    LEFT JOIN tr_mbship B ON A.tmem_numb = B.tmem_numb
    AND A.tmem_numb = B.tmem_numb
    WHERE A.clas_date = %s ''' 
    
    params = [date]
    
    with connection.cursor() as cursor:
        cursor.execute(sql_query, params)
        queryset = cursor.fetchall()
        accumulated_queryset += queryset
    
    # print(accumulated_queryset)

    return Response(accumulated_queryset)

######################################################################################3

# 제목 : 예약버튼 이벤트
# 로직 : 예약하기, 예약 취소하기
# 요청 : 수강번호, 요청자id
# 리턴 : ok,error

# API : http://127.0.0.1:8000/classrequest/
# 
# 예약일련번호 resv_numb, 수업개설일련번호 CLAS_NUMB,수업날짜 CLAS_DATE, 회원권 일련번호 UMEM_NUMB , reserve_status 현재 예약 상태

@csrf_exempt
@api_view(['PUT'])
def class_request(request):
    data = request.data
    resvnumb = data["resv_numb"] # 예약일련번호
    # clssnumb = data['clss_numb'] # 수업개설넘버
    # clasdate = data['clas_date'] # 수업날짜
    # umemnumb = data['umem_numb'] # 사용자 멤버쉽코드
    resvstat = data['resv_stat'] # 예약상태

    queryset = ReMaster.objects.get(resv_numb = resvnumb)
    if queryset:
        queryset.resv_stat = resvstat

    try:
        queryset.save()
        return HttpResponse(status=200) 
    except:
        return HttpResponse(status=400, content=f"Fail update")




# API : http://127.0.0.1:8000/trmbship/
# 제목 : 강의생성 수강 가능 리스트 리턴
# 로직 : 너 수강권 뭐있음?
# 요청 : ID : 00000000
# 리턴 : 수강권 리스트
@csrf_exempt
@api_view(['GET'])
def trmbship_list(request):
    data = request.data
    usernumb = data['usernumb']

    trmb_ob = TrMbship.objects.filter(user_numb=usernumb) # 강의 정보 가져오기

    # for da in trmb_ob:
    #    print(da.tmem_name)
    serializer = TrMbshipSerializer(trmb_ob,many=True)
    return Response(serializer.data)

# API : http://127.0.0.1:8000/make_class/
# 제목 : 강의생성 기본값 셋팅로직
# 로직 : 강의 생성 버튼 눌렀을때 기본값 셋팅
# 요청 : 강의명, 강의시작시간, 종료시간, 날짜, 예약마감, 개인단체구분, 정원, 운동구분 코드, 센터명
# 리턴 : x
@csrf_exempt
@api_view(['POST','PUT','DELETE'])
def make_class(request):
    # 입력값 정의
    clasnumb = request.data["clas_numb"] # 삭제 수정에는 필요, 등록일땐 빈칸
    tmemnumb = request.data["tmem_numb"] # 수강권번호
    userid = request.data["user_id"] # ID값

    # INSERT
    if request.method == 'POST':
        last_serial = TrClass.objects.order_by('-clas_numb').first()
        if last_serial:
            last_date = last_serial.clas_numb[:6]

            if last_date == datetime.now().strftime('%y%m%d'):
                sum_serial = int(last_serial.clas_numb[6:]) + 1
                formatted_num = f"{sum_serial:04d}"
                new_serial = str(datetime.now().strftime('%y%m%d')) + formatted_num
            else:
                new_serial = str(datetime.now().strftime('%y%m%d')) + '0000'

        
        clasdate_v = request.data["clas_date"] # 강의시작시간 
        clastime_v = request.data["clas_time"] # 수업시작시간 4자리 1130
        clasname_v = request.data["clas_name"] # 강의이름
        clasclos_v = request.data["clas_clos"] # 수업종료시간 4자리 1130
        clasnmax_v = request.data["clas_nmax"] # 정원 2자리
        claswait_v = request.data["clas_wait"] # 대기인원 2자리
        resvstat_v = request.data["resv_stat"] # 예약시작시간 12자리 202302011130
        resvlast_v = request.data["resv_last"] # 예약마감시간 12자리 202302211200
        resvalr1_v = request.data["resv_alr1"] # 예약마감전 알람시간 2자리 11시간
 
        # 모델 객체 생성 및 저장
        new_data = TrClass(clas_numb=new_serial, clas_date=clasdate_v,clas_time=clastime_v,clas_nmax=clasnmax_v,clas_name=clasname_v,
                            clas_wait=claswait_v,resv_stat=resvstat_v,resv_last=resvlast_v,resv_alr1=resvalr1_v,
                            clas_clos=clasclos_v, tmem_numb=tmemnumb,clas_ysno='Y',clas_inst=datetime.now())

        
        try:
            new_data.save()  # 데이터 저장 시도
            return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
        except :
            # 저장에 실패한 경우 
            return HttpResponse(status=400, content=f"Fail save")

    # UPDATE
    elif request.method == 'PUT':
        try:
            obj = TrClass.objects.get(clas_numb=clasnumb)
        except :
            return HttpResponse(status=404, content=f"No match data, {clasnumb}")

        clasname_v = request.data["clas_name"] # 강의이름
        clasdate_v = request.data['clas_date'] # 강의시작시간 
        clastime_v = request.data["clas_time"] # 수업시작시간 4자리 1130
        clasclos_v = request.data["clas_clos"] # 수업종료시간 4자리 1130
        clasnmax_v = request.data["clas_nmax"] # 정원 2자리
        claswait_v = request.data["clas_wait"] # 대기인원 2자리
        resvstat_v = request.data["resv_stat"] # 예약시작시간 12자리 202302011130
        resvlast_v = request.data["resv_last"] # 예약마감시간 12자리 202302211200
        resvalr1_v = request.data["resv_alr1"] # 예약마감전 알람시간 2자리 11시간

        # 모델 객체 생성 및 저장
        obj.clas_name = clasname_v
        obj.clas_date = clasdate_v
        obj.clas_time = clastime_v
        obj.clas_clos = clasclos_v
        obj.clas_nmax = clasnmax_v
        obj.clas_wait = claswait_v
        obj.resv_stat = resvstat_v
        obj.resv_last = resvlast_v
        obj.resv_alr1 = resvalr1_v
        obj.clas_updt = datetime.now()
        try:
            obj.save()  # 데이터 저장 시도
            return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
        except :
            # 저장에 실패한 경우 
            return HttpResponse(status=400, content=f"Fail update")

            
    # DELETE
    elif request.method == 'DELETE':
        try:
            obj = TrClass.objects.get(clas_numb=clasnumb)
        except :
            return HttpResponse(status=404, content=f"No match data, {clasnumb}")

        try:
            obj.delete()  # 데이터 저장 시도
            return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
        except :
            # 저장에 실패한 경우 400
            return HttpResponse(status=400, content=f"Fail delete")
    else:
        return 

