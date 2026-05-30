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

  const [loading, setLoading] = useState(false);

  const [online, setOnline] = useState(true);

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello 👋 Ask me anything about traffic laws or challans.",
    },
  ]);

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
    const res = await fetch("http://127.0.0.1:8000/chat", {
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
      content: data.response,
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
            Bangalore, Karnataka
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

        <div className="grid md:grid-cols-3 gap-4 mb-5">
          <select
          value={state}
          onChange={(e) => setState(e.target.value)}
          className="bg-zinc-800 border border-zinc-700 rounded-xl px-4 py-3">
            <option>Karnataka</option>
            <option>Delhi</option>
            <option>Maharashtra</option>
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
    </main>
  );
}