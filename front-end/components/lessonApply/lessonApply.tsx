'use client'

import { useEffect, useRef } from 'react'
import styles from './lessonApply.module.scss'
import { applyLesson } from './api'

interface ApplyData {
  resv_numb: string
  user_numb: string
  clas_numb: string
  tmem_numb: string
  resv_stat: string
}

const applyData = {
  resv_numb: '',
  user_numb: '00000002',
  clas_numb: '2308010004',
  tmem_numb: 'A0000004',
  resv_stat: '01',
}

interface Props {
  applyData: ApplyData
  closeModal: () => void
}

export default function LessonApply({ applyData, closeModal }: Props) {
  const modalRef = useRef<HTMLDivElement>(null)

  const handleClickApply = () => {
    applyLesson(applyData)
    closeModal()
  }

  const handleClickCancel = () => {
    closeModal()
  }

  useEffect(() => {
    const handleCloseModal = (e: MouseEvent) => {
      if (!modalRef.current?.contains(e.currentTarget as Node)) {
        closeModal()
      }
    }

    document.addEventListener('click', handleCloseModal)

    return () => {
      document.removeEventListener('click', handleCloseModal)
    }
  }, [])

  return (
    <>
      <div className={styles.background}></div>
      <div className={styles.applyModal} ref={modalRef}>
        <div className={styles.content}>
          <p>신청하시겠습니까?</p>
        </div>
        <div className={styles.actions}>
          <button
            className={styles.applyButton}
            type="button"
            onClick={handleClickApply}
          >
            신청
          </button>
          <button
            className={styles.closeButton}
            type="button"
            onClick={handleClickCancel}
          >
            닫기
          </button>
        </div>
      </div>
    </>
  )
}
