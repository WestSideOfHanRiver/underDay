'use client'

import { SessionProvider } from 'next-auth/react'
import { Provider } from 'react-redux'
import './globals.css'

import { store } from '../stores/selectedDate'

import styles from './layout.module.scss'

import Navigation from '@components/navigation'

// FIXME: use client 안 쓰도록 빼내기
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
            <main className={styles.main}>{children}</main>
            <div id="portal" />
            <Navigation />
          </Provider>
        </SessionProvider>
      </body>
    </html>
  )
}
