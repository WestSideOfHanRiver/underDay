'use client'

import { useState } from 'react'

import TicketDetails from '../ticketDetails/ticketDetails'

import styles from '../tickets.module.scss'

export default function AddTicketButton() {
  const [toggleDetail, setToggleDetail] = useState(false)

  const handleClickAdd = () => {
    setToggleDetail(true)
  }

  return (
    <>
      <button
        className={styles.ticketsBtn}
        type="button"
        onClick={handleClickAdd}
      >
        생성
      </button>

      {toggleDetail && <TicketDetails setToggleDetail={setToggleDetail} />}
    </>
  )
}
