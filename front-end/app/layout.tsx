'use client'

import { SessionProvider } from 'next-auth/react'

import './globals.css'

import Navigation from './navigation'

export interface children {
  children: React.ReactNode
}

export const metadata = {
  title: 'Under Day',
  description: 'check your workout schedule and manage yours',
}

export default function RootLayout({ children }: children) {
  return (
    <>
      <SessionProvider>
        <html lang="en">
          <body>
            {children}
            <Navigation />
          </body>
        </html>
      </SessionProvider>
    </>
  )
}
