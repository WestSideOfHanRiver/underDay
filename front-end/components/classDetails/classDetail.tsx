'use client'

import { Dispatch, SetStateAction, useEffect, useRef } from 'react'
import { SubmitHandler, useForm } from 'react-hook-form'

import { ClassDetails } from 'types/class'

import styles from './classDetail.module.scss'

interface Props {
  setToggleDetail: Dispatch<SetStateAction<boolean>>
  title?: string
}

export default function ClassDetails({ setToggleDetail, title }: Props) {
  const { register, handleSubmit } = useForm<ClassDetails>({
    defaultValues: {
      title: title || '',
    },
  })
  console.log('title:', title)
  const submitClass: SubmitHandler<ClassDetails> = (data) => {
    console.log('class registered!!')
  }
  // FIXME: classId는 어떻게 넘길것인가 ?

  const thisForm = useRef<HTMLFormElement>(null)
  const focusedInput = useRef<HTMLInputElement>(null)

  useEffect(() => {
    const closeModal = (e: MouseEvent) => {
      if (!thisForm.current?.contains(e.target as Node)) {
        setToggleDetail(false)
      }
    }

    document.addEventListener('click', closeModal)
    // focusedInput.current?.focus()

    return () => {
      document.removeEventListener('click', closeModal)
    }
  }, [])

  return (
    <>
      <form
        className={styles.classForm}
        onSubmit={handleSubmit(submitClass)}
        ref={thisForm}
      >
        <label>수업명</label>
        <input
          className={styles.input}
          {...register('title', { required: true })}
          name="title"
        />
        <label>날짜</label>
        <input
          className={styles.input}
          {...register('date', { required: true })}
        />
        <label>시작 시간</label>
        <input
          className={styles.input}
          {...register('startTime', { required: true })}
        />
        <label>종료 시간</label>
        <input
          className={styles.input}
          {...register('endTime', { required: true })}
        />
        <label>강의 신청 시작</label>
        <input
          className={styles.input}
          {...register('startBookingTime', { required: true })}
        />
        <label>강의 신청 마감</label>
        <input
          className={styles.input}
          {...register('endBookingTime', { required: true })}
        />
        <label>정원</label>
        <input
          className={styles.input}
          {...register('maxParticipantsCount', { required: true })}
        />
        <label>대기 인원</label>
        <input
          className={styles.input}
          {...register('maxWaitingCount', { required: true })}
        />
        <label>예약 알림 시간</label>
        <input
          className={styles.input}
          {...register('alertTimeOfBooking', { required: true })}
        />
        <button type="submit">등록 or 수정</button>
      </form>
    </>
  )
}
