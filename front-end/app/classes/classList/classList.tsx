'use client'

import { useEffect, useState } from 'react'
import { useSelector } from 'react-redux'
import { Lesson } from 'types/lesson'
import { fetchDailyLessons } from './api'
import { SelectedDateState } from '@stores/selectedDate'
import styles from './classList.module.scss'

import ClassCard from '../classCard'

export default function ClassList() {
  const selectedDate = useSelector(
    (state: SelectedDateState) => state.selectedDate.value,
  )
  const [classes, setClasses] = useState<Lesson[]>([])

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchDailyLessons({
        userId: '00000010',
        selectedDate,
        userType: 'B',
      })

      setClasses(result)
    }

    fetchData()
  }, [selectedDate])

  if (classes.length === 0) {
    return <p className={styles.message}>예정중인 강의가 없습니다.</p>
  }

  return (
    <ul>
      {classes.map((el: Lesson) => (
        <li key={el.classId}>
          <ClassCard
            teacher={''}
            category={''}
            lessonName={el.lessonName}
            lessonState={'예약확정'}
            startTime={el.startTime}
            endTime={el.endTime}
            maxOccupancy={el.maxOccupancy}
          />
        </li>
      ))}
    </ul>
  )
}
