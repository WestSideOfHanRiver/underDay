'use client'

import { SessionProvider } from 'next-auth/react'
import { Provider } from 'react-redux'
import './globals.css'

import { store } from '../stores/selectedDate'

import styles from '../styles/default.module.scss'

import Navigation from '@components/navigation'

// export const metadata = {
//   title: 'Under Day',
//   description: 'check your workout schedule and manage yours',
// }

export interface children {
  children: React.ReactNode
}

export default function RootLayout({ children }: children) {
  return (
    <html lang="ko">
      <body>
        <SessionProvider>
          <Provider store={store}>
            <div className={styles.wrap}>
              <main className={styles.main}>{children}</main>
              <div id="portal" />
              <Navigation />
            </div>
          </Provider>
        </SessionProvider>
      </body>
    </html>
  )
}
