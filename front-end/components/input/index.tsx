'use client'

import { useRef, useState } from 'react'

import styles from './input.module.scss'

export interface inputData {
  id: string
  title: string
  type: string
  label: string,
  regEx: RegExp,
  check: inputCheck[]
}

export interface inputCheck {
  name: string
  regex: RegExp
}

export default function Input(props: { data: inputData; event: Function }) {
  const checkInput = useRef(null);
  const [text, setText] = useState<string>('')
  const [data, setData] = useState({ ...props.data })

  const handleInput = (e: { target: { value: string } }) => {
    setText(e.target.value);
    props.event(e)
  }

  return (
    <div className={styles.inputArea}>
      <input
        type="text"
        id={data.id}
        onChange={handleInput}
        autoComplete="off"
        autoFocus
      />

      <label
        className={`${text !== '' ? styles.active : ''}`}
        htmlFor={data.label}
      >
        {data.label}
      </label>

      <div ref={checkInput} className={styles.checkInput}>
        {data.check.map((item: inputCheck, index) => {
          return (
            <small
              key={index}
              className={item.regex.test(text) ? `${styles.active}` : ''}
            >
            {item.name}
            </small>
          )
        })}
      </div>
    </div>
  )
}