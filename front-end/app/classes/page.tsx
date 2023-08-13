import CLASSES from './mockupData'

import Calendar from '@components/calendar'
import ClassCard from './classCard'
import AddClassButton from './addClassButton'

export default function ClassesPage() {
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
      {/* {classes.map((el, index) => (
        <ClassCard
          key={index}
          teacher={'바다표범'}
          lessonName={'저스티나'}
          lessonState={'예약가능'}
          category={'헬스'}
        />
      ))} */}
      <AddClassButton />
    </>
  )
}
