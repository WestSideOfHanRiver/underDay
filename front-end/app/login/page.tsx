import { signIn } from 'next-auth/react'
import Image from 'next/image'

import styles from './login.module.scss'

import KaKaoIcon from '@svg/kakao.svg'
import NaverIcon from '@svg/naver.svg'
import GoogleIcon from '@svg/google.svg'

export default function Login() {
  return (
    <div className={styles.loginWrap}>
      <div className={styles.kakao} onClick={() => signIn('kakao')}>
        <Image src={KaKaoIcon} alt="카카오톡 아이콘" />
        <span>카카오톡으로 시작하기</span>
      </div>

      <div className={styles.naver} onClick={() => signIn('naver')}>
        <Image src={NaverIcon} alt="네이버 아이콘" />
        <span>네이버로 시작하기</span>
      </div>

      <div className={styles.google} onClick={() => signIn('google')}>
        <Image src={GoogleIcon} alt="구글 아이콘" />
        <span>구글로 시작하기</span>
      </div>
    </div>
  )
}
