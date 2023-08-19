'use client'

import { SessionProvider } from 'next-auth/react'
import { Provider } from 'react-redux'
import './globals.css'

import { store } from './store'

import Navigation from './navigation'

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
            {children}
            <Navigation />
          </Provider>
        </SessionProvider>
      </body>
    </html>
  )
}
