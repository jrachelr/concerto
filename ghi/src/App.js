import { Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import LoginForm from "./Users/Login";
import Landing from "./Landing";
import Logout from "./Users/Logout";
import SignupForm from "./Users/Signup";
import { useToken, AuthProvider } from "./auth.js";
import SearchComponent from "./SearchComponent";
import ConcertList from "./ConcertList";
import { useState } from "react";
import Header from "./Layout/Header";
import SideBar from "./Layout/SidebarNav";
import Favorites from "./ConcertFavorites";

function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null;
}

function App() {
  const [token, login, logout, signup] = useToken();
  const [concerts, setConcerts] = useState([]);

  async function getConcerts(lat, long) {
    const concertsUrl = `http://localhost:8000/concerts/${lat},${long}`;
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
      console.log(concerts);
    } else {
      console.log("ERROR");

      // const setLocation = (data) => {
      // 	setConcerts(data);
      // };
    }
  }

  return (
    <>
      <AuthProvider>
        <GetToken />
        <Routes>
          <Route path="/" element={<Landing />} token={token} />
          <Route path="header/" element={<Header />} token={token} />
          <Route path="sidebar/" element={<SideBar />} token={token} />
          <Route path="myconcerts/" element={<Favorites />} token={token} />
          <Route
            path="login/"
            element={<LoginForm token={token} login={login} />}
          />
          <Route
            path="signup/"
            element={<SignupForm token={token} signup={signup} />}
          />
          <Route path="logout/" element={<Logout />} logout={logout} />
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
