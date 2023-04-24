import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from './page.module.scss'

import { useState } from 'react'

import Calendar from './components/calendar'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <main>
      <Calendar />
    </main>
  )
}
