import { signIn } from 'next-auth/react'
import Image from 'next/image'

import styles from './social.module.scss'

import KaKaoIcon from '@svg/kakao.svg'
import NaverIcon from '@svg/naver.svg'
import GoogleIcon from '@svg/google.svg'

export default function Social() {
  return (
    <div className={styles.loginWrap}>
      <div className={styles.kakao} onClick={() => signIn('kakao')}>
        <Image src={KaKaoIcon} alt="카카오톡 아이콘" />
      </div>

      <div className={styles.naver} onClick={() => signIn('naver')}>
        <Image src={NaverIcon} alt="네이버 아이콘" />
      </div>

      <div className={styles.google} onClick={() => signIn('google')}>
        <Image src={GoogleIcon} alt="구글 아이콘" />
      </div>
    </div>
  )
}
