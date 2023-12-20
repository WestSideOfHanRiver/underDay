export const timeReplacer = (time: string): string => {
  const regex = /^(\d{2})(\d{2})$/
  const match = time.match(regex)

  if (!match) {
    return '잘못된 시간 형식'
  }

  return `${match[1]}:${match[2]}`
}
