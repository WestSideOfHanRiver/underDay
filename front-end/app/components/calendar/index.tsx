'use client'

import moment from 'moment'
import { useState } from 'react'

import styles from './calendar.module.scss'

const DUMMYDATE = ['20230523', '20230526']

export default function Calendar() {
  const [getMoment, setMoment] = useState(moment())
  const [getTitle, setTitle] = useState(getMoment.format('M'))

  const handleCalendar = (days: number) => {
    const date = getMoment.clone().add(days, 'month')

    setMoment(date)
    setTitle(date.format('M'))
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
            .map((data, index) => {
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
                  data-day={`${days.day()}`}
                  className={styleClass != null ? `${styles[styleClass]}` : ''}
                >
                  {days.format('DD')}
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
        <button type="button" onClick={() => handleCalendar(-1)}></button>
        <h2>{getTitle}월</h2>
        <button type="button" onClick={() => handleCalendar(1)}></button>
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
