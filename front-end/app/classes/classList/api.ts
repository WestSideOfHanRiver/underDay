import { timeReplacer } from '@utils/formatter'
import axios from 'axios'
import { Lesson, LessonResponse } from 'types/lesson'

interface Props {
  userId: string
  selectedDate: string
  userType: string
}

export const fetchDailyLessons = async ({
  userId,
  selectedDate,
  userType,
}: Props): Promise<Lesson[]> => {
  const url = process.env.NEXT_PUBLIC_DAILY_CLASSES_URL

  try {
    const response = await axios.get(
      `${url}?user_numb=${userId}&date=${selectedDate}&user_abcd=${userType}`,
    )

    const result = response.data.map((el: LessonResponse) => ({
      classId: el.clas_numb,
      lessonName: el.clas_name,
      lessonDate: el.clas_date,
      startTime: timeReplacer(el.clas_time),
      endTime: timeReplacer(el.clas_clos),
      ticketId: el.tmem_numb,
      // teacherName: string
      maxOccupancy: el.clas_nmax,
      waitingNumber: el.clas_wait,
      startBookingTime: el.resv_stat,
      endBookingTime: el.resv_last,
      bookingCheckTime: el.resv_alr1,
      availableBooking: el.clas_ysno,
      createdAt: el.clas_inst,
      updatedAt: el.clas_updt,
    }))

    return result
  } catch (error) {
    return []
  }
}
