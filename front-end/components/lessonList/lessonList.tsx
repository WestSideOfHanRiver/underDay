'use client'

import { useEffect, useState } from 'react'
import { fetchLessons } from './api'

import styles from './lessonList.module.scss'
import { useSelector } from 'react-redux'
import { SelectedDateState } from '@stores/selectedDate'
import { Lesson } from 'types/lesson'
import LessonCard from '@components/lessonCard'
import { TbAdjustmentsFilled } from 'react-icons/tb'
import LessonApply from '@components/lessonApply'
import axios from 'axios'

export default function LessonList() {
  const [lessons, setLessons] = useState<Lesson[]>([])
  const selectedDate = useSelector(
    (state: SelectedDateState) => state.selectedDate.value,
  )

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchLessons(selectedDate)

      setLessons(result)
    }

    fetchData()
  }, [selectedDate])

  const [toggleApplyModal, setToggleApplyModal] = useState(false)

  const handleClickLesson = () => {
    setToggleApplyModal(true)

    const url = `https://port-0-underdaybackend-iciy2almouoe34.sel5.cloudtype.app/classrequest/`
    axios.put(url)
  }

  if (lessons.length === 0) {
    return <p className={styles.message}>신청 가능한 강의가 없습니다.</p>
  }

  // FIXME: 지워라
  const applyData = {
    resv_numb: '',
    user_numb: '00000002',
    clas_numb: '2308010004',
    tmem_numb: 'A0000004',
    resv_stat: '01',
  }

  return (
    <>
      {lessons.map((lesson) => (
        <li key={lesson.classId} onClick={handleClickLesson}>
          <LessonCard
            teacher={lesson.teacherName}
            lessonName={lesson.lessonName}
            lessonState={lesson.reservationState}
            category={lesson.category}
            startTime={lesson.startTime}
            endTime={lesson.endTime}
          />
        </li>
      ))}
      {toggleApplyModal && (
        <LessonApply
          applyData={applyData}
          closeModal={() => setToggleApplyModal(false)}
        />
      )}
    </>
  )
}
