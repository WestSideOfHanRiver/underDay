'use client'

import Navigation from './navigation'
import './globals.css'
import { SessionProvider } from 'next-auth/react'

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
      <html lang="en">
        <body>
          {children}
          <Navigation />
        </body>
      </html>
    </SessionProvider>
  )
}
