'use client'

import { useState } from 'react'

import Modal from '@components/modal/modal'
import TicketDetails from '../ticketDetails/ticketDetails'

export default function AddTicketButton() {
  const [toggleDetail, setToggleDetail] = useState(false)

  const handleClickAdd = () => {
    setToggleDetail(true)
  }

  return (
    <>
      <button type="button" onClick={handleClickAdd}>회원권 생성하기</button>
      {toggleDetail && (
        <Modal>
          <TicketDetails setToggleDetail={setToggleDetail} />
        </Modal>
      )}
    </>
  )
}
