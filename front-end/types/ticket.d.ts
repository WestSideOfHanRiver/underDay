export interface TicketDetails {
  membership_seq: string // 회원권일련번호,
  user_member_seq: string // 사용자일련번호(회원),
  user_member_id: string // 사용자ID(회원),
  user_member_nm: string // 사용자명(회원),
  class_seq: number // 강사수업일련번호,
  class_nm: string // 강의명,
  membership_stat_date: string // 회원권이용시작일자,
  membership_end_date: string // 회원권이용종료일자,
  membership_join_number: string // 회원권등록회차,
  membership_use_number: string // 회원권사용회차,
  membership_use_yn: 'Y' | 'P' | 'N' // 회원권사용가능여부,
  user_teach_seq: string // 사용자일련번호(강사),
  user_teach_id: string // 사용자ID(강사),
  user_teach_nm: string // 사용자명(강사)
}

export interface TicketClasses {
  tmem_numb: number
  user_numb: number
  tmem_name: string
}
