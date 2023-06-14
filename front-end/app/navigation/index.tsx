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
import { usePathname } from 'next/navigation'

export default function Navigation() {
  const pathname = usePathname()

  return (
    <nav className={styles.navigation}>
      <ul>
        {NAV_LIST.map(({ label, path, icon, activeIcon }) => {
          const isActive = pathname === path

          return (
            <li key={path}>
              <Link
                className={`${styles.link} ${isActive ? styles.active : ''}`}
                href={path}
              >
                {!isActive && (
                  <Image className={styles.icon} src={icon} alt={label} />
                )}
                {isActive && (
                  <Image className={styles.icon} src={activeIcon} alt={label} />
                )}
                {label}
              </Link>
            </li>
          )
        })}
      </ul>
    </nav>
  )
}

const NAV_LIST = [
  {
    label: '홈',
    path: '/',
    icon: homeIcon,
    activeIcon: homeActiveIcon,
  },
  {
    label: '수강권',
    path: '/classes',
    icon: ticketIcon,
    activeIcon: ticketActiveIcon,
  },
  {
    label: '커뮤니티',
    path: '/community',
    icon: communityIcon,
    activeIcon: communityActiveIcon,
  },
  {
    label: '마이',
    path: '/setting',
    icon: myPageIcon,
    activeIcon: myPageActiveIcon,
  },
]
