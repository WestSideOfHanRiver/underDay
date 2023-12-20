'use client'

import React, { useState } from 'react'
import { useForm, FormProvider } from 'react-hook-form'
import axios from 'axios'
import { useRouter } from 'next/navigation'
import { ToastContainer, toast } from 'react-toastify'

import CheckLicense from './checkLicense/checkLicense'
import CheckAddress from './checkAddress/checkAddress'
import CheckPassword from './checkPassword/chechPassword'

import 'react-toastify/dist/ReactToastify.css'
import styles from './register.module.scss'

interface InputInfo {
  id: number
  name: string
  type: string
  title: string
  pattern?: {
    value: RegExp
    message?: string
  }
}

export interface InputAuth {
  label: string
  value: string
}

const inputAuthList: InputAuth[] = [
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
  },
]

const inputInfoList: InputInfo[] = [
  {
    id: 1,
    name: 'user_abcd',
    type: 'radio',
    title: '권한을 선택해 주세요.',
    pattern: {
      value: /^[a-zA-Z]+$/,
    },
  },
  {
    id: 2,
    name: 'user_name',
    type: 'text',
    title: '이름을 입력해 주세요.',
    pattern: {
      value: /^[a-zA-Z가-힣]+$/,
    },
  },
  {
    id: 3,
    name: 'user_phon',
    type: 'text',
    title: '휴대폰번호를 입력해 주세요.',
    pattern: {
      value: /^01(?:0|1|[6-9])-(?:\d{3}|\d{4})-\d{4}$/,
      message: '-를 포함한 휴대폰 번호를 입력해 주세요.',
    },
  },
  {
    id: 4,
    name: 'user_idxx',
    type: 'text',
    title: '아이디를 입력해 주세요.',
  },
  {
    id: 5,
    name: 'password1',
    type: 'com',
    title: '비밀번호를 입력해 주세요.',
  },
  {
    id: 6,
    name: 'company',
    type: 'text',
    title: '센터명을 입력해 주세요.',
    pattern: {
      value: /^[a-zA-Z]+$/,
    },
  },
  {
    id: 7,
    name: 'license',
    type: 'com',
    title: '사업자 번호를 입력해 주세요.',
  },
  {
    id: 8,
    name: 'address',
    type: 'com',
    title: '주소를 입력해 주세요.',
  },
]

export default function Info() {
  const router = useRouter()
  const [count, setCount] = useState(0)
  const [max, setMax] = useState(5)
  const methods = useForm({ mode: 'onChange' })

  const onSubmit = async (data: any) => {
    if (methods.getValues('user_abcd') === 'C') {
      setMax(inputInfoList.length - 1)
    }

    if (count == max) {
      await axios
        .post(
          'https://port-0-underday-local-2rrqq2blmlt9v8u.sel5.cloudtype.app/user/signup/',
          data,
        )
        .then((res) => res.data)
        .then((data) => {
          if (data.message == 'OK') {
            router.push('/')
          }
        })
        .catch((err) => {
          console.log('통신 실패', err)
        })

      return
    }

    setCount((prev) => prev + 1)
  }

  const onInvalid = (errors: Object) => {
    Object.entries(errors).map(([type, data]) => {
      toast(data.message)
    })
  }

  return (
    <>
      <div className={styles.formWrap}>
        <h2>{inputInfoList[count].title}</h2>
        <form onSubmit={methods.handleSubmit(onSubmit, onInvalid)}>
          {inputInfoList.slice(0, count + 1).map((inputInfo, index) => (
            <>
              {inputInfo.type === 'text' && (
                <div className={styles.inputWrap}>
                  <input
                    type="text"
                    placeholder={inputInfo.title}
                    {...methods.register(`${inputInfo.name}`, {
                      required: {
                        value: true,
                        message: inputInfo.title,
                      },
                      pattern: {
                        value: inputInfo.pattern?.value ?? RegExp(''),
                        message: inputInfo.pattern?.message ?? '',
                      },
                    })}
                  />
                </div>
              )}
              {inputInfo.type === 'radio' && (
                <div className={styles.radioWrap}>
                  {inputAuthList.map((inputAuth, index) => (
                    <>
                      <input
                        type="radio"
                        id={inputAuth.value}
                        value={inputAuth.value}
                        {...methods.register(`${inputInfo.name}`, {
                          required: {
                            value: true,
                            message: inputInfo.title,
                          },
                        })}
                      />
                      <label htmlFor={inputAuth.value}>{inputAuth.label}</label>
                    </>
                  ))}
                </div>
              )}

              {inputInfo.type === 'com' ? (
                <FormProvider {...methods}>
                  {inputInfo.name === 'password1' && <CheckPassword />}
                  {inputInfo.name === 'license' && <CheckLicense />}
                  {inputInfo.name === 'address' && <CheckAddress />}
                </FormProvider>
              ) : (
                ''
              )}
            </>
          ))}

          <button type="submit">다음</button>
        </form>

        <ToastContainer position="top-center" />
      </div>
    </>
  )
}
