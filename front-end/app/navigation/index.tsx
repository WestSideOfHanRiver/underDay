import Link from 'next/link'

import styles from './navigation.module.scss'

import { AiFillSetting, AiFillHome } from 'react-icons/ai'
import { HiChatBubbleLeftRight } from 'react-icons/hi2'
import { FaTicketAlt } from 'react-icons/fa'

export default function Navigation() {
  return (
    <nav className={styles.navigation}>
      <ul>
        {NAV_LIST.map(({ path, icon }) => (
          <li>
            <Link href={path}>{icon}</Link>
          </li>
        ))}
      </ul>
    </nav>
  )
}

const NAV_LIST = [
  {
    label: 'Home',
    path: '/',
    icon: <AiFillHome />,
  },
  {
    label: 'Classes',
    path: 'classes',
    icon: <FaTicketAlt />,
  },
  {
    label: 'Home',
    path: 'community',
    icon: <HiChatBubbleLeftRight />,
  },
  {
    label: 'Home',
    path: 'setting',
    icon: <AiFillSetting />,
  },
]
