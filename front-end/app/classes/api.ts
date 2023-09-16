export const fetchData = async () => {
  const url = `http://localhost:3000/~`

  try {
    const res = await fetch(url)

    if (!res.ok) {
      throw new Error('Failed to fetch data from server')
    }

    return res.json()
  } catch (error) {
    return []
  }
}
