import Image from 'next/image';
import { Inter } from 'next/font/google';
import styles from './page.module.css';

const inter = Inter({ subsets: ['latin'] });

export default function Home() {
  return (
    <main className={styles.main}>
      <h1>여기는 메인 ~</h1>
    </main>
  );
}
