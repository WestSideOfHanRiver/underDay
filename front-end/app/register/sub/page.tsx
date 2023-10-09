'use client'
import React from 'react'
import { useState } from 'react'
import { useRouter, useSearchParams } from 'next/navigation'

import Input from '@components/input'

import styles from '../info/page.module.scss'

export interface inputValue {
  id: string
  value: string
}

// 센터명
// 주소
// 사업자 번호

// 추가사항 -> 사업자 번호 검증 , 주소 API

export default function Sub() {
  const router = useRouter()
  console.log(useSearchParams()?.get('detailData'))

  const maxLength = SUB_LIST.length
  const [count, setCount] = useState(1)
  const [infoData, setInfoData] = useState<Record<string, string>>({})

  // 클릭시 다음 항목으로 이동
  // 마지막 항목일 경우 제출
  const handleClick = () => {
    if (handleException()) {
      if (count === maxLength) {
        handleSubmit()
        return
      }

      setCount(count + 1)
    }
  }

  // 질문에 따른 정규식 테스트
  const handleException = () => {
    const checkValue = SUB_LIST.slice(0, count).map((item) => {
      const id = item.id
      const regEx = item.regEx

      // 빈 값인지 확인
      const isEmptyValue =
        infoData[id] === undefined ||
        (infoData[id] === null && infoData[id] === '')

      // 정규식이 있고 해당 정규식에 부합하지 않는지 확인
      let doesNotMatchRegex = !regEx.test(infoData[id])

      if (isEmptyValue || doesNotMatchRegex) {
        return item.title
      } else {
        return ''
      }
    })

    const hasErrors = checkValue.some((title) => title !== '')

    if (hasErrors) {
      checkValue.forEach((title) => {
        if (title !== '') {
          alert(title)
        }
      })
      return false
    } else {
      return true
    }
  }

  // 제출
  const handleSubmit = () => {
    console.log(infoData)
  }

  // 입력칸이 변동될 때마다 변경
  const handleChange = (e: { target: { id: string; value: string } }) => {
    const { id, value } = e.target

    setInfoData((prevState) => ({
      ...prevState,
      [id]: value,
    }))
  }

  return (
    <form className={styles.form}>
      <h1 className={styles.title}>{SUB_LIST[count - 1].title}</h1>

      <div className={styles.info}>
        <div className={styles.inputWrap}>
          {SUB_LIST.slice(0, count).map((item, index) => (
            <Input key={index} data={item} event={handleChange} />
          ))}
        </div>
      </div>

      <button type="button" className={styles.active} onClick={handleClick}>
        <span>확인</span>
      </button>
    </form>
  )
}

const SUB_LIST = [
  {
    id: 'company',
    title: '센터명을 입력해 주세요.',
    type: 'input',
    label: '센터명',
    regEx: /^[a-zA-Z]+$/,
    check: [],
  },
  {
    id: 'address',
    title: '주소를 입력해 주세요.',
    type: 'input',
    label: '주소',
    regEx: /^[a-zA-Z]+$/,
    check: [],
  },
  {
    id: 'license',
    title: '사업자 번호를 입력해 주세요.',
    type: 'input',
    label: '사업자 번호',
    regEx: /^[a-zA-Z]+$/,
    check: [],
  },
]
