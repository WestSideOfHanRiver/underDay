'use client'

import { useSession, signOut } from 'next-auth/react'

import Calendar from './components/calendar'
import Login from './components/login'

export default function Home() {
  const { data: session, status } = useSession()

  if (status == 'loading') {
    return <div>loading...</div>
  }

  return (
    <>
      {session ? (
        <div>
          <Calendar />
        </div>
      ) : (
        <Login />
      )}
    </>
  )
}
