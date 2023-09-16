import { configureStore } from '@reduxjs/toolkit'

import selectedDateReducer from '@components/calendar/selectedDateSlice'

export const store = configureStore({
  reducer: {
    selectedDate: selectedDateReducer,
  },
})

export type RootState = ReturnType<typeof store.getState>

export type AppDispatch = typeof store.dispatch
