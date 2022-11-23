import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./index.css";
import { AuthProvider } from "./auth";
import LoginForm from "./Login";
import Landing from "./Landing";
import { token, useToken } from "./auth.js";
// import { useEffect, useState } from "react";

function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null;
}

function App() {
  // const[token] = useToken()

  return (
    <AuthProvider>
      <BrowserRouter>
        <GetToken />
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="login/" element={<LoginForm />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
