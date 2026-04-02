import React, { useEffect, useState } from "react";

export default function App() {
  const [assets, setAssets] = useState([]);
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/assets").then(r => r.json()).then(setAssets);
    fetch("http://localhost:8000/alerts").then(r => r.json()).then(setAlerts);
  }, []);

  return (
    <div style={{fontFamily: "Arial", padding: 24, maxWidth: 1000, margin: "0 auto"}}>
      <h1>OpenDigital Twin Builder</h1>
      <p>Master bundle demo dashboard</p>
      <h2>Assets</h2>
      {assets.map((a) => (
        <div key={a.asset_uid} style={{border: "1px solid #ddd", padding: 12, borderRadius: 10, marginBottom: 8}}>
          <strong>{a.name}</strong><br />
          {a.asset_type} — {a.asset_uid}
        </div>
      ))}
      <h2>Alerts</h2>
      {alerts.map((a, i) => (
        <div key={i} style={{border: "1px solid #ddd", padding: 12, borderRadius: 10, marginBottom: 8}}>
          <strong>{a.severity}</strong> — {a.message}
        </div>
      ))}
    </div>
  );
}
