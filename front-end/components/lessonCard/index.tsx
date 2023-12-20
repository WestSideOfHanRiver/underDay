import Image from 'next/image'

import styles from './lessonCard.module.scss'

import LessonState from '@components/lessonState'
import teacherIcon from '@svg/teacher.svg'
import peopleIcon from '@svg/people.svg'
import locationIcon from '@svg/location.svg'

import { MdSportsTennis } from 'react-icons/md'
import { BsClockFill } from 'react-icons/bs'
import { GrSwim, GrYoga } from 'react-icons/gr'
import { TbStretching } from 'react-icons/tb'
import { BiDumbbell } from 'react-icons/bi'

interface Props {
  teacher: string
  lessonName: string
  lessonState: string
  category: string
}

export default function LessonCard({
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

  return (
    <article className={`${styles.lessonCard}`}>
      <p className={styles.category}>
        {CategoryIcon}
        {category}
      </p>
      <div className={styles.lesson}>
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
  )
}
