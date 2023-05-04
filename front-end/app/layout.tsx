import './globals.css'

import Navigation from './navigation'

export const metadata = {
  title: 'Under Day',
  description: 'check your workout schedule and manage yours',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {children}
        <Navigation />
      </body>
    </html>
  )
}
