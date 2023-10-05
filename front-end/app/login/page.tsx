'use client'

import Link from 'next/link'
import React, { useEffect, useState } from 'react'
import axios from 'axios'

import Social from '@components/social'

import styles from './page.module.scss'
import { signIn } from 'next-auth/react'

export default function Login() {
  const [username, setUserId] = useState('')
  const [password, setPassword] = useState('')

  const passwordLogin = () => {
    // 아이디, 비밀번호 빈값 체크
    if (!username) {
      alert('아이디를 입력해 주세요.')
      return
    }

    if (!password) {
      alert('비밀번호를 입력해 주세요.')
      return
    }

    axios
      .post(
        // 'http://127.0.0.1:8000/signup'
        'https://port-0-underday-2rrqq2blmyv6o6x.sel5.cloudtype.app/user/login/',
        {
          user_idxx: username,
          password: password,
        },
      )
      .then((res) => {
        if (res.data.message == 'SUCCESS') {
          console.log('로그인 성공!!!')
        }
      })
  }

  return (
    <div className={styles.login}>
      <div className={styles.loginWrap}>
        <div className={styles.inputWrap}>
          <label>휴대전화 아이디</label>
          <input
            type="text"
            placeholder="번호만 입력"
            autoComplete="off"
            value={username}
            onChange={(e) => setUserId(e.target.value)}
          ></input>
        </div>

        <div className={styles.inputWrap}>
          <label>비밀번호</label>
          <input
            type="password"
            placeholder="8~15자 영문+숫자 조합의 비밀번호 입력"
            autoComplete="off"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          ></input>
        </div>

        <button type="button" onClick={passwordLogin}>
          <span>로그인</span>
        </button>
      </div>

      <div className={styles.lineDiv}>
        <p>또는</p>
      </div>

      <Social />

      <div className={styles.joinWrap}>
        <Link href="./register/info">비밀번호 찾기</Link>
        <Link href="./register/info">회원가입</Link>
      </div>
    </div>
  )
}
