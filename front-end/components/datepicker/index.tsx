import { useState } from 'react'
import { useFormContext } from 'react-hook-form'
import DatePicker, {
  DayValue,
  Locale,
} from '@hassanmojab/react-modern-calendar-datepicker'

import '@hassanmojab/react-modern-calendar-datepicker/lib/DatePicker.css'
import styles from './datepicker.module.scss'

interface DateProps {
  data: string
  title: string
  value?: DayValue
}

export default function InputDate({ data, title, value }: DateProps) {
  const { setValue } = useFormContext()
  const myCustomLocale: Locale = {
    months: [
      '1월',
      '2월',
      '3월',
      '4월',
      '5월',
      '6월',
      '7월',
      '8월',
      '9월',
      '10월',
      '11월',
      '12월',
    ],

    weekDays: [
      {
        name: '일요일',
        short: 'S',
        isWeekend: true,
      },
      {
        name: '월요일',
        short: 'M',
      },
      {
        name: '화요일',
        short: 'T',
      },
      {
        name: '수요일',
        short: 'W',
      },
      {
        name: '목요일',
        short: 'T',
      },
      {
        name: '금요일',
        short: 'F',
      },
      {
        name: '토요일',
        short: 'S',
        isWeekend: true,
      },
    ],

    weekStartingIndex: 0,

    getToday(gregorainTodayObject: {
      year: number
      month: number
      day: number
    }) {
      return gregorainTodayObject
    },

    toNativeDate(date: { year: number; month: number; day: number }) {
      return new Date(date.year, date.month, date.day)
    },

    getMonthLength(date: { year: number; month: number }) {
      return new Date(date.year, date.month, 0).getDate()
    },

    transformDigit(digit: any) {
      return digit
    },

    nextMonth: 'Next Month',
    previousMonth: 'Previous Month',
    openMonthSelector: 'Open Month Selector',
    openYearSelector: 'Open Year Selector',
    closeMonthSelector: 'Close Month Selector',
    closeYearSelector: 'Close Year Selector',
    defaultPlaceholder: 'Select...',
    from: '',
    to: '~',
    digitSeparator: ',',
    yearLetterSkip: 0,
    isRtl: false,
  }

  const [day, setDay] = useState<DayValue>(value)

  const handleCalendar = (selectedDay: DayValue) => {
    setDay(selectedDay)
    setValue(data, formatDate(selectedDay))
  }

  const formatDate = (selectedDay: DayValue) => {
    if (selectedDay) {
      const { year, month, day } = selectedDay
      return year.toString() + month.toString() + day.toString()
    }
  }

  return (
    <DatePicker
      wrapperClassName={styles.calendarWrap}
      value={day}
      onChange={handleCalendar}
      colorPrimary="#0fbcf9"
      calendarPopperPosition={'top'}
      colorPrimaryLight="rgba(75, 207, 250, 0.4)"
      calendarClassName={styles.calendar}
      locale={myCustomLocale}
      calendarTodayClassName={styles.calendarToday}
      shouldHighlightWeekends
      inputPlaceholder={title}
    />
  )
}
