'use client'

import './globals.css'
import { SessionProvider } from 'next-auth/react'

export interface children {
  children: React.ReactNode
}

export default function RootLayout({ children }: children) {
  return (
    <>
      <SessionProvider>
        <html lang="en">
          <body>{children}</body>
        </html>
      </SessionProvider>
    </>
  )
}
