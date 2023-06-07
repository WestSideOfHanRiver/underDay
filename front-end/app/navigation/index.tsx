import Link from 'next/link'
import Image from 'next/image'

import styles from './navigation.module.scss'

import homeIcon from '@svg/home.svg'
import homeActiveIcon from '@svg/homeActive.svg'
import ticketIcon from '@svg/ticket.svg'
import ticketActiveIcon from '@svg/ticketActive.svg'
import communityIcon from '@svg/community.svg'
import communityActiveIcon from '@svg/communityActive.svg'
import myPageIcon from '@svg/myPage.svg'
import myPageActiveIcon from '@svg/myPageActive.svg'

export default function Navigation() {
  return (
    <nav className={styles.navigation}>
      <ul>
        {NAV_LIST.map(({ label, path, icon }) => (
          <li key={path}>
            <Link className={styles.link} href={path}>
              <Image src={icon} alt={label} width={16} height={16} />
              {label}
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  )
}

const NAV_LIST = [
  {
    label: '홈',
    path: '/',
    icon: homeIcon,
  },
  {
    label: '수강권',
    path: 'classes',
    icon: ticketIcon,
  },
  {
    label: '커뮤니티',
    path: 'community',
    icon: communityIcon,
  },
  {
    label: '마이',
    path: 'setting',
    icon: myPageIcon,
  },
]
