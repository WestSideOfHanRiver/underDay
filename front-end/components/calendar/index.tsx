'use client'

import { MouseEvent, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import moment, { Moment } from 'moment'
import Image from 'next/image'

import styles from './calendar.module.scss'

import PreviousIcon from '@svg/previous.svg'
import NextIcon from '@svg/next.svg'

import { SelectedDateState } from '@stores/selectedDate'
import { setSelectedDate } from './selectedDateSlice'

export default function Calendar() {
  const [currentMoment, setCurrentMoment] = useState(moment())
  const [slideAnimation, setSlideAnimation] = useState('')
  const dispatch = useDispatch()
  const selectedDate = useSelector(
    (state: SelectedDateState) => state.selectedDate.value,
  )

  const handleMonthChange = (monthsToAdd: number) => {
    const newMoment = currentMoment.clone().add(monthsToAdd, 'month')
    setCurrentMoment(newMoment)
  }

  const handleClickDate = (e: MouseEvent<HTMLLIElement>) => {
    const clickedDate = moment(e.currentTarget.dataset.date, 'YYMMDD')
    const isDifferentMonth = !currentMoment.isSame(clickedDate, 'month')

    if (isDifferentMonth) {
      setCurrentMoment(clickedDate)
    }

    dispatch(setSelectedDate(clickedDate.format('YYMMDD')))
  }

  const handleResetCurrentMoment = () => {
    const current = moment()

    setCurrentMoment(current)
    dispatch(setSelectedDate(current.format('YYMMDD')))
  }

  const generateCalendar = (moment: Moment) => {
    const firstWeek = moment.clone().startOf('month').week()
    const lastWeek =
      moment.clone().endOf('month').week() === 1
        ? 53
        : moment.clone().endOf('month').week()

    let calendar = []
    for (let week = firstWeek; week <= lastWeek; week++) {
      calendar.push(
        <ul key={week} className={`${styles.days} ${slideAnimation}`}>
          {Array.from({ length: 7 }).map((_, index) =>
            renderDayCell(week, index),
          )}
        </ul>,
      )
    }

    return calendar
  }

  const renderDayCell = (week: number, index: number) => {
    const day = currentMoment
      .clone()
      .startOf('year')
      .week(week)
      .startOf('week')
      .add(index, 'day')
    const isToday = moment().isSame(day, 'day')
    const isDifferentMonth = !currentMoment.isSame(day, 'month')
    const isSelectedDate = day.format('YYMMDD') === selectedDate

    return (
      <li
        key={index}
        className={`${isToday ? styles.today : ''} ${
          isDifferentMonth ? styles.before : ''
        } ${isSelectedDate ? styles.selectedDate : ''}`}
        data-day={day.day()}
        data-date={day.format('YYMMDD')}
        onClick={handleClickDate}
      >
        {day.format('D')}
      </li>
    )
  }

  return (
    <div className={styles.content}>
      <div className={styles.topTit}>
        <button type="button" onClick={() => handleMonthChange(-1)}>
          <Image src={PreviousIcon} alt="previous month" />
        </button>
        <h2 onClick={handleResetCurrentMoment}>
          {currentMoment.format('YY년 M월')}
        </h2>
        <button type="button" onClick={() => handleMonthChange(1)}>
          <Image src={NextIcon} alt="next month" />
        </button>
      </div>
      <ul className={styles.dayTit}>
        {'일월화수목금토'.split('').map((day) => (
          <li key={day}>{day}</li>
        ))}
      </ul>
      {generateCalendar(currentMoment)}
    </div>
  )
}
