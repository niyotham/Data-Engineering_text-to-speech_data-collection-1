import React from "react";
import { useState } from "react";
import { Recorder } from "react-voice-recorder";
import "react-voice-recorder/dist/index.css";

export default function App() {
  const [audioDetails, setAudioDetails] = useState({
    url: null,
    blob: null,
    chunks: null,
    duration: {
      h: 0,
      m: 0,
      s: 0
    }
  });

  const handleAudioStop = (data) => {
    console.log(data);
    setAudioDetails({ ...data });
  };

  const handleAudioUpload = (file) => {
    console.log(file);
  };

  const handleReset = () => {
    setAudioDetails({
      url: null,
      blob: null,
      chunks: null,
      duration: {
        h: 0,
        m: 0,
        s: 0
      }
    });
  };

  return (
    <div className="App">
      <Recorder
        record={true}
        title={"Text to Speech Recording"}
        audioURL={audioDetails.url}
        showUIAudio
        handleAudioStop={handleAudioStop}
        handleAudioUpload={handleAudioUpload}
        // handleCountDown={handleCountDown}
        handleReset={handleReset}
        // mimeTypeToUseWhenRecording={`audio/webm`}
      />
    </div>
  );
}
