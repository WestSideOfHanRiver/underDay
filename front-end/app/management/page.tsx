import Link from 'next/link'
import Image from 'next/image'

import { MdSportsTennis } from 'react-icons/md'
import { BsClockFill } from 'react-icons/bs'
import { GrSwim, GrYoga } from 'react-icons/gr'
import { TbStretching } from 'react-icons/tb'
import { BiDumbbell } from 'react-icons/bi'

import styles from './management.module.scss'

interface Props {
  id: number
  teacher: string
  lessonName: string
  category: string
}

export default function Management({
  id,
  teacher,
  lessonName,
  category,
}: Props) {
  const datas = [
    {
      id: 123,
      teacher: '김민영',
      category: '필라테스',
      pro_img:
        'https://mblogthumb-phinf.pstatic.net/MjAyMDAzMTZfNjYg/MDAxNTg0MzIzNDY2Mjg5.SlhGMREbGgtqfqBjWeTUsO-EF5v73VsN5Z0_AFTCqP4g.Df8jH0ZvYsaG5W88evGXZVKp2HM_tpGLlcvur_RX708g.JPEG.sampgon/%ED%94%84%EB%A1%9C%ED%95%84%EC%82%AC%EC%A7%84_%EB%B9%84%ED%83%80%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4_(227).jpg?type=w800',
    },
    {
      id: 892,
      teacher: '최지영',
      category: '요가',
      pro_img:
        'data:image/jpeg;base64,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',
    },
    {
      id: 8235,
      teacher: '이미지',
      category: '헬스',
      pro_img:
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp8bmA6Wo8AgCeZqRtAbu304L7t9PoJtD0-Q&usqp=CAU',
    },
  ]
  return (
    <>
      <main className={styles.main}>
        <ul className={styles.ul}>
          {datas.map((a, i) => {
            return (
              <li className={styles.list} data-id={datas[i].id} key={i}>
                <figure className={styles.pro_img}>
                  <img src={datas[i].pro_img} alt={datas[i].teacher}></img>
                </figure>

                <p>{datas[i].teacher}</p>
                <p>{datas[i].category}</p>
                <Link href="/">정보보기</Link>
              </li>
            )
          })}
        </ul>
      </main>
    </>
  )
}
