'use client'

import Link from 'next/link'
import Image from 'next/image'
import styles from './teacher.module.scss'

import { useRouter, useSearchParams } from 'next/navigation'
import { MdSportsTennis } from 'react-icons/md'
import { BsClockFill } from 'react-icons/bs'
import { GrSwim, GrYoga } from 'react-icons/gr'
import { TbStretching } from 'react-icons/tb'
import { BiDumbbell } from 'react-icons/bi'

export default function Teacher() {
  const searchParams = useSearchParams()

  const id = searchParams?.get('id') || ''
  const name = searchParams?.get('name') || ''
  //console.log(searchParams)

  return (
    <>
      <h2>
        id: {id} neme : {name}
      </h2>
      <div className={styles.profileImage}>
        <figure>
          <img
            src="https://mblogthumb-phinf.pstatic.net/MjAyMDAzMTZfNjYg/MDAxNTg0MzIzNDY2Mjg5.SlhGMREbGgtqfqBjWeTUsO-EF5v73VsN5Z0_AFTCqP4g.Df8jH0ZvYsaG5W88evGXZVKp2HM_tpGLlcvur_RX708g.JPEG.sampgon/%ED%94%84%EB%A1%9C%ED%95%84%EC%82%AC%EC%A7%84_%EB%B9%84%ED%83%80%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4_(227).jpg?type=w800"
            alt={`${name}님 프로필 사진`}
          />
          <figcaption>{name}</figcaption>
        </figure>
      </div>
      <div>
        <div>
          <input type="checkbox" id="check_0" name="authority" />
          <label htmlFor="check_0">권한 1</label>
        </div>
        <div>
          <input type="checkbox" id="check_1" name="authority" />
          <label htmlFor="check_1">권한 2</label>
        </div>
        <div>
          <input type="checkbox" id="check_2" name="authority" />
          <label htmlFor="check_2">권한 3</label>
        </div>
      </div>
    </>
  )
}
