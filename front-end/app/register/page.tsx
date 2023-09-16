"use client" 

import React, { useState } from 'react';
import { useForm, FormProvider } from 'react-hook-form';
import { error } from 'console';
import axios from 'axios';
import CheckLicense from './checkLicense/checkLicense';
import CheckAddress from './checkAddress/checkAddress';

import styles from './register.module.scss'

interface InputInfo {
  id: number;
  name: string;
  type: string;
  title: string;
  pattern: RegExp;
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
  }
];

const inputInfoList: InputInfo[] = [
  {
    id: 1,
    name: 'user_abcd',
    type: 'radio',
    title: '권한을 선택해 주세요.',
    pattern: /^[a-zA-Z]+$/,
  },
  {
    id: 2,
    name: 'user_name',
    type: 'text',
    title: '이름을 입력해 주세요.',
    pattern: /^[a-zA-Z]+$/,
  },
  {
    id: 3,
    name: 'user_phon',
    type: 'text',
    title: '휴대폰번호를 입력해 주세요.',
    pattern: /^\d+$/,
  },
  {
    id: 4,
    name: 'user_numb',
    type: 'text',
    title: '아이디를 입력해 주세요.',
    pattern: /^[a-zA-Z]+$/,
  },
  {
    id: 5,
    name: 'password1',
    type: 'text',
    title: '비밀번호를 입력해 주세요.',
    pattern: /^[a-zA-Z]+$/,
  },
  {
    id: 6,
    name: 'password2',
    type: 'text',
    title: '비밀번호를 확인해 주세요.',
    pattern: /^[a-zA-Z]+$/,
  },
  {
    id: 7,
    name: 'company',
    type: 'text',
    title: '센터명을 입력해 주세요.',
    pattern: /^[a-zA-Z]+$/,
},
  {
      id: 8,
      name: 'address',
      type: 'com',
      title: '주소를 입력해 주세요.',
      pattern: /^[a-zA-Z]+$/,
  },
  {
      id: 9,
      name: 'license',
      type: 'com',
      title: '사업자 번호를 입력해 주세요.',
      pattern: /^[a-zA-Z]+$/,
  }
]

export default function Info() {
  const [ count , setCount ] = useState(0);
  const [ max , setMax ] = useState(5);
  const methods = useForm({mode: "onChange"});

  const onSubmit = (data: any) => {
    if (methods.getValues("user_abcd") === 'C') {
      setMax(inputInfoList.length - 1);
    }

    if ( count == max ) {
      console.log(data);

      axios.post('', {data}, {withCredentials: true}
        ).then(() => {
          console.log('');
        }).catch((error) => {
          console.dir(error);
        });
      
      return
    } 

    setCount(count + 1);
  } 

  const onInvalid = (errors: any) => {
    alert(inputInfoList[count].title);
  };

  return (
    <>
      <div className={styles.formWrap}>
        <h2>{inputInfoList[count].title}</h2>
        <form onSubmit={methods.handleSubmit(onSubmit, onInvalid)}>

          {inputInfoList.slice(0, count + 1).map((inputInfo, index) => (
            <>
              {
                inputInfo.type === 'text' &&
                  <div className={styles.inputWrap}>
                    <input type="text" placeholder={inputInfo.title} {...methods.register(`${inputInfo.name}`, {required: true, pattern: inputInfo.pattern })}/>
                    <label htmlFor={inputInfo.name}>{inputInfo.title}</label>
                  </div>
              }

              {
                inputInfo.type === 'radio' &&
                  <div className={styles.radioWrap}>
                    {inputAuthList.map((inputAuth, index) => (
                      <>
                        <input type="radio" id={inputAuth.value} value={inputAuth.value} {...methods.register(`${inputInfo.name}`, {required: true})}/>
                        <label htmlFor={inputAuth.value}>{inputAuth.label}</label>
                      </>
                    ))}
                  </div> 
              }

              {
                inputInfo.type === 'com' ? 
                  <FormProvider {...methods}>
                    {inputInfo.name === 'license' && <CheckLicense/>}
                    {inputInfo.name === 'address' && <CheckAddress/>}
                  </FormProvider> : ''
              }
            </>
          ))}

          <button type="submit">다음</button>
        </form>
      </div>
    </>
  );
}
