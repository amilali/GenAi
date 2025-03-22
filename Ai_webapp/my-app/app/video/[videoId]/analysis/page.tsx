'use client';
import YoutubeVideoDetails from '@/components/YoutubeVideoDetails'
import React from 'react'
import { useParams } from 'next/navigation'
type Props = {}

export default function analysisPage({}: Props) {
  const param = useParams<{videoId : string}>();
  const {videoId} = param;
  return (
    <div className='xl:container mx-auto px-4 md:px-0'>
      <div className='grid grid-cols-1 lg:grid-cols-2 gap-4'>
          <div className='order-2 lg:order-1 border border-gray-500 rounded-2xl'>
            {/* left */}
            <YoutubeVideoDetails videoId={videoId}/>
          </div>

          <div className='order-1 lg:order-2'>
            {/* Right */}
            chat
          </div>

      </div>
    </div>
  )
}