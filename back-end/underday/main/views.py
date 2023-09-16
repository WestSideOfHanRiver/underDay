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

# 제목 : 캘린더 메인페이지  
# 로직 : 월/일 에 해당하는 모든 데이터, 수강가능한 일정
# 요청 : Nickname, date, time
# 리턴 : 수강가능 강의 리스트
# id, date20230303, time1430
# ur_master -> ur_mbship -> tr_class
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



######################    Serializer 사용한 class_list 함수   ###########################
# API : http://127.0.0.1:8000/classlist/
@csrf_exempt
@api_view(['GET'])
def class_list(request):
    data = request.data
    usernumb = data['usernumb']
    date = data['date']
    time = data['time']
    mbsh_ob = UrMbship.objects.filter(user_numb=usernumb)# 유저 맴버쉽 가져오기
    accumulated_queryset =TrClass.objects.none()
    for i in mbsh_ob:
        try:
            trcl_ob = TrClass.objects.filter(tmem_numb=i.tmem_numb,clas_date=date) # 강의 리스트
            accumulated_queryset |= trcl_ob
            print(trcl_ob)
            for j in trcl_ob:
                clas_time = j.clas_time
            print(date+'일의 강의 ' +clas_time[:2]+'시 ' + clas_time[2:4]+'분 ' +trmb_ob.tmem_name)
 
        except:
            classlist = None
            print('강의가 없어요')
        trmb_ob = TrMbship.objects.get(tmem_numb=i.tmem_numb) # 강의 정보 가져오기
        print(date+'일의 강의 ' +clas_time[:2]+'시 ' + clas_time[2:4]+'분 ' +trmb_ob.tmem_name)
        print()
    print(accumulated_queryset)
    serializer = TrClassSerializer(accumulated_queryset,many=True)
    return Response(serializer.data)

######################################################################################3

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
    print(usernumb)
    trmb_ob = TrMbship.objects.filter(user_numb=usernumb) # 강의 정보 가져오기
    print(trmb_ob)
    # for da in trmb_ob:
    #    print(da.tmem_name)
    serializer = TrMbshipSerializer(trmb_ob,many=True)
    return Response(serializer.data)

# API : http://127.0.0.1:8000/classrequest/
# 제목 : 강의생성 기본값 셋팅로직
# 로직 : 강의 생성 버튼 눌렀을때 기본값 셋팅
# 요청 : 강의명, 강의시작시간, 종료시간, 날짜, 예약마감, 개인단체구분, 정원, 운동구분 코드, 센터명
# 리턴 : x
@csrf_exempt
@api_view(['POST','PUT','DELETE'])
def class_request(request):
    # 입력값 정의
    clasnumb = request.data["clasnumb"] # 삭제 수정에는 필요, 등록일땐 빈칸
    tmemnumb = request.data["tmemnumb"] # 수강권번호
    userid = request.data["userid"] # ID값

    # INSERT
    if request.method == 'POST':
        last_serial = TrClass.objects.order_by('-clas_numb').first()
    
        print(last_serial)
        if last_serial:
            last_date = last_serial.clas_numb[:6]
            print(last_date)

            if last_date == datetime.now().strftime('%y%m%d'):
                sum_serial = int(last_serial.clas_numb[6:]) + 1
                formatted_num = f"{sum_serial:04d}"
                new_serial = str(datetime.now().strftime('%y%m%d')) + formatted_num
            else:
                new_serial = str(datetime.now().strftime('%y%m%d')) + '0000'

        
        clasdate_v = request.data['clasdate'] # 강의시작시간 
        clastime_v = request.data["clastime"] # 수업시작시간 4자리 1130
        clasclos_v = request.data["clasclos"] # 수업종료시간 4자리 1130
        clasnmax_v = request.data["clasnmax"] # 정원 2자리
        claswait_v = request.data["claswait"] # 대기인원 2자리
        resvstat_v = request.data["resvstat"] # 예약시작시간 12자리 202302011130
        resvlast_v = request.data["resvlast"] # 예약마감시간 12자리 202302211200
        resvalr1_v = request.data["resvalr1"] # 예약마감전 알람시간 2자리 11시간
 
        # 모델 객체 생성 및 저장
        new_data = TrClass(clas_numb=new_serial, clas_date=clasdate_v,clas_time=clastime_v,clas_nmax=clasnmax_v,
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

        clasdate_v = request.data['clasdate'] # 강의시작시간 
        clastime_v = request.data["clastime"] # 수업시작시간 4자리 1130
        clasclos_v = request.data["clasclos"] # 수업종료시간 4자리 1130
        clasnmax_v = request.data["clasnmax"] # 정원 2자리
        claswait_v = request.data["claswait"] # 대기인원 2자리
        resvstat_v = request.data["resvstat"] # 예약시작시간 12자리 202302011130
        resvlast_v = request.data["resvlast"] # 예약마감시간 12자리 202302211200
        resvalr1_v = request.data["resvalr1"] # 예약마감전 알람시간 2자리 11시간
        print(clasdate_v,clastime_v,clasclos_v)
        # 모델 객체 생성 및 저장
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


