// ChatWidget.jsx
import React, { useState } from "react";

export default function ChatWidget() {
  const [messages, setMessages] = useState([]);
  const [msg, setMsg] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage() {
    if (!msg || loading) return;

    setLoading(true);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: msg })
      });

      const data = await res.json();

      setMessages(prev => [
        ...prev,
        { q: msg, a: data.answer || "No response" }
      ]);

      setMsg("");
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { q: msg, a: "⚠️ Error connecting to server" }
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      style={{
        position: "fixed",
        bottom: 20,
        right: 20,
        background: "white",
        padding: 20,
        width: 320,
        borderRadius: 10,
        zIndex: 1000,
        boxShadow: "0 10px 30px rgba(0,0,0,0.2)"
      }}
    >
      <h4>📘 Book Assistant</h4>

      <div style={{ maxHeight: 220, overflowY: "auto", marginBottom: 10 }}>
        {messages.map((m, i) => (
          <div key={i}>
            <b>You:</b> {m.q}<br />
            <b>Bot:</b> {m.a}
            <hr />
          </div>
        ))}
      </div>

      <input
        value={msg}
        onChange={e => setMsg(e.target.value)}
        style={{ width: "100%" }}
        placeholder="Ask a question..."
        onKeyDown={e => e.key === "Enter" && sendMessage()}
      />

      <button
        onClick={sendMessage}
        disabled={loading}
        style={{ marginTop: 10, width: "100%" }}
      >
        {loading ? "Thinking..." : "Ask"}
      </button>
    </div>
  );
}
