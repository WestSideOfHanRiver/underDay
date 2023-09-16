'use client'

import { useState } from 'react'

import styles from './addClassButton.module.scss'
import ClassDetails from '@components/classDetails'
import Modal from '@components/modal/modal'

export default function AddClassButton() {
  const [toggleDetail, setToggleDetail] = useState(false)

  const handleClickAdd = () => {
    setToggleDetail(true)
  }

  return (
    <>
      <button
        className={`${styles.addButton} ${toggleDetail ? styles.close : ''}`}
        type="button"
        onClick={handleClickAdd}
      />
      {toggleDetail && (
        <Modal>
          <ClassDetails setToggleDetail={setToggleDetail} />
        </Modal>
      )}
    </>
  )
}
