import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css';
import { AuthProvider } from './auth';
import LoginForm from './Login';
import { token, useToken } from "./auth.js";
// import { useEffect, useState } from "react";

function GetToken() {
    // Get token from JWT cookie (if already logged in)
    useToken();
    return null
}


function App() {
  // const[token] = useToken()

  return (
 <AuthProvider>

  <BrowserRouter>
    <GetToken />
    <Routes>
      <Route path="/" element={<LoginForm />}></Route>
    </Routes>
  </BrowserRouter>
  </AuthProvider>
  );
}

export default App;
