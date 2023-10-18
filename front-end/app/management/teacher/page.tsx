'use client'

import Link from 'next/link'
import Image from 'next/image'

import { useRouter } from 'next/navigation'
import { MdSportsTennis } from 'react-icons/md'
import { BsClockFill } from 'react-icons/bs'
import { GrSwim, GrYoga } from 'react-icons/gr'
import { TbStretching } from 'react-icons/tb'
import { BiDumbbell } from 'react-icons/bi'

import Back_btn from '../../../public/assets/svg/back_btn.svg'

export default function Teacher({ searchParams }) {
  //console.log(searchParams)

  return (
    <>
      <div className='pageTopNav'>
        <Back_btn/>
      </div>
      <h2>
        id: {searchParams.id} neme : {searchParams.name}
      </h2>
    </>
  )
}
