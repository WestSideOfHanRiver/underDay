'use client'

import Link from 'next/link'
import React, { useState } from 'react'
import axios from 'axios'
import { setCookie } from '@utils/cookie'

import Social from '@components/social'

import styles from './login.module.scss'

export default function Login() {
  const [username, setUserId] = useState('')
  const [password, setPassword] = useState('')

  const passwordLogin = async () => {
    // 아이디, 비밀번호 빈값 체크
    if (!username) {
      alert('아이디를 입력해 주세요.')
      return
    }

    if (!password) {
      alert('비밀번호를 입력해 주세요.')
      return
    }

    await axios
      .post(
        'https://port-0-underday-local-2rrqq2blmlt9v8u.sel5.cloudtype.app/user/login/',
        {
          user_idxx: username,
          password: password,
        },
      )
      .then((res) => res.data)
      .then((data) => {
        if (data.message == 'OK') {
          console.log('성공')
        } else {
          console.log('아이디, 비밀번호를 다시 확인해 주세요.')
        }
      })
      .catch((err) => {
        console.log('통신 실패', err)
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
        <Link href="./register">비밀번호 찾기</Link>
        <Link href="./register">회원가입</Link>
      </div>
    </div>
  )
}
