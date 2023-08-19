'use client'

import { useSession, signOut } from 'next-auth/react'

import styles from './page.module.scss'

import LessonCard from './components/lessonCard'
import Calendar from './components/calendar'

import { Inter } from 'next/font/google'
import Login from './login/page'

const DUMMY = [
  {
    category: '요가',
    teacher: '조완석',
    lessonName: '다리 찢어보자 요가킹',
    lessonState: '신청',
  },
  {
    category: '헬스',
    teacher: '김도완',
    lessonName: 'Muscle Up for One Night Stand',
    lessonState: '대기',
  },
  {
    category: '필라테스',
    teacher: '진가영',
    lessonName: '고무고무 필라테스',
    lessonState: '확정',
  },
  {
    category: '수영',
    teacher: '김부건',
    lessonName:
      '이 수업은 엄청 긴 이름으로 지어져서 어디서 생략해야할지 보기위한',
    lessonState: '반려',
  },
  {
    category: '테니스',
    teacher: '김수한무두루미와',
    lessonName: 'hI',
    lessonState: '15명/15명 대기 9 ',
  },
]

export default function Home() {
  const { data: session, status } = useSession()
  const categories = ['전체', ...new Set(DUMMY.map(({ category }) => category))]

  // FIXME: 수정 필요
  if (status == 'loading') {
    return <div>loading...</div>
  }

  if (!session) {
    return <Login />
  }

  return (
    <main className={styles.main}>
      <Calendar />
      <select name="" id="">
        {categories.map((category) => (
          <option key={category}>{category}</option>
        ))}
      </select>
      <label htmlFor="">Day</label>
      {DUMMY.map(({ teacher, lessonName, lessonState, category }) => (
        <LessonCard
          teacher={teacher}
          lessonName={lessonName}
          lessonState={lessonState}
          category={category}
          key={lessonName} // 수정 해야함
        />
      ))}
    </main>
  )
}
