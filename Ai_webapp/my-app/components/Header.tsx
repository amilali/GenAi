/* eslint-disable */
"use client";
import React from "react";
import Link from "next/link";
import { SignedOut, SignedIn, UserButton, SignInButton } from "@clerk/nextjs";
import { motion } from "framer-motion";

const Header = () => {
  return (
    <header className="sticky top-0 z-50 left-0 right-0 backdrop-blur-sm flex justify-between items-center overflow-x-clip p-4">
      <div>
        <Link href="/">
          <div className="text-xl font-bold bg-gradient-to-r from-red-500 to-white text-transparent bg-clip-text bg-[length:200%_auto] animate-[shine_2s_linear_infinite]">
            YTOptimizer.ai
          </div>
        </Link>
      </div>
      <div>
        <motion.div
          initial={{ opacity: 0}}
          animate={{ opacity: 1}}
          transition={{ type: "tween", duration: 0.8 }}
          exit={{ opacity: 0 }}
          className="m-2 h-10"
        >
          <SignedIn>
            <div>
              <UserButton />
            </div>
          </SignedIn>
          <SignedOut>
            <SignInButton mode="modal">
              <button className="inline-flex text-white items-center justify-center rounded-md border border-red-500 bg-[linear-gradient(110deg,#000103,45%,#1e2631,55%,#000103)] bg-[length:200%_100%] px-5 font-medium text-slate-400 transition-colors focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 m-2 text-md p-2 hover:ring-1 hover:ring-red-500">
                Sign In
              </button>
            </SignInButton>
          </SignedOut>
        </motion.div>
      </div>
    </header>
  );
};

export default Header;
