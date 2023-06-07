'use client'

import { MouseEvent, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import moment from 'moment'

import styles from './calendar.module.scss'

import { RootState } from '@/store'
import { setSelectedDate } from './selectedDateSlice'

const DUMMYDATE = ['20230623', '20230626']

export default function Calendar() {
  const [getMoment, setMoment] = useState(moment())
  const [getTitle, setTitle] = useState(getMoment.format('M'))

  const handleCalendar = (days: number) => {
    const date = getMoment.clone().add(days, 'month')

    setMoment(date)
    setTitle(date.format('M'))
  }

  const selectedDate = useSelector(
    (state: RootState) => state.selectedDate.value,
  )
  const dispatch = useDispatch()

  const handleClickDate = (e: MouseEvent<HTMLLIElement>) => {
    dispatch(setSelectedDate(e.currentTarget.dataset.date!))
  }

  const calendarArr = () => {
    const today = getMoment
    const firstWeek = today.clone().startOf('month').week()
    const lastWeek =
      today.clone().endOf('month').week() === 1
        ? 53
        : today.clone().endOf('month').week()

    let result: any[] = []
    let week = firstWeek

    for (week; week <= lastWeek; week++) {
      result = result.concat(
        <ul key={week} className={styles.days}>
          {Array(7)
            .fill(0)
            .map((_, index) => {
              let days = today
                .clone()
                .startOf('year')
                .week(week)
                .startOf('week')
                .add(index, 'day')

              let styleClass = null

              if (moment().isSame(days, 'day')) {
                styleClass = 'today'
              } else if (!today.isSame(days, 'month')) {
                styleClass = 'before'
              }

              return (
                <li
                  key={index}
                  className={`${
                    styleClass != null ? `${styles[styleClass]}` : ''
                  } ${
                    days.format('YYMMDD') === selectedDate
                      ? styles.selectedDate
                      : ''
                  }`}
                  data-day={`${days.day()}`}
                  data-date={`${days.format('YYMMDD')}`}
                  onClick={handleClickDate}
                >
                  {days.format('D')}
                  {DUMMYDATE.map((date, index) => {
                    if (date === days.format('YYYYMMDD')) {
                      return <small key={index} className={styles.dot}></small>
                    }
                  })}
                </li>
              )
            })}
        </ul>,
      )
    }
    return result
  }

  const Dates = calendarArr()

  return (
    <div className={styles.content}>
      <div className={styles.topTit}>
        <h2>{getTitle}</h2>
        <div className={styles.topBtn}>
          <button type="button" onClick={() => handleCalendar(-1)}>
            전
          </button>
          <button type="button" onClick={() => handleCalendar(1)}>
            후
          </button>
        </div>
      </div>
      <ul className={styles.dayTit}>
        {'일월화수목금토'.split('').map((day) => (
          <li key={day}>{day}</li>
        ))}
      </ul>
      {Dates}
    </div>
  )
}
