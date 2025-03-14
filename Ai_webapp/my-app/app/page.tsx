"use client";

import { HeroHighlight, Highlight } from "@/components/ui/hero-highlight";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";
// import { Moon, Sun } from "lucide-react";
import {ThreeDCardDemo} from "@/components/ui/ThreeDCardDemo";
import {features} from '@/app/utils'


export default function Home() {
  const [darkMode, setDarkMode] = useState(() => {
    return typeof window !== "undefined" && localStorage.getItem("theme") === "dark";
  });

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
      localStorage.setItem("theme", "dark");
    } else {
      document.documentElement.classList.remove("dark");
      localStorage.setItem("theme", "light");
    }
  }, [darkMode]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4 bg-gradient-to-br">
      {/* <button
        onClick={() => setDarkMode(!darkMode)}
        className="p-2 rounded-full bg-gray-200 dark:bg-gray-800 transition z-10"
      >
        {darkMode ? <Sun className="text-yellow-500" /> : <Moon className="text-gray-900" />}
      </button> */}

      <div className="text-center max-w-4xl mt-12 pt-12">
        <motion.h1 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-4xl font-bold text-gradient sm:text-7xl"
        >
          Automate Your YouTube Success
        </motion.h1>
        <motion.p 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="mt-6 text-xl text-gray-600 dark:text-gray-300 sm:text-2xl"
        >
          Transform your content creation workflow with AI-powered automation. Create, edit, and publish videos faster than ever.
        </motion.p>
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="mt-8 py-20 space-y-4 sm:space-y-0 sm:space-x-4 sm:flex sm:justify-center text-gradient"
        >
          <div className="container mx-auto">
            <h1 className="text-3xl font-bold mb-12">Powerful feature for content creator</h1>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 bg-black text-white">
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                // <ThreeDCardDemo key={index} iconBg={feature.iconBg} iconColor={feature.iconColor} title={feature.title} iconNAme={feature.icon} url={feature.url}/>
                <div
                  key={index}
                  className="p-6 rounded-xl border border-blue-500 hover:border-blue-500 transition-all duration-300"
                >
                  <div
                    className={`w-12 h-12 rounded-lg flex items-center justify-center mb-4 ${feature.iconBg}`}
                  >
                    <Icon className={`w-6 h-6 ${feature.iconColor} md:item-center`} />
                  </div>

                  <h3 className="text-xl font-semibold mb-2">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600">{feature.description}</p>
                </div>
              );
            })}
            </div>
          </div>
        </motion.div>
      {/* Footer section */}
      <section className="w-full overfow-hidden py-20 px-4 md:px-0 bg-gradient-to-r from-blue-600 to-blue-400 rounded-3xl">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-white mb-6">
            Ready to Meet Your AI Content Agent?
          </h2>
          <p className="text-xl text-blue-50">
            Join creators leveraging AI to unlock content insights
          </p>
        </div>
      </section>
    </div>
    </div>
  );
}
