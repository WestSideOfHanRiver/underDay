import { timeReplacer } from '@utils/formatter'
import axios from 'axios'
import { Moment } from 'moment'
import { LessonResponse } from 'types/lesson'

export const fetchLessons = async (selectedDate: string) => {
  const url = `https://port-0-underdaybackend-iciy2almouoe34.sel5.cloudtype.app/classlist?user_numb=00000000&date=${selectedDate}&user_abcd=A`

  try {
    const response = await axios.get(url)

    if (response.status !== 200) {
      throw new Error(response.data.message)
    }

    const result = response.data.map((el: LessonResponse) => ({
      classId: el.clas_numb,
      lessonName: el.clas_name,
      lessonDate: el.clas_date,
      startTime: timeReplacer(el.clas_time),
      endTime: timeReplacer(el.clas_clos),
      ticketId: el.tmem_numb,
      teacherName: el.tech_name,
      maxOccupancy: el.clas_nmax,
      enrollment: el.clas_cmax,
      waitingNumber: el.clas_wait,
      startBookingTime: el.resv_stat,
      endBookingTime: el.resv_last,
      bookingCheckTime: el.resv_alr1,
      availableBooking: el.clas_ysno,
      createdAt: el.clas_inst,
      updatedAt: el.clas_updt,
      reservationState: '예약가능',
      category: el.tmem_cate,
    }))

    return result
  } catch (error) {
    return []
  }
}
