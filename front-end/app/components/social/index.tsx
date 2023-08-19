import { signIn } from 'next-auth/react'
import Image from 'next/image'

import styles from './social.module.scss'

import Kakao from '../../assets/svg/kakao.svg'
import Naver from '../../assets/svg/naver.svg'
import Google from '../../assets/svg/google.svg'

export default function Social() {
  return (
    <div className={styles.loginWrap}>
      <div className={styles.kakao} onClick={() => signIn('kakao')}>
        <Image src={Kakao} alt="카카오톡 아이콘" />
      </div>

      <div className={styles.naver} onClick={() => signIn('naver')}>
        <Image src={Naver} alt="네이버 아이콘" />
      </div>

      <div className={styles.google} onClick={() => signIn('google')}>
        <Image src={Google} alt="구글 아이콘" />
      </div>
    </div>
  )
}
