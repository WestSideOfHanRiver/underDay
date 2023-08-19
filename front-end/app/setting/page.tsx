import styles from './setting.module.scss'

export default function Setting() {
  return (
    <section>
      <h2 className="blind">프로필선택</h2>
      <button type="button" className={styles.select_profile}>
        heungsoo89
      </button>
    </section>
  )
}
