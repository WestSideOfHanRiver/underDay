'use client'

import Calendar from '@components/calendar'

import { useState } from 'react'
import LessonApply from '@components/lessonApply'
import Modal from '@components/modal'
import LessonList from '@components/lessonList'

export default function Home() {
  const [toggleApplyModal, setToggleApplyModal] = useState(false)

  return (
    <>
      <Calendar />
      <LessonList />
      {toggleApplyModal && (
        <Modal>
          <LessonApply
            applyData={{
              resv_numb: '',
              user_numb: '00000002',
              clas_numb: '2308010004',
              tmem_numb: 'A0000004',
              resv_stat: '01',
            }}
            closeModal={() => setToggleApplyModal(false)}
          />
        </Modal>
      )}
    </>
  )
}
