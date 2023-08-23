import styles from './classes.module.scss'

export default function Classes() {
  return (
    <main className={styles.main}>
      <div className={styles.content}>
        <article className={styles.classCard_wrap}>
          <div className={styles.classCard_info}>
            <p className={styles.name}>Muscle Up for One Night Stand</p>
            <p className={`${styles.state} ${styles.inActive}`}>예약마감</p>
            <p className={styles.time}>
              <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"></path></svg>
              8:00 PM - 9:00 PM
            </p>
          </div>
          <div className={styles.classCard_detail}>
            <p>정원 10 / 100</p>
            <p>강사 김도완</p>
            <p>점포명</p>
          </div>
        </article>

        <article className={styles.classCard_wrap}>
          <div className={styles.classCard_info}>
            <p className={styles.name}>Muscle Up for One Night Stand</p>
            <p className={`${styles.state} ${styles.active}`}>예약마감</p>
            <p className={styles.time}>
              <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"></path></svg>
              8:00 PM - 9:00 PM
            </p>
          </div>
          <div className={styles.classCard_detail}>
            <p>정원 10 / 100</p>
            <p>강사 김도완</p>
            <p>점포명</p>
          </div>
        </article>
      </div>
    </main>
  )
}

const CLASSES_LIST = [
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
