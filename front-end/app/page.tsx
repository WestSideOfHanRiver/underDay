'use client'

import { useSession, signOut } from 'next-auth/react'
import { Noto_Sans_KR } from 'next/font/google'

import LessonCard from './components/lessonCard'
import Calendar from '@components/calendar'

import Lottie from 'lottie-react'
import Loding from './assets/svg/loding.json'

// import Login from './login'

const notoSans = Noto_Sans_KR({
  weight: '500',
  display: 'fallback',
  subsets: ['latin'],
  style: 'normal',
  variable: '--noto-sans_KR-bold',
  fallback: ['system-ui'],
})

const DUMMY = [
  {
    category: '요가',
    teacher: '조완석',
    lessonName: '다리 찢어보자 요가킹',
    lessonState: '예약대기',
  },
  {
    category: '헬스',
    teacher: '김도완',
    lessonName: 'Muscle Up for One Night Stand',
    lessonState: '예약마감',
  },
  {
    category: '필라테스',
    teacher: '진가영',
    lessonName: '고무고무 필라테스',
    lessonState: '예약확정',
  },
  {
    category: '수영',
    teacher: '김부건',
    lessonName:
      '이 수업은 엄청 긴 이름으로 지어져서 어디서 생략해야할지 보기위한',
    lessonState: '예약가능',
  },
]

export default function Home() {
  const { data: session, status } = useSession()
  const categories = ['전체', ...new Set(DUMMY.map(({ category }) => category))]

  // FIXME: 수정 필요
  if (status == 'loading') {
    return (
      <div>
        <Lottie animationData={Loding} />
      </div>
    )
  }

  // if (!session) {
  //   return <Login />
  // }

  return (
    <>
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
          lessonState={
            lessonState as '예약마감' | '예약확정' | '예약대기' | '예약가능'
          }
          category={category}
          key={lessonName} // 수정 해야함
        />
      ))}
    </>
  )
}
