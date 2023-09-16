import TICKETS from './mockupData';
import AddTicketsButton from './addTicketButton/index';
import TicketCard from './ticketsCard/ticketsCard';

import styles from "./tickets.module.scss";

export default function TicketsPage() {
    return (
        <main className={styles.main}>
            <AddTicketsButton/> 

            <TicketCard/>
        </main>
    )
};
