import React from 'react'

type Props = {}

export default function analysisPage({}: Props) {
  return (
    <div className='xl:container mx-auto px-4 md:px-0'>
      <div className='grid grid-cols-1 lg:grid-cols-2 gap-4'>
          <div className='order-2 lg:order-1'>
            {/* left */}
            cool stuff
          </div>

          <div className='order-1 lg:order-2'>
            {/* Right */}
            chat
          </div>

      </div>
    </div>
  )
}