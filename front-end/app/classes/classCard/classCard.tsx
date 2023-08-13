'use client'

import Image from 'next/image'

import styles from './classCard.module.scss'

import LessonState from '@components/lessonState'
import teacherIcon from '@svg/teacher.svg'
import peopleIcon from '@svg/people.svg'
import locationIcon from '@svg/location.svg'

import { MdSportsTennis } from 'react-icons/md'
import { BsClockFill } from 'react-icons/bs'
import { GrSwim, GrYoga } from 'react-icons/gr'
import { TbStretching } from 'react-icons/tb'
import { BiDumbbell } from 'react-icons/bi'
import { useState } from 'react'
import Modal from '@components/modal'
import ClassDetails from '@components/classDetails'

interface Props {
  teacher: string
  lessonName: string
  lessonState: '예약확정' | '예약대기' | '예약마감' | '예약가능'
  category: string
}

export default function ClassCard({
  teacher,
  lessonName,
  lessonState,
  category,
}: Props) {
  const CategoryIcon = {
    수영: <GrSwim />,
    필라테스: <TbStretching />,
    요가: <GrYoga />,
    테니스: <MdSportsTennis />,
    헬스: <BiDumbbell />,
  }[category]

  const [toggleDetail, setToggleDetail] = useState(false)

  const handleClickClassCard = () => {
    setToggleDetail(true)
    console.log(teacher, lessonName)
  }

  return (
    <>
      <article className={`${styles.classCard}`} onClick={handleClickClassCard}>
        <p className={styles.category}>
          {CategoryIcon}
          {category}
        </p>
        <div className={styles.class}>
          <p className={styles.name}>{lessonName}</p>
          <LessonState lessonState={lessonState} />
          <p className={styles.time}>
            <BsClockFill />
            8:00 PM - 9:00 PM
          </p>
        </div>
        <div className={styles.info}>
          <p>
            <Image src={peopleIcon} alt="personnel" className={styles.icon} />
            정원 10 / 100
          </p>
          <p>
            <Image src={teacherIcon} alt="teacher" className={styles.icon} />
            강사 {teacher}
          </p>
          <p>
            <Image src={locationIcon} alt="location" className={styles.icon} />
            점포명
          </p>
        </div>
      </article>
      {toggleDetail && (
        <Modal>
          <ClassDetails setToggleDetail={setToggleDetail} title={lessonName} />
        </Modal>
      )}
    </>
  )
}
