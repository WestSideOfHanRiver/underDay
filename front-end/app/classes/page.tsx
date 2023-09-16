import CLASSES from './mockupData'

import { fetchData } from './api'

import Calendar from '@components/calendar'
import ClassCard from './classCard'
import AddClassButton from './addClassButton'

export default async function ClassesPage() {
  const classes = await fetchData()

  return (
    <>
      <Calendar />
      <ClassCard
        teacher="김부건"
        lessonName={'저스티나'}
        lessonState={'예약가능'}
        category={'헬스'}
      />
      {CLASSES.map((el) => (
        <ClassCard
          key={el.classId}
          teacher={'바다표범'}
          lessonName={'저스티나'}
          lessonState={'예약가능'}
          category={'헬스'}
        />
      ))}
      {classes.length === 0 && <h2>등록된 강의가 없습니다.</h2>}
      <AddClassButton />
    </>
  )
}
