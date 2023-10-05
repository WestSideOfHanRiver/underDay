'use client'
import TICKETS from './mockupData'
import { useState } from 'react'
import Modal from '@components/modal'
import TicketDetails from './ticketDetails/ticketDetails'
import AddTicketsButton from './addTicketButton/index'
import TicketCard from './ticketsCard/ticketsCard'

const data = {
  category: '요가',
  teacher: '조완석',
  lessonName: '다리 찢어보자 요가킹',
  lessonState: '예약대기',
}

export default function TicketsPage() {
  const [toggleDetail, setToggleDetail] = useState(false)

  return (
    <>
      <AddTicketsButton setToggleDetail={setToggleDetail} />

      {/* 반복문 돌거임 */}
      <TicketCard setToggleDetail={setToggleDetail} />

      {toggleDetail && (
        <Modal>
          <TicketDetails setToggleDetail={setToggleDetail} data={data} />
        </Modal>
      )}
    </>
  )
}
