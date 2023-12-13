'use client'

import { TicketDetails } from 'types/ticket'
import { useState } from 'react'

import TicketDetail from '../ticketDetails/ticketDetails'
import moment from 'moment'

import styles from './ticketsCard.module.scss'

export default function TicketCard({ ...el }: TicketDetails) {
  const stateStyle = {
    Y: '이용가능',
    N: '이용불가',
    P: '이용중지',
  }[el.membership_use_yn]

  const [toggleDetail, setToggleDetail] = useState(false)

  const handleClickTicket = () => {
    setToggleDetail(true)
  }

  return (
    <>
      <div className={styles.ticket} onClick={handleClickTicket}>
        <div className={styles.tickets_info}>
          <div className={styles.ticket_label}>
            <small>{el.class_nm}ᆞ</small>
            <small>{el.user_teach_nm}</small>
          </div>
          <p className={styles.ticket_title}>{el.user_member_nm}</p>
          <p
            className={`${styles.ticket_state} ${styles[el.membership_use_yn]}`}
          >
            {stateStyle}
          </p>
          <p className={styles.ticket_date}>
            {moment(el.membership_stat_date).format('YYYY.MM.DD')} ~
            {moment(el.membership_end_date).format('YYYY.MM.DD')}
          </p>
        </div>
        <div className={styles.tickets_detail}>
          <span>
            회차 {el.membership_use_number} / {el.membership_join_number}
          </span>
          <span>{el.user_member_nm} 회원</span>
          <span>{el.membership_seq}</span>
        </div>
      </div>

      {toggleDetail && (
        <TicketDetail setToggleDetail={setToggleDetail} data={el} />
      )}
    </>
  )
}
