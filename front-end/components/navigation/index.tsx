import Link from 'next/link'
import Image from 'next/image'
import { usePathname } from 'next/navigation'

import styles from './navigation.module.scss'

import homeIcon from '@svg/home.svg'
import homeActiveIcon from '@svg/homeActive.svg'
import ticketIcon from '@svg/ticket.svg'
import ticketActiveIcon from '@svg/ticketActive.svg'
import communityIcon from '@svg/community.svg'
import communityActiveIcon from '@svg/communityActive.svg'
import myPageIcon from '@svg/myPage.svg'
import myPageActiveIcon from '@svg/myPageActive.svg'
import classIcon from '@svg/class.svg'
import classActiveIcon from '@svg/classActive.svg'

export default function Navigation() {
  const pathname = usePathname()

  return (
    <nav className={styles.navigation}>
      <ul>
        {NAV_LIST.map(({ label, path, icon, activeIcon }) => {
          const isActive =
            (path === '/' && pathname === '/') ||
            (pathname !== '/' && path.startsWith(pathname!))

          return (
            <li key={path}>
              <Link
                className={`${styles.link} ${isActive ? styles.active : ''}`}
                href={path}
              >
                <Image
                  className={styles.icon}
                  src={isActive ? activeIcon : icon}
                  alt={label}
                  width={24}
                  height={24}
                />
                {label}
              </Link>
            </li>
          )
        })}
      </ul>
    </nav>
  )
}

// FIXME: 로그인한 User type(고객, 강사, 기업)에 따라 다르게 뿌려야함
const NAV_LIST = [
  {
    label: '홈',
    path: '/',
    icon: homeIcon,
    activeIcon: homeActiveIcon,
  },
  {
    label: '강의',
    path: '/classes',
    icon: classIcon,
    activeIcon: classActiveIcon,
  },
  {
    label: '수강권',
    path: '/tickets',
    icon: ticketIcon,
    activeIcon: ticketActiveIcon,
  },
  {
    label: '회원관리',
    path: '/membership',
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
