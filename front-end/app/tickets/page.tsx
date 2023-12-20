import { fetchData } from './api'
import { use } from 'react'
import { TicketDetails } from 'types/ticket'

import AddTicketsButton from './addTicketButton/index'
import TicketCard from './ticketsCard/ticketsCard'
import Empty from '@components/empty'

import styles from './tickets.module.scss'

export async function getTickets() {
  const url =
    'https://port-0-underday-local-2rrqq2blmlt9v8u.sel5.cloudtype.app/ticket/ticket_list/'
  const tickets = await fetchData(url)

  return tickets
}

export default function TicketsPage() {
  const tickets = use(getTickets())

  return (
    <>
      {tickets.length > 0 ? (
        <article className={styles.ticketsWrap}>
          <div className={styles.ticketsTitle}>
            <span>이용권 {tickets.length}개</span>
            <p>갖고 계시네요</p>
          </div>

          {tickets.map((el: TicketDetails) => (
            <TicketCard key={el.membership_seq} {...el} />
          ))}
        </article>
      ) : (
        <Empty message={'등록된 수강권이 없습니다:('} />
      )}

      <AddTicketsButton />
    </>
  )
}
