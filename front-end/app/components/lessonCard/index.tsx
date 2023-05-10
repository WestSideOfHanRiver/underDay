import Image from 'next/image'

import styles from './lessonCard.module.scss'

import { MdCancel, MdCheckCircle, MdSportsTennis } from 'react-icons/md'
import { BsClockFill } from 'react-icons/bs'
import { GrSwim, GrYoga } from 'react-icons/gr'
import { TbStretching } from 'react-icons/tb'
import { BiDumbbell } from 'react-icons/bi'

interface Props {
  teacher: string
  lessonName: string
  lessonState: string // '확정', '대기', '신청',
  category: string
}

export default function LessonCard({
  teacher,
  lessonName,
  lessonState,
  category,
}: Props) {
  const StateIcon = {
    반려: <MdCancel />,
    확정: <MdCheckCircle />,
    대기: null,
  }[lessonState]

  const CategoryIcon = {
    수영: <GrSwim />,
    필라테스: <TbStretching />,
    요가: <GrYoga />,
    테니스: <MdSportsTennis />,
    헬스: <BiDumbbell />,
  }[category]

  return (
    <article
      className={`${styles.lessonCard} 
                  ${lessonState === '반려' ? styles.denied : ''} 
                  ${lessonState === '확정' ? styles.confirmed : ''}`}
    >
      <p className={styles.time}>
        <BsClockFill className="" />
        8:00 PM - 9:00 PM
      </p>
      <p className={styles.lessonName}>{lessonName}</p>
      <div className={styles.profile}>
        <Image
          src={
            'https://image.fmkorea.com/files/attach/new/20200107/33854530/54243311/2579921739/40c8c9ae0f0ab0a4bfba2ba0a69cf632.jpg'
          }
          width={50}
          height={50}
          alt="profile-image"
        />
        <p className={styles.name}>{teacher}</p>
      </div>
      <div className={styles.extraInfo}>
        <p className={styles.category}>
          {CategoryIcon}
          {category}
        </p>
        <p
          className={`${lessonState === '반려' ? styles.denied : ''}
                      ${lessonState === '확정' ? styles.confirmed : ''}`}
        >
          {StateIcon}
          {lessonState}
        </p>
      </div>
      {lessonState === '신청' && (
        <button className={styles.applyButton}>수강 신청</button>
      )}
      {lessonState === '확정' && (
        <button className={styles.applyButton}>수강 취소</button>
      )}
      {lessonState === '대기' && (
        <button className={styles.applyButton}>대기 취소</button>
      )}
    </article>
  )
}
