import { createSlice } from '@reduxjs/toolkit'
import { PayloadAction } from '@reduxjs/toolkit'
import moment from 'moment'

export interface SelectedDateState {
  value: string
}

const initialState: SelectedDateState = {
  value: moment().format('YYMMDD'),
}

export const selectedDateSlice = createSlice({
  name: 'selectedDate',
  initialState,
  reducers: {
    init: (state) => {
      state.value = initialState.value
    },
    setSelectedDate: (state, action: PayloadAction<string>) => {
      state.value = action.payload
    },
  },
})

export const { init, setSelectedDate } = selectedDateSlice.actions

export default selectedDateSlice.reducer
