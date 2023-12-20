import { useForm, FormProvider } from 'react-hook-form'
import { ToastContainer, toast } from 'react-toastify'
import { Dispatch, SetStateAction, useEffect, useState } from 'react'
import { TicketClasses, TicketDetails } from 'types/ticket'
import { fetchData } from '../api'

import axios from 'axios'
import Link from 'next/link'
import InputDate from '@components/datepicker'
import moment from 'moment'
import Empty from '@components/empty'

import styles from './ticketDetails.module.scss'

type Props = {
  setToggleDetail: Dispatch<SetStateAction<boolean>>
  data?: TicketDetails
}

export async function getClasses() {
  const url =
    'https://port-0-underday-local-2rrqq2blmlt9v8u.sel5.cloudtype.app/ticket/trMbshipList/'
  const classes = await fetchData(url)

  return classes
}

export default function TicketDetails({ setToggleDetail, data }: Props) {
  const status = data == undefined ? 'create' : 'update'
  const methods = useForm<TicketDetails>({ mode: 'onChange' })
  const [classes, setClasses] = useState<TicketClasses[]>()

  useEffect(() => {
    getClasses().then((res) => {
      setClasses(res)
    })
  }, [])

  const onSubmit = async (data: TicketDetails) => {
    const url =
      status == 'create'
        ? 'https://port-0-underday-local-2rrqq2blmlt9v8u.sel5.cloudtype.app/ticket/create/'
        : 'https://port-0-underday-local-2rrqq2blmlt9v8u.sel5.cloudtype.app/ticket/update/'

    await axios
      .post(url, data)
      .then((res) => res.data)
      .then((data) => {
        if (data.message == 'OK') {
          toast('회원권 생성이 완료되었습니다.')
        } else {
          console.log(data.message)
        }
      })
      .catch((err) => {
        console.log('통신 실패', err)
      })
  }

  const onInvalid = (errors: Object) => {
    Object.entries(errors).map(([type, data]) => {
      toast(data.message)
    })
  }

  if (!classes) return null

  return (
    <form
      className={styles.form}
      onSubmit={methods.handleSubmit(onSubmit, onInvalid)}
    >
      {classes.length > 0 ? (
        <>
          <p className={styles.required}>
            는 필수 입력 항목입니다.
            <br />
            해당 내용을 입력해 개별 수강권을 만들어 주세요.
          </p>

          <div className={styles.input_wrap}>
            <label className={styles.required}>사용자 ID</label>
            <input
              type="text"
              value={data?.user_member_id}
              placeholder="사용자 ID를 입력해 주세요."
              {...methods.register('user_member_id', {
                required: true,
                maxLength: 16,
              })}
            />
          </div>

          <div className={styles.input_wrap}>
            <label className={styles.required}>강의 목록</label>
            <div className={styles.select_wrap}>
              <select
                {...methods.register('class_seq')}
                value={data?.class_seq}
              >
                <option>강의 선택</option>
                {classes.map((ele: TicketClasses, index: number) => (
                  <option key={index} value={ele.tmem_numb}>
                    {ele.tmem_name}
                  </option>
                ))}
              </select>
              <i></i>
            </div>
          </div>

          <div className={styles.input_wrap}>
            <label className={styles.required}>등록 회차</label>
            <input
              type="text"
              value={data?.membership_join_number}
              placeholder="회원권 등록 회차를 입력해 주세요."
              {...methods.register('membership_join_number', {
                required: true,
                maxLength: 6,
              })}
            />
          </div>

          <div className={styles.input_wrap}>
            <label className={styles.required}>사용 회차</label>
            <input
              type="text"
              value={data?.membership_use_number}
              placeholder="회원권 사용 회차를 입력해 주세요."
              {...methods.register('membership_use_number', {
                required: true,
                maxLength: 6,
              })}
            />
          </div>

          <div className={styles.input_wrap}>
            <label className={styles.required}>사용 여부</label>
            <div className={styles.select_wrap}>
              <select
                {...methods.register('membership_use_yn')}
                value={data?.membership_use_yn}
              >
                <option value="Y">사용</option>
                <option value="P">정지</option>
                <option value="N">미사용</option>
              </select>
              <i></i>
            </div>
          </div>

          <FormProvider {...methods}>
            <div className={styles.date_wrap}>
              <div className={styles.input_wrap}>
                <label className={styles.required}>회원권 시작일</label>
                <InputDate
                  data={'membership_stat_date'}
                  title={'회원권 시작일'}
                  value={
                    data?.membership_stat_date
                      ? {
                          year: moment(
                            data?.membership_stat_date,
                            'YYYYMMDD',
                          ).year(),
                          month:
                            moment(
                              data?.membership_stat_date,
                              'YYYYMMDD',
                            ).month() + 1,
                          day: moment(
                            data?.membership_stat_date,
                            'YYYYMMDD',
                          ).date(),
                        }
                      : null
                  }
                />
              </div>

              <div className={styles.input_wrap}>
                <label className={styles.required}>회원권 종료일</label>
                <InputDate
                  data={'membership_end_date'}
                  title={'회원권 종료일'}
                  value={
                    data?.membership_end_date
                      ? {
                          year: moment(
                            data?.membership_end_date,
                            'YYYYMMDD',
                          ).year(),
                          month:
                            moment(
                              data?.membership_end_date,
                              'YYYYMMDD',
                            ).month() + 1,
                          day: moment(
                            data?.membership_end_date,
                            'YYYYMMDD',
                          ).date(),
                        }
                      : null
                  }
                />
              </div>
            </div>
          </FormProvider>

          <div className={styles.btn_wrap}>
            <button
              type="button"
              className={styles.del_btn}
              onClick={() => setToggleDetail(false)}
            >
              닫기
            </button>
            <button type="submit" className={styles.submit_btn}>
              회원권 {status == 'update' ? '수정하기' : '생성하기'}
            </button>
          </div>

          <ToastContainer position="top-center" />
        </>
      ) : (
        <>
          <Empty message={'등록된 강의가 없습니다:('} />
          <div className={styles.btn_wrap}>
            <button
              type="button"
              className={styles.del_btn}
              onClick={() => setToggleDetail(false)}
            >
              닫기
            </button>
            <Link className={styles.submit_btn} href="/">
              강의 만들기
            </Link>
          </div>
        </>
      )}
    </form>
  )
}
