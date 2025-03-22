"use client";

import { useFormStatus } from "react-dom";

function AnalyseButton() {
  const { pending } = useFormStatus();

  return (
    <button
      type="submit"
      disabled={pending}
      className="px-6 py-2 text-white bg-red-600 rounded-lg hover:bg-red-900 focus:outline-none focus:ring-2 focus:ring-red-700 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 font-medium z-100"
    >
      {pending ? "Analyzing..." : "Analyze"}
    </button>
  );
}

export default AnalyseButton;