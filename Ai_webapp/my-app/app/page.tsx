"use client";

import { HeroHighlight, Highlight } from "@/components/ui/hero-highlight";
import { motion ,AnimatePresence} from "framer-motion";
import { useEffect, useState } from "react";
import {Video,Brain,MessageSquare} from "lucide-react";
import {features} from '@/app/utils'
import Image from "next/image";
import YoutubeVideoForm from "@/components/ui/YoutubeVideoForm";

const steps = [
  {
    title: "1. Connect Your Content",
    description: "Share your YouTube video URL and let your agent get to work",
    icon: Video,
  },
  {
    title: "2. AI Agent Analysis",
    description: "Your personal agent analyzes every aspect of your content",
    icon: Brain,
  },
  {
    title: "3. Receive Intelligence",
    description: "Get actionable insights and strategic recommendations",
    icon: MessageSquare,
  },
];

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
      <div className="text-center max-w-4xl mt-12 pt-12">
      <AnimatePresence>
        <motion.h1 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ type: "spring",duration: 0.8 }}
          exit={{ opacity: 0 }}
          className="text-4xl font-bold text-gradient sm:text-7xl"
        >
          Automate Your YouTube Success
        </motion.h1>
      </AnimatePresence>
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
        transition={{ duration: 0.8, delay: 0.2 }}
        className="mt-6 text-xl text-gray-600 dark:text-gray-300 sm:text-2xl">
        <YoutubeVideoForm />
        </motion.div>
        
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
                <div
                  key={index}
                  className="p-6 rounded-xl border border-red-500 hover:border-red-500 transition-all duration-300"
                >
                  <div
                    className={`w-12 h-12 rounded-lg flex items-center justify-center mb-4 ${feature.iconBg}`}
                  >
                    <Icon className={`w-6 h-6 ${feature.iconColor} md:item-center`} />
                    </div> 

                  <h3 className="text-xl font-semibold mb-2">
                    {feature.title}
                  </h3>
                  <p className="text-white">{feature.description}</p>
                </div>
              );
            })}
            </div>
          </div>
        </motion.div>

      {/* How it works sections */}
      <section className="py-20 bg-black">
        <div className="container mx-auto px-4 max-w-6xl">
          <h2 className="text-3xl font-bold text-center mb-12">
            Meet Your AI Agent in 3 Simple Steps
          </h2>

          <div className="grid md:grid-cols-3 gap-8">
            {steps.map((step, index) => {
              const Icon = step.icon;
              return (
                <div
                  key={index}
                  className="text-center p-6 rounded-xl bg-black text-white shadow-md hover:shadow-lg transition-all"
                >
                  <div className="w-18 h-16 bg-gradient-to-r from-red-600 to-red-400 rounded-full flex items-center justify-center mx-auto mb-4">
                    <Icon className="w-8 h-8 text-white" />
                  </div>
                  <h3 className="text-xl font-semibold mb-2">{step.title}</h3>
                  <p className="text-gray-600">{step.description}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>
      {/* Footer section */}
      <section className="w-full overfow-hidden py-20 px-4 md:px-0 bg-gradient-to-r from-red-600 to-red-400 rounded-3xl">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-white mb-6">
            Ready to Meet Your AI Content Agent?
          </h2>
          <p className="text-xl text-red-50">
            Join creators leveraging AI to unlock content insights
          </p>
        </div>
      </section>
    </div>
    </div>
  );
}
