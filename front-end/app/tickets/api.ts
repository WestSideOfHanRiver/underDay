export const fetchData = async (url: string, data?: object) => {
  if (url != '') {
    try {
      const res = await fetch(
        url,
        data && {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data),
        },
      )

      if (!res.ok) {
        throw new Error('서버에서 데이터를 가져오지 못했습니다:(')
      }

      return res.json()
    } catch (err) {
      return []
    }
  }
}
