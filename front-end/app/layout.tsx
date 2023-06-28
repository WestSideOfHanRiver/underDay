'use client'

import { SessionProvider } from 'next-auth/react'
import { Provider } from 'react-redux'
import './globals.css'

import { store } from './store'

import Navigation from './navigation'

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
    <SessionProvider>
      <html lang="ko">
        <body>
          <Provider store={store}>
            {children}
            <Navigation />
          </Provider>
        </body>
      </html>
    </SessionProvider>
  )
}
