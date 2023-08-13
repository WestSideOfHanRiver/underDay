'use client'

import { ReactNode, useEffect, useState } from 'react'
import { createPortal } from 'react-dom'

import { allowScrollY, preventScrollY } from '@utils/scroll'

interface Props {
  children: ReactNode
}

export default function Modal({ children }: Props) {
  const [isMounted, setIsMounted] = useState(false)

  useEffect(() => {
    setIsMounted(true)

    const prev = preventScrollY()

    return () => {
      allowScrollY(prev)
    }
  }, [])

  return isMounted
    ? createPortal(children, document.querySelector('#portal')!)
    : null
}
