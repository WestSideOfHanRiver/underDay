'use client'

import { useSearchParams } from 'next/navigation'

export default function Teacher() {
  const searchparams = useSearchParams()

  const id = searchparams.get('id')
  const name = searchparams.get('name')

  return (
    <>
      <h2>
        id: {id} name : {name}
      </h2>
    </>
  )
}
