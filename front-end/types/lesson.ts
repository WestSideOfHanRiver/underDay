export interface LessonResponse {
  clas_numb: string // 수업개설일련번호
  clas_name: string // 수업이름
  clas_date: string // 수업일자
  clas_time: string // 수업시작시간
  clas_clos: string // 수업종료시간
  tmem_numb: string // 강사수업일련번호
  tech_name: string // 강사이름
  clas_nmax: number // 정원
  clas_cmax: number // 신청인원
  clas_wait: number // 총 대기 가능 인원
  clas_cwai: number // 현재 대기인원
  resv_stat: string // 예약시작시간
  resv_last: string // 예약마감시간
  resv_alr1: number // 예약확인알림시간
  clas_ysno: string // 수업예약마감여부
  clas_inst: string // 수업생성일시
  clas_updt: string | null // 업데이트날짜
  reservationState: string // 수업 예약 상태
  reservationId: string // 수업 일련번호
  tmem_cate: string // 카테고리
}

export interface Lesson {
  classId: string
  lessonName: string
  lessonDate: string
  startTime: string
  endTime: string
  ticketId: string
  teacherName: string
  maxOccupancy: number
  enrollment: number
  maxWaiting: number
  waitingCount: number
  startBookingTime: string
  endBookingTime: string
  bookingCheckTime: string
  availableBooking: string
  createdAt: string
  updatedAt: string
  reservationState: string
  reservationId: string
  category: string
}

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
