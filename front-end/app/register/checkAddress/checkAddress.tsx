import { useState } from 'react'
import DaumPostcode from 'react-daum-postcode'
import { useFormContext } from 'react-hook-form'

import styles from '../register.module.scss'

const CheckAddress = () => {
  const { register, setValue } = useFormContext()

  const [openPostcode, setOpenPostcode] = useState<boolean>(false)
  const handlePostCode = {
    clickButton: () => {
      setOpenPostcode((current) => !current)
    },

    selectAddress: (data: any) => {
      console.log(`
                주소: ${data.address},
                우편번호: ${data.zonecode}
            `)
      setOpenPostcode(false)
      setValue('address', data.address)
    },
  }

  return (
    <div className={styles.comWrap}>
      <div className={styles.btnWrap}>
        <div className={styles.inputWrap}>
          <input
            type="text"
            placeholder="주소를 입력해 주세요."
            {...register('address', {
              disabled: true,
              required: {
                value: true,
                message: '주소를 입력해 주세요.',
              },
            })}
          />
        </div>

        <button
          type="button"
          className={styles.btn}
          onClick={handlePostCode.clickButton}
        >
          주소검색
        </button>
      </div>

      {openPostcode && (
        <DaumPostcode
          onComplete={handlePostCode.selectAddress}
          autoClose={false}
          defaultQuery="판교역로 235"
        />
      )}
    </div>
  )
}

export default CheckAddress
