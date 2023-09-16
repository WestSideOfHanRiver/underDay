import { Dispatch, SetStateAction, useState } from 'react';
import DatePicker, { DayValue, Locale } from '@hassanmojab/react-modern-calendar-datepicker';

import '@hassanmojab/react-modern-calendar-datepicker/lib/DatePicker.css';
import styles from "./datepicker.module.scss";

interface Props {
    onChange?: (date: DayValue | null) => void;  
    position?: any  
    title?: string 
}

export default function InputDate ({ onChange, position, title }: Props ) {
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
    
        getToday(gregorainTodayObject: { year: number, month: number, day: number }) {
            return gregorainTodayObject;
        },
    
        toNativeDate(date: { year: number; month: number; day: number; }) {
            return new Date(date.year, date.month, date.day);
        },
    
        getMonthLength(date: { year: number; month: number }) {
            return new Date(date.year, date.month, 0).getDate();
        },
    
        transformDigit(digit: any) {
            return digit;
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

    const [day, setDay] = useState<DayValue>(null);
    const handleCalendar = (selectedDay: DayValue) => {
        setDay(selectedDay);

        // if (selectedDay !== null && onChange) {
        //     onChange(selectedDay); 
        // }
    }

    return(
        <DatePicker
            wrapperClassName={styles.calendarWrap}
            value={day}
            onChange={handleCalendar}
            colorPrimary="#0fbcf9"
            calendarPopperPosition={position}
            colorPrimaryLight="rgba(75, 207, 250, 0.4)"
            calendarClassName={styles.calendar}
            locale={myCustomLocale}
            calendarTodayClassName={styles.calendarToday}
            shouldHighlightWeekends
            inputPlaceholder={title}
        />
    )
}