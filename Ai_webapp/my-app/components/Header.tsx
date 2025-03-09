"use client";
import React from 'react'
import Link from 'next/link'
const Header = () => {
  return (
    <header className='sticky top-0 z-50 left-0 right-0 border-b backdrop-blur-sm'>
        <div>
            <Link href="/">
            <div className='text-xl font-semibold bg-linear-to-tl from-blue-500 from-10% to-blue-200 to-90% text-transparent bg-clip-text opacity-80 m-2'>Z3Tube.Ai</div>                
            </Link>
        </div>
    </header>
  )
}

export default Header