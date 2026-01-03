import React from 'react';
import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // Import the Register component

function App() {
  return (
    <Routes>
      {/* Route for Login */}
      <Route path="/login" element={<LoginPanel />} />
      
      {/* Route for Registration */}
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;