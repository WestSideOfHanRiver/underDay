import styles from './ticketsCard.module.scss'
import AddTicketsButton from '../addTicketButton'

export default function TicketCard() {
  return (
      <div className={styles.content}>
        <article className={styles.tickets_wrap}>
          <div className={styles.tickets_info}>
            <p className={styles.name}>dfdfd Up for One Night Stand</p>
            <p className={`${styles.state} ${styles.inActive}`}>예약마감</p>
            <p className={styles.time}>
              <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"></path></svg>
              8:00 PM - 9:00 PM
            </p>
          </div>
          <div className={styles.tickets_detail}>
            <p>정원 10 / 100</p>
            <p>강사 김도완</p>
            <p>점포명</p>
          </div>
        </article>
      </div>
  )
}

