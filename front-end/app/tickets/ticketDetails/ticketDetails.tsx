import { useForm, SubmitHandler, Controller } from 'react-hook-form'
import { Dispatch, SetStateAction } from 'react'
import InputDate from '@components/datepicker'

import styles from './ticketDetails.module.scss'

type Inputs = {
  user_numb: string // 사용자 ID
  tmem_numb: string // 강사 수업 일련번호
  umem_stat: string // 회원권 이용 시작 일시
  umem_endt: string // 회원권 이용 종료 일시
  umem_tnum: string // 회원권 등록 회차
  umem_unum: string // 회원권 사용 회차
  umem_ysno: string // 회원권 사용 가능 여부
  umem_inst: string // 회원권 등록 일시
}

interface Props {
  setToggleDetail: Dispatch<SetStateAction<boolean>>
  data: object
}

export default function TicketDetails({ setToggleDetail, data }: Props) {
  console.log(data)

  const {
    control,
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()
  const onSubmit: SubmitHandler<Inputs> = (data) => console.log(data)

  return (
    <>
      <form className={styles.form} onSubmit={handleSubmit(onSubmit)}>
        <div className={styles.topWrap}>
          <p className={styles.required}>
            는 필수 입력 항목입니다.
            <br />
            해당 내용을 입력해 개별 수강권을 만들어 주세요.
          </p>
          <button
            type="button"
            className={styles.closeBtn}
            onClick={() => setToggleDetail(false)}
          ></button>
        </div>

        <div className={styles.inputWrap}>
          <label className={styles.required}>사용자 ID</label>
          <input
            type="text"
            placeholder="사용자 ID를 입력해 주세요."
            {...register('user_numb', { required: true, maxLength: 16 })}
          />
        </div>

        <div className={styles.inputWrap}>
          <label className={styles.required}>강의 목록</label>
          <div className={styles.selectWrap}>
            <select {...register('tmem_numb')}>
              <option value="수업일련번호1">수업일련번호1</option>
              <option value="수업일련번호2">수업일련번호2</option>
              <option value="수업일련번호3">수업일련번호3</option>
            </select>
            <i></i>
          </div>
        </div>

        <div className={styles.dateWrap}>
          <div>
            <label className={styles.required}>시작일</label>
            <Controller
              name={'umem_stat'}
              control={control}
              rules={{ required: true }}
              render={({ field: { onChange, name } }) => (
                <InputDate
                  title={'회원권 시작일을 입력해 주세요.'}
                  position={'bottom'}
                  onChange={onChange}
                />
              )}
            />
          </div>

          <div>
            <label className={styles.required}>회원권 종료일</label>
            <Controller
              name={'umem_endt'}
              control={control}
              rules={{ required: true }}
              render={({ field: { onChange, name } }) => (
                <InputDate
                  title={'회원권 종료일을 입력해 주세요.'}
                  position={'bottom'}
                  onChange={onChange}
                />
              )}
            />
          </div>
        </div>

        <div className={styles.inputWrap}>
          <label className={styles.required}>등록 회차</label>
          <input
            type="text"
            placeholder="회원권 등록 회차를 입력해 주세요."
            {...register('umem_tnum', { required: true, maxLength: 6 })}
          />
        </div>

        <div className={styles.inputWrap}>
          <label className={styles.required}>사용 회차</label>
          <input
            type="text"
            placeholder="회원권 사용 회차를 입력해 주세요."
            {...register('umem_unum', { required: true, maxLength: 6 })}
          />
        </div>

        <div className={styles.inputWrap}>
          <label className={styles.required}>사용 여부</label>
          <div className={styles.radioWrap}>
            <input
              type="radio"
              id="umem_yes"
              value="Y"
              {...register('umem_ysno', { required: true })}
            />
            <label htmlFor="umem_yes">사용</label>

            <input
              type="radio"
              id="umem_no"
              value="P"
              {...register('umem_ysno', { required: true })}
            />
            <label htmlFor="umem_no">정지</label>

            <input
              type="radio"
              id="umem_pause"
              value="N"
              {...register('umem_ysno', { required: true })}
            />
            <label htmlFor="umem_pause">미사용</label>
          </div>
        </div>

        <div className={styles.inputWrap}>
          <label className={styles.required}>등록 일자</label>
          <Controller
            name={'umem_unum'}
            control={control}
            rules={{ required: true }}
            render={({ field: { onChange, name } }) => (
              <InputDate
                title={'회원권 등록 일자를 입력해 주세요.'}
                position={'top'}
                onChange={onChange}
              />
            )}
          />
        </div>

        <div className={styles.btnWrap}>
          <button
            type="submit"
            className={styles.submit_btn}
            onClick={() => setToggleDetail(true)}
          >
            회원권 생성하기
          </button>
        </div>
      </form>
    </>
  )
}
