"use client";
import React from 'react'
import Link from 'next/link'
import { SignedOut, UserButton } from '@clerk/nextjs';
import { SignInButton } from '@clerk/nextjs';
import { SignedIn } from '@clerk/nextjs';

const Header = () => {
  return (
    <header className='sticky top-0 z-50 left-0 right-0 backdrop-blur-sm flex justify-between items-center overflow-x-clip'>
        <div>
            <Link href="/">
                <div className='text-xl font-bold bg-gradient-to-r from-blue-500 to-sky-500 text-transparent bg-clip-text bg-[length:200%_auto] animate-[shine_2s_linear_infinite]'>
                    Z3Tube.Ai
                </div>
            </Link>
        </div>
        <div>
          <SignedIn>
            <div className='m-2'>
              <UserButton />
            </div>
          </SignedIn>
          <SignedOut>
            <SignInButton mode="modal">
              <button className="inline-flex h-6 animate-shimmer items-center justify-center rounded-md border border-slate-800 bg-[linear-gradient(110deg,#000103,45%,#1e2631,55%,#000103)] bg-[length:200%_100%] px-6 font-medium text-slate-400 transition-colors focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2 focus:ring-offset-slate-50 m-2 text-md p-2">
                Sign In
              </button>
            </SignInButton>
          </SignedOut>
        </div>
    </header>
  )
}

export default Header