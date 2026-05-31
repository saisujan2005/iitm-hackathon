"use client";

import { useEffect, useState } from "react";
import {
  MapPin,
  Send,
  Wifi,
  WifiOff,
  ShieldAlert,
} from "lucide-react";



export default function Home() {
  const [query, setQuery] = useState("");

  const [state, setState] = useState("Karnataka");

  const [violation, setViolation] = useState("");

  const [violations, setViolations] = useState<any[]>([]);

  const [fine, setFine] = useState<any>(null);

  const [ocrFile, setOcrFile] = useState<File | null>(null);

  const [ocrResult, setOcrResult] = useState<any>(null);

  const [ocrLoading, setOcrLoading] = useState(false);

  const [loading, setLoading] = useState(false);

  const [online, setOnline] = useState(true);

  const [locationName, setLocationName] = useState("Detecting...");

  const [city, setCity] = useState("");
  
  const [detectedState, setDetectedState] = useState("");

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello 👋 Ask me anything about traffic laws or challans.",
    },
  ]);
  useEffect(() => {

    if (!navigator.geolocation) {
      setLocationName("Location not supported");
      return;
    }

    navigator.geolocation.getCurrentPosition(
      async (position) => {

        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        try {

          const res = await fetch(
            `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`
          );

          const data = await res.json();

          console.log("Location:", data);

          const detectedState =
            data.address.state || "";

          const city =
            data.address.city ||
            data.address.town ||
            data.address.village ||
            "";

          setLocationName(
            `${city}, ${detectedState}`
          );

          if (
            detectedState
              .toLowerCase()
              .includes("karnataka")
          ) {
            setState("Karnataka");
          }

          if (
            detectedState
              .toLowerCase()
              .includes("delhi")
          ) {
            setState("Delhi");
          }

        } catch (err) {
          console.error(
            "Reverse geocoding failed:",
            err
          );

          setLocationName(
            "Location unavailable"
          );
        }
      },

      (err) => {
        console.error(
          "Geolocation error:",
          err
        );

        setLocationName(
          "Location unavailable"
        );
      }
    );

  }, []);

  useEffect(() => {
    const updateStatus = () => {
      setOnline(navigator.onLine);
    };

    window.addEventListener("online", updateStatus);
    window.addEventListener("offline", updateStatus);

    return () => {
      window.removeEventListener("online", updateStatus);
      window.removeEventListener("offline", updateStatus);
    };
  }, []);

  useEffect(() => {
  const fetchViolations = async () => {
    try {
      const res = await fetch(
        `http://127.0.0.1:8000/violations/${state}`
      );

      const data = await res.json();

      console.log("Violations:", data);

      setViolations(data);

      if (data.length > 0) {
        setViolation(data[0].violation);
      }

    } catch (err) {
      console.error(err);
    }
  };

     fetchViolations();
},     [state]);
  useEffect(() => {

    navigator.geolocation.getCurrentPosition(
      async (position) => {

        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        try {

          const res = await fetch(
            `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`
          );

          const data = await res.json();

          const detectedState =
            data.address.state || "";

          const city =
            data.address.city ||
            data.address.town ||
            data.address.village ||
            "";

          setLocationName(
            `${city}, ${detectedState}`
          );

          if (
            detectedState
              .toLowerCase()
              .includes("karnataka")
          ) {
            setState("Karnataka");
          }

          if (
            detectedState
              .toLowerCase()
              .includes("delhi")
          ) {
            setState("Delhi");
          }

        } catch (err) {
          console.error(err);
        }
      },
      (err) => {
        console.error(err);
      }
    );

  }, []);

const handleSend = async () => {
  if (!query.trim()) return;

  const userMessage = {
    role: "user",
    content: query,
  };

  setMessages((prev) => [...prev, userMessage]);

  const currentQuery = query;
  setQuery("");

  try {
    const res = await fetch("http://127.0.0.1:8000/chat/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question: currentQuery,
      }),
    });

    const data = await res.json();

    const aiMessage = {
      role: "assistant",
      content: data.answer,
    };

    setMessages((prev) => [...prev, aiMessage]);
  } catch (err) {
    console.error(err);

    setMessages((prev) => [
      ...prev,
      {
        role: "assistant",
        content: "Backend connection failed.",
      },
    ]);
  }
};

const detectLocation = () => {

  if (!navigator.geolocation) return;

  navigator.geolocation.getCurrentPosition(
    async (position) => {

      const lat = position.coords.latitude;
      const lon = position.coords.longitude;

      try {

        const res = await fetch(
          `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`
        );

        const data = await res.json();

        setCity(
             data.address.county || ""
        );

        setDetectedState(
            data.address.state || ""
      );

        const detectedState =
          data.address.state;

        console.log(
          "Detected State:",
           detectedState
);  

        if (
          detectedState?.includes(
            "Karnataka"
          )
        ) {
          setState("Karnataka");
        }

        else if (
          detectedState?.includes(
            "Delhi"
          )
        ) {
          setState("Delhi");
        }

        else if (
          detectedState?.includes(
            "Maharashtra"
          )
        ) {
          setState("Maharashtra");
        }

        else if (
          detectedState?.includes(
             "Tamil Nadu"
       )
     ) {
          setState(
           "Tamil Nadu"
     );
  }

      } catch (err) {

        console.error(err);

      }

    }
  );
};useEffect(() => {

  detectLocation();

}, []);



const calculateFine = async () => {
  try {
    setLoading(true);

    console.log("Sending Request:", {
      state,
      violation,
      vehicle_type: "bike",
      repeat_offense: false,
    });

    const res = await fetch(
      "http://127.0.0.1:8000/calculate",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          state,
          violation,
          vehicle_type: "bike",
          repeat_offense: false,
        }),
      }
    );

    const data = await res.json();

    console.log("Backend Response:", data);

    setFine(data);
  } catch (err) {
    console.error("Calculate Fine Error:", err);
  } finally {
    setLoading(false);
  }
};

const uploadChallan = async () => {

  if (!ocrFile) return;

  try {

    setOcrLoading(true);

    const formData = new FormData();

    formData.append(
      "file",
      ocrFile
    );

    const res = await fetch(
      "http://127.0.0.1:8000/ocr/upload",
      {
        method: "POST",
        body: formData,
      }
    );

    const data = await res.json();

    setOcrResult(data);

  } catch (err) {

    console.error(err);

  } finally {

    setOcrLoading(false);

  }
};

  return (
    <main className="min-h-screen bg-zinc-950 text-white p-6">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-3xl font-bold">🚦 DriveLegal</h1>
          <p className="text-zinc-400 text-sm">
            AI Powered Traffic Law Assistant
          </p>
        </div>

        <div
          className={`flex items-center gap-2 px-3 py-2 rounded-xl text-sm ${
            online
              ? "bg-green-500/20 text-green-400"
              : "bg-red-500/20 text-red-400"
          }`}
        >
          {online ? <Wifi size={18} /> : <WifiOff size={18} />}
          {online ? "Online" : "Offline"}
        </div>
      </div>

      {/* Location */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 flex items-center gap-3 mb-6">
        <MapPin className="text-blue-400" />
        <div>
          <p className="font-medium">Location Detected</p>
          <p className="text-sm text-zinc-400">
            {locationName}
          </p>
        </div>
      </div>

      {/* Chat Section */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-4 h-[400px] overflow-y-auto mb-6">
        <div className="space-y-4">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`max-w-[80%] p-4 rounded-2xl ${
                msg.role === "user"
                  ? "ml-auto bg-blue-600"
                  : "bg-zinc-800"
              }`}
            >
              <p>{msg.content}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Input */}
      <div className="flex gap-3 mb-8">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask about traffic laws..."
          className="flex-1 bg-zinc-900 border border-zinc-700 rounded-2xl px-4 py-3 outline-none"
        />

        <button
          onClick={handleSend}
          className="bg-blue-600 hover:bg-blue-700 transition px-5 rounded-2xl flex items-center justify-center"
        >
          <Send size={18} />
        </button>
      </div>

      {/* Challan Calculator */}
      <div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6">
        <div className="flex items-center gap-2 mb-5">
          <ShieldAlert className="text-yellow-400" />
          <h2 className="text-xl font-semibold">
            Challan Calculator
          </h2>
        </div>

        <div className="mb-4">
  <button
    onClick={detectLocation}
    className="bg-blue-600 hover:bg-blue-700 px-5 py-3 rounded-xl"
  >
    📍 Detect My Location
  </button>
</div>

<div className="grid md:grid-cols-3 gap-4 mb-5">

  <select
    value={state}
    onChange={(e) => setState(e.target.value)}
    className="bg-zinc-800 border border-zinc-700 rounded-xl px-4 py-3"
  >
    <option>Karnataka</option>
    <option>Delhi</option>
    <option>Maharashtra</option>
    <option>Tamil Nadu</option>
  </select>

  <select
    value={violation}
    onChange={(e) => setViolation(e.target.value)}
    className="bg-zinc-800 border border-zinc-700 rounded-xl px-4 py-3"
  >
    {violations.map((item) => (
      <option
        key={item.id}
        value={item.violation}
      >
        {item.violation}
      </option>
    ))}
  </select>

  <select className="bg-zinc-800 border border-zinc-700 rounded-xl px-4 py-3">
    <option>Bike</option>
    <option>Car</option>
  </select>

</div>

        <button
        onClick={calculateFine}
        className="bg-yellow-500 hover:bg-yellow-600 text-black font-semibold px-6 py-3 rounded-2xl">
          Calculate Fine
        </button>

        <div className="mt-6 bg-zinc-800 rounded-2xl p-4">
          <p className="text-zinc-400 text-sm mb-1">
            Estimated Fine
          </p>
          {fine && (
  <div className="mt-6 bg-zinc-800 rounded-2xl p-4">
    <p className="text-zinc-400 text-sm mb-1">
      Estimated Fine
    </p>

    {fine.error ? (
      <p className="text-red-400">
        {fine.error}
      </p>
    ) : (
      <>
        <h3 className="text-3xl font-bold text-yellow-400">
          {fine.fine_amount}
        </h3>

        <p className="text-sm text-zinc-400 mt-3">
          <strong>Violation:</strong>{" "}
          {fine.violation}
        </p>

        <p className="text-sm text-zinc-400 mt-2">
          <strong>Section:</strong>{" "}
          {fine.section}
        </p>

        <p className="text-sm text-zinc-400 mt-2">
          <strong>State:</strong>{" "}
          {fine.state}
        </p>

        {fine.source_url && (
          <p className="text-xs text-zinc-500 mt-3 break-all">
            Source: {fine.source_url}
          </p>
        )}
      </>
    )}
  </div>
)}
          
       </div>
      </div>
      {/* OCR Upload */}

<div className="bg-zinc-900 border border-zinc-800 rounded-2xl p-6 mt-6">

  <h2 className="text-xl font-semibold mb-4">
    📸 Challan OCR
  </h2>

  <div className="flex items-center gap-4">

  <label
    className="
      cursor-pointer
      bg-zinc-800
      hover:bg-zinc-700
      px-5
      py-3
      rounded-xl
      border
      border-zinc-700
    "
  >
    📄 Upload Challan

    <input
      type="file"
      accept="image/*"
      className="hidden"
      onChange={(e) => {

        if (e.target.files?.[0]) {

          setOcrFile(
            e.target.files[0]
          );

        }

      }}
    />
  </label>

  <button
    onClick={uploadChallan}
    className="bg-green-600 hover:bg-green-700 px-5 py-3 rounded-xl"
  >
    Analyze Challan
  </button>



</div>

{ocrFile && (

  <p className="text-sm text-zinc-400 mt-3">

    Selected File:
    {" "}
    {ocrFile.name}

  </p>

)}

 

  {ocrLoading && (

    <p className="mt-4 text-zinc-400">
      Analyzing image...
    </p>

  )}

  {ocrResult && (

  <div className="mt-6 bg-zinc-800 rounded-xl p-5 border border-zinc-700">

    <h3 className="font-semibold text-lg mb-4">
      📸 Challan Analysis
    </h3>

    <div className="space-y-3">

      <div>
        <p className="text-zinc-400 text-sm">
          Vehicle Number
        </p>

        <p>
          {ocrResult.ocr?.vehicle_number ||
            "N/A"}
        </p>
      </div>

      <div>
        <p className="text-zinc-400 text-sm">
          Section
        </p>

        <p>
          {ocrResult.ocr?.section ||
            "Not Available"}
        </p>
      </div>

      <div>
        <p className="text-zinc-400 text-sm">
          Fine Amount
        </p>

        <p>
          ₹{
            ocrResult.ocr?.fine_amount ||
            "Not Available"
          }
        </p>
      </div>

      {ocrResult.official_record && (

        <>
          <div>
            <p className="text-zinc-400 text-sm">
              Violation
            </p>

            <p>
              {
                ocrResult.official_record
                  .violation
              }
            </p>
          </div>

          <div>
            <p className="text-zinc-400 text-sm">
              Legal Explanation
            </p>

            <p className="text-sm">
              {
                ocrResult.official_record
                  .explanation
              }
            </p>
          </div>

          <div>
            <p className="text-green-400 font-medium">
              ✅ Verified against database
            </p>
          </div>
        </>

      )}

      {ocrResult.message && (

        <div>
          <p className="text-yellow-400">
            ⚠ {ocrResult.message}
          </p>
        </div>

      )}

    </div>

  </div>

)}

</div>
    </main>
  );
}