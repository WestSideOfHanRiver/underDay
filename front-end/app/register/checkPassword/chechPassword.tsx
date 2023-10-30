import { useFormContext } from 'react-hook-form'

import styles from '../register.module.scss'

interface Check {
  name: string
  regex: RegExp
}

const checkList: Check[] = [
  {
    name: '특수기호 입력',
    regex: /^(?=.*[!@#$%^&*()_+\-=[\]{};':"|,.<>/?]).+$/,
  },
  {
    name: '대문자 입력',
    regex: /^(?=.*[A-Z]).+$/,
  },
  {
    name: '9-12자리 입력',
    regex: /^(?!.*undefined).{9,12}$/,
  },
]

const CheckPassword = () => {
  const { register, watch } = useFormContext()

  return (
    <div className={styles.inputWrap}>
      <input
        type="password"
        placeholder="비밀번호를 확인해 주세요."
        {...register('password2', {
          required: {
            value: true,
            message: '비밀번호를 입력해 주세요.',
          },
          pattern: {
            value: new RegExp(`^${watch('password1')}$`),
            message: '비밀번호를 확인해 주세요.',
          },
        })}
      />

      <input
        type="password"
        placeholder="비밀번호를 입력해 주세요."
        {...register('password1', {
          required: {
            value: true,
            message: '비밀번호를 입력해 주세요.',
          },
          pattern: {
            value:
              /^(?=.*[!@#$%^&*()_+\-=[\]{};':"|,.<>/?])(?=.*[A-Z]).{9,12}$/,
            message: '문자, 숫자, 특수문자를 최소 1자리 이상 혼합해 주세요.',
          },
          validate: {
            notVaild: (value) =>
              !RegExp(/(\d){10,}/).test(value) ||
              !RegExp(/(\w){10,}/).test(value) ||
              '연속된 비밀번호 입니다. 다른 비밀번호를 입력해 주세요.',
          },
        })}
      />

      <div className={styles.inputExcep}>
        {checkList.map((item, index) => {
          return (
            <small
              key={index}
              className={
                item.regex.test(watch('password1')) ? `${styles.active}` : ''
              }
            >
              {item.name}
            </small>
          )
        })}
      </div>
    </div>
  )
}

export default CheckPassword
