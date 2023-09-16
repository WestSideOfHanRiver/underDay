export interface ClassDetails {
  classId: string // 강사 수업 일련번호
  title: string // 수업이름
  date: string // 수업날짜
  startTime: string // 수업 시작 시간
  endTime: string // 수업 종료 시간
  startBookingTime: string // 수업 예약 시간 시간
  endBookingTime: string // 수업 예약 종료 시간
  maxParticipantsCount: number // 정원
  maxWaitingCount: number // 대기인원
  alertTimeOfBooking: string // 예약 알림시간
}

/*
수업개설일련번호	CLAS_NUMB 	NVARCHAR(7)	ex)C002311 최대 10억개 영어1자리 + 숫자 6자리
수업일자	CLAS_DATE	NVARCHAR(8)	ex) 00000000년월일 20230601
수업시작시간	CLAS_TIME	NVARCHAR(4)	HHMM
수업종료시간	CLAS_CLOS	NVARCHAR(4)	HHMM
강사수업일련번호	TMEM_NUMB 	NVARCHAR(8)	(ex)10320023 최대 1억개 숫자 8자리
정원	CLAS_NMAX	NVARCHAR(2)	양의정수
대기인원	CLAS_WAIT	NVARCHAR(2)	양의정수
예약시작시간			
예약마감시간	CLAS_LAST	NVARCHAR(8)	ex) 00000000년월일
예약확인알림시간	CLAS_ALR1	NVARCHAR(8)	ex) 보류
수강확정일림시간	CLAS_ALR2	NVARCHAR(8)	ex) 00000000년월일
수업예약마감여부	CLAS_YSNO	NVARCHAR(1)	(Y,N)
수업생성일시	CLAS_INST	DATETIMEFIELD	(000000000000)년월일시간분 12자리 DateTimeField
업데이트 날짜	                                           	DATETIMEFIELD	내정보 업데이트
*/
