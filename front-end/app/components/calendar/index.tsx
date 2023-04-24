'use client'

import moment from 'moment'
import { useState } from 'react'

import styles from './calendar.module.scss'

export default function Calendar() {
  const [getMoment, setMoment] = useState(moment())
  const [getTitle, setTitle] = useState(getMoment.format('YY.MM'))

  const handleCalendar = (days: number) => {
    const date = getMoment.clone().add(days, 'month')

    setMoment(date)
    setTitle(date.format('YY.MM'))
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

              let styleClass = ''

              if (moment().format('YYYYMMDD') === days.format('YYYYMMDD')) {
                styleClass = 'today'
              } else if (today.format('YYYYMM') !== days.format('YYYYMM')) {
                styleClass = 'before'
              }

              return (
                <li key={index} className={`${styles[styleClass]}`}>
                  {days.format('DD')}
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
