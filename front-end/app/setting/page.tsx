'use client'

import Image from 'next/image'
import styles from './setting.module.scss'
import Link from 'next/link'
import PorfileImg from '/public/test_img/profile_0.png'

export default function Setting() {
  return (
    <>
      <main className={styles.main}>
        <h2 className="blind">사용자 설정화면</h2>
        <SettingHead></SettingHead>
        <Profile></Profile>
      </main>
    </>
  )
}

const SettingHead = () => {
  return (
    <nav className={styles.settingNav}>
      <Link
        href="#"
        onClick={(e) => {
          e.preventDefault()
          alert('프로필 선택!!')
        }}
      >
        heungsoo89
      </Link>
    </nav>
  )
}

const Profile = () => {
  return (
    <section>
      <h3 className="blind">마이페이지</h3>
      <div className={styles.profile_info}>
        <div className={styles.profileImgBox}>
          <figure>
            <Image src={PorfileImg} alt="프로필 이미지" />
          </figure>
        </div>
        <strong>아무개</strong>
        <a href="tel:010-4043-4240" className={styles.tel}>
          010-4043-4240
        </a>
      </div>
      <ul className={styles.category}>
        <li>#필라테스</li>
        <li>#PT</li>
      </ul>
      <ul className={styles.menu}>
        <li>
          <Link 
          href="#"
          onClick={(e) => {
              e.preventDefault()
              alert('프로필 편집!!')
            }}
          >
            <span>프로필 편집</span>
          </Link>
        </li>
        <li>
          <Link 
          href="#"
          onClick={(e) => {
              e.preventDefault()
              alert('프로필 공유!!')
            }}
          >
            <span>프로필 공유</span>
          </Link>
        </li>
      </ul>
    </section>
  )
}

const ProfileSelecter = () => {
  return (
    <div className={styles.profileSelecterModal}>
      <div className={styles.profileSelecter}>
        <ul>
          <li>
            <a href="#">프로필1(기업)</a>
          </li>
          <li>
            <a href="#">프로필2(강사)</a>
          </li>
          <li>
            <a href="#">프로필3(회원)</a>
          </li>
        </ul>
      </div>
    </div>
  )
}
