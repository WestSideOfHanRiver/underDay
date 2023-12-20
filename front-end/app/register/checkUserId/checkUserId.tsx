import axios from 'axios'
import { useFormContext } from 'react-hook-form'

import styles from '../register.module.scss'

const CheckUserId = () => {
  const { register, getValues, setValue } = useFormContext()
  const checkUserId = () => {
    axios
      .post(
        'https://port-0-underday-local-2rrqq2blmlt9v8u.sel5.cloudtype.app/user/chkUserId/',
        {
          user_idxx: getValues('user_idxx'),
        },
      )
      .then((res) => res.data)
      .then((data) => {
        if (data.message == 'OK') {
          console.log('성공')
        } else {
          console.log('중복된 아이디 입니다.')
        }
      })
      .catch((err) => {
        console.log('통신 실패', err)
      })
  }

  return (
    <div className={styles.btnWrap}>
      <div className={styles.inputWrap}>
        <input
          type="text"
          placeholder="아이디를 입력해 주세요."
          {...register('user_idxx', { required: true })}
        />
      </div>

      <button type="button" className={styles.btn} onClick={checkUserId}>
        중복확인
      </button>
    </div>
  )
}

export default CheckUserId
