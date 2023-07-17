import styles from './lessonState.module.scss'

interface StateProps {
  lessonState: '예약가능' | '예약대기' | '예약마감' | '예약확정'
}

export default function LessonState({ lessonState }: StateProps) {
  const stateStyle = {
    예약가능: 'available',
    예약대기: 'standBy',
    예약마감: 'closed',
    예약확정: 'confirmed',
  }[lessonState]

  return (
    <p className={`${styles.lessonState} ${styles[stateStyle]}`}>
      {lessonState}
    </p>
  )
}
