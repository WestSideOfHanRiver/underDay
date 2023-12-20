import axios from 'axios'

interface AppliedData {
  resv_numb: string
  user_numb: string
  clas_numb: string
  tmem_numb: string
  resv_stat: string
}

export const applyLesson = async (data: AppliedData) => {
  const url = `https://port-0-underdaybackend-iciy2almouoe34.sel5.cloudtype.app/classrequest/`

  try {
    const response = await axios.put(url, data)

    if (response.status === 200) {
      return
    }
  } catch (error) {
    return
  }
}
