import Image from 'next/image'

import emptyIcon from '@svg/empty.png'
import styles from './empty.module.scss'

interface Props {
  message: string
}

export default function empty({ message }: Props) {
  return (
    <div className={styles.emptyPage}>
      <Image src={emptyIcon} alt="빈 페이지" />
      <p>{message}</p>
      <span>
        해당 페이지 접근이 불가능합니다.
        <br /> 자세한 내용은 담당자에게 문의해 주세요.
      </span>
    </div>
  )
}
