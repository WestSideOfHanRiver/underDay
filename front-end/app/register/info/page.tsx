'use client'
import React from 'react'
import { useState } from 'react'

import Input from '@/components/input'

import styles from './page.module.scss'
import {useRouter} from 'next/navigation'
import axios from 'axios'

export interface inputValue {
  id: string
  value: string
}

// 비밀번호 
// 비밀번호 확인
// 사용자 구분
// 휴대폰번호
// 실명

export default function Info () {
  const maxLength = BASIC_LIST.length
  const [count, setCount] = useState(1);
  const [infoData, setInfoData] = useState<Record<string, string>>({});

  // 클릭시 다음 항목으로 이동 
  // 마지막 항목일 경우 제출
  const handleClick = () => {
    if (handleException()) {
      if (count === maxLength) {
        handleSubmit();
        return
      }

      setCount(count + 1)
    }
  }

  // 질문에 따른 정규식 테스트
  const handleException = () => {
    const checkValue = BASIC_LIST
      .slice(0, count)
      .map((item) => {
        const id = item.id;
        const regEx = item.regEx;

        // 빈 값인지 확인
        const isEmptyValue = infoData[id] === undefined || infoData[id] === null && infoData[id] === ''; 

        // 정규식이 있고 해당 정규식에 부합하지 않는지 확인
        let doesNotMatchRegex = !regEx.test(infoData[id]); 

        //예외) 비밀번호 확인의 경우 이전 비밀번호와 동일한지 비교
        if (id === 'password2') {
          doesNotMatchRegex = infoData[id] != infoData["password1"];
        }

        if (isEmptyValue || doesNotMatchRegex){
          return item.title
        } else {
          return ''
        }
      });

      const hasErrors = checkValue.some(title => title !== '');

      if (hasErrors) {
        checkValue.forEach(title => {
          if (title !== '') {
            alert(title);
          }
        });
        return false;
      } else {
        return true;
      }
  }

  // 권한 타입이 회원, 강사인 경우 설문 제출 -> 저장
  // 권한 타입이 기업인 경우 다음 페이지(기업 추가 질문)으로 이동
  const router = useRouter()
  const handleSubmit = () => {
    if (infoData.user_abcd === 'C') {
      router.push('../sub');
        // query: {
        //   detailData: JSON.stringify(infoData)
        // });
    } else {
      axios.post('', infoData, {withCredentials: true})
        .then(res => {
          console.log(res)
        })
    }
  }

  // 권한 변동될 때마다 변경
  const handleAuth = (e: { target: { id: string } }) => {
    setInfoData((prevState) => ({
      ...prevState,
      "user_abcd": e.target.id,
    }));
  }

  // 입력칸이 변동될 때마다 변경
  const handleChange = (e: { target: { id: string; value: string } }) => {
    const { id, value } = e.target;

    setInfoData((prevState) => ({
      ...prevState,
      [id]: value,
    }));
  };

  return (
    <form className={styles.form}>
      <h1 className={styles.title}>{BASIC_LIST[count - 1].title}</h1>
      <div className={styles.info}>
        <div className={styles.inputWrap}>
          {BASIC_LIST.slice(1, count).map((item, index) => (
            <Input
              key={index}
              data={item}
              event={handleChange}
            />
          ))}
        </div>
      </div>

      <div className={styles.auth}> 
        <small>권한</small>
        <div className={styles.authWrap}>
          {AUTH_LIST.map((item, index) => (
            <>
              <input 
                data-key={index}
                id={item.value} 
                type="radio" 
                name="user_abcd"
                onChange={handleAuth}
                />
              <label htmlFor={item.value}>{item.label}</label>
            </>
          ))}
        </div>
      </div>

      <button
          type="button"
          className={styles.active}
          onClick={handleClick}
        >
        <span>확인</span>
      </button>
    </form>
  )
}

const AUTH_LIST = [
  {
    label: '회원',
    value: 'A',
  },
  {
    label: '강사',
    value: 'B',
  },
  {
    label: '센터',
    value: 'C',
  }
];

const BASIC_LIST = [
  {
    id: 'user_abcd',
    title: '권한을 선택해 주세요.',
    type: '',
    label: '',
    regEx: /^[a-zA-Z]+$/,
    check: []
  },
  {
    id: 'user_name',
    title: '이름을 입력해 주세요.',
    type: 'input',
    label: '이름',
    regEx: /^[a-zA-Z]+$/,
    check: []
  },
  {
    id: 'user_phon',
    title: '휴대폰번호를 입력해 주세요.',
    type: 'input',
    label: '휴대폰번호',
    regEx: /^\d+$/,
    check: []
  },
  {
    id: 'user_numb',
    title: '아이디를 입력해 주세요.',
    type: 'input',
    label: '아이디',
    regEx: /^[a-zA-Z]+$/,
    check: []
  },
  {
    id: 'password1',
    title: '비밀번호를 입력해 주세요.',
    type: 'input',
    label: '비밀번호',
    regEx: /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.{7,10}$).*$/,
    check: [
      {
        name: '특수기호 입력',
        regex: /^(?=.*[!@#$%^&*()_+\-=[\]{};':"|,.<>/?]).+$/,
      },
      {
        name: '대문자 입력',
        regex: /^(?=.*[A-Z]).+$/,
      },
      {
        name: '7~10자리 입력',
        regex: /^.{7,10}$/,
      },
    ],
  },
  {
    id: 'password2',
    title: '비밀번호를 확인해 주세요.',
    type: 'input',
    label: '비밀번호 확인',
    regEx: /^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.{7,10}$).*$/,
    check: []
  },
]