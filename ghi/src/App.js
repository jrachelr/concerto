import { Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import LoginForm from "./Users/Login";
import Landing from "./Landing";
import Logout from "./Users/Logout";
import SignupForm from "./Users/Signup";
import { useToken, AuthProvider } from "./auth.js";
import ConcertList from "./ConcertComponents/ConcertList";
import SearchComponent from "./SearchComponent";
import { useState } from "react";
import Header from "./Layout/Header";
import SideBar from "./Layout/SidebarNav";
import Favorites from "./Users/ConcertFavorites";

function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null;
}

function App() {
  const [concerts, setConcerts] = useState([]);

  async function getConcerts(city, state) {
    const concertsUrl = `http://localhost:8000/concerts/${city},${state}`;
    const fetchConfig = {
      method: "get",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(concertsUrl, fetchConfig);
    if (response.ok) {
      const data = await response.json();
      setConcerts(data.concerts);
    } else {
      console.log("SOS");
    }
  }

  return (
    <>
      <AuthProvider>
        <GetToken />
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="header/" element={<Header />} />
          <Route path="sidebar/" element={<SideBar />} />
          <Route path="myconcerts/" element={<Favorites />} />
          <Route path="login/" element={<LoginForm />} />
          <Route path="signup/" element={<SignupForm />} />
          <Route path="logout/" element={<Logout />} />
          <Route path="*" element={<Navigate to="/" />} />
          <Route
            path="search"
            element={<SearchComponent getConcerts={getConcerts} />}
          />
          <Route
            path="concerts"
            element={<ConcertList concerts={concerts} />}
          />
        </Routes>
      </AuthProvider>
    </>
  );
}

export default App;
