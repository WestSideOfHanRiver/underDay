'use client'

import Image from 'next/image'
import styles from '../setting.module.scss'
import Link from 'next/link'
import PorfileImg from '/public/test_img/profile_0.png'

export default function Setting() {
  return (
    <>
      <main className={styles.main}>
        <SettingHead></SettingHead>
        <Profile></Profile>
        <ProfileFrom></ProfileFrom>
        <CareerFrom></CareerFrom>
        <CategoryList></CategoryList>
      </main>
    </>
  )
}

const SettingHead = () => {
  return (
    <nav className={styles.settingNav}>
        <Link
        href='#'
        className={styles.back}
        >
            <span className='blind'>뒤로가기</span>
        </Link>
      <h2>프로필 편집</h2>
    </nav>
  )
}

const Profile = () => {
  return (
    <section>
      <h3 className='blind'>프로필 정보</h3>
      <div className={styles.profile_info}>
        <div className={styles.profileImgBox}>
          <figure>
            <Image src={PorfileImg} alt="프로필 이미지" />
          </figure>
          <Link
            href='#'
          >
             <span>프로필 수정</span>
          </Link>
         
        </div>

      </div>
    </section>
    
  )
}

const ProfileFrom = () =>{
    return(
        <article className={styles.profileFrom}>
            <h4 className='blind'>정보입력</h4>
            <div>
                <label>닉네임</label>
                <input type="text" placeholder='닉네임을 입력해주세요.'/>
            </div>
            <div>
                <label>전화번호</label>
                <input type="text" placeholder='전화번호를 입력해주세요.'/>
            </div>
            <div>
                <label>주소</label>
                <input type="text" placeholder='기본주소'/>
                <input type="text" placeholder='상세주소'/>
            </div>
        </article>
    )
}

const CareerFrom = () =>{
    return(
        <article className={styles.CareerFrom}>
            <h4>경력</h4>
            <div>
                <button type='button' className={styles.addCareer}>경력추가 +</button>
                <ul>
                    <li>
                        <input type="text" value="경력 1"/>
                        <button type="button"><span className=''>삭제</span></button>
                    </li>
                    <li>
                        <input type="text" value="경력 2"/>
                        <button type="button"><span className='='>삭제</span></button>
                    </li>
                </ul>
            </div>
        </article>
    )
}


const CategoryList = () =>{
    return(
        <article>
            <h4>카테고리</h4>
            <ul>
                <li><button type="button">#필라테스</button></li>
                <li><button type="button">#헬스</button></li>
                <li><button type="button">#수영</button></li>
            </ul>
        </article>
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
