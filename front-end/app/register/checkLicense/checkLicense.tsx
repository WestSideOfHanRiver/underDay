import axios from 'axios'
import { useState } from 'react'
import { useFormContext } from 'react-hook-form'

import styles from '../register.module.scss'

const CheckLicense = () => {
  const [active, setActive] = useState(false)
  const { register, getValues, setValue } = useFormContext()
  const checkLicense = () => {
    const serviceKey = process.env.LICENSE_SECRET

    axios
      .post(
        `https://api.odcloud.kr/api/nts-businessman/v1/status?serviceKey=${serviceKey}`,
        {
          b_no: [`${getValues('license').replace(/-/g, '')}`],
        },
      )
      .then((res) => res.data)
      .then((data) => {
        if (data.match_cnt > 0) {
          alert('사업자등록 번호가 인증되었습니다.')

          setValue('license', getValues('license'))
          setActive(true)
        } else {
          alert(data.data[0].tax_type)

          setActive(false)
        }
      })
      .catch(function (err) {
        console.log(err)
      })
  }

  return (
    <div className={styles.btnWrap}>
      <div className={styles.inputWrap}>
        <input
          type="text"
          placeholder="사업자등록 번호를 입력해 주세요."
          {...register('license', {
            required: {
              value: true,
              message: '사업자등록 번호를 입력해 주세요.',
            },
            validate: {
              notCheck: (value) => active || '사업자등록 번호를 인증해 주세요.',
            },
          })}
        />
      </div>

      <button type="button" className={styles.btn} onClick={checkLicense}>
        인증하기
      </button>
    </div>
  )
}

export default CheckLicense
