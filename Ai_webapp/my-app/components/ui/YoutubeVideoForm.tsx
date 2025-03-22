import Form from "next/form";
import AnalyseButton from "./AnalyseButton";
import { analyseYoutubeVideo } from "@/action/analyseYoutubeVideo";
import _ from "lodash";


function YoutubeVideoForm() {
  return (
    <div className="w-full max-w-2xl mx-auto">
      <Form
        action={_.throttle(analyseYoutubeVideo,500)}
        className="flex flex-col sm:flex-row gap-2 items-center z-100"
        
      >
        <input
          required
          name="url"
          type="text"
          placeholder="Enter YouTube URL"
          // onInvalid={(e) => (e.target as HTMLInputElement).setCustomValidity("Please enter a valid YouTube URL")}
          className="flex-1 w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg focus:outline-none focus:ring-4 focus:ring-red-500 focus:border-transparent transition-all duration-200 z-100"
        />
        <AnalyseButton />
      </Form>
    </div>
  );
}

export default YoutubeVideoForm;