import { Dispatch, SetStateAction } from 'react'

interface Props {
  setToggleDetail: Dispatch<SetStateAction<boolean>>
}

export default function AddTicketButton({ setToggleDetail }: Props) {
  const buttonStyle = {
    borderRadius: '4px',
    boxShadow: '0 2px 4px 0 rgba(204, 204, 204, 0.2)',
    backgroundColor: '#ddd',
    fontWeight: '700',
    color: '#0f2552',
    outline: 'none',
    border: 'none',
    cursor: 'pointer',
    display: 'block',
    margin: '32px 0 20px',
    width: '100%',
    fontSize: '14px',
    height: '48px',
  };

  return (
    <>
      <button type="button" style={buttonStyle} onClick={() => setToggleDetail(true)}>회원권 생성하기</button>
    </>
  )
}
