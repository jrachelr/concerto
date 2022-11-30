import { Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import LoginForm from "./Users/Login";
import Landing from "./Landing";
import Homepage from "./Homepage";
import Logout from "./Users/Logout";
import SignupForm from "./Users/Signup";
import { useToken } from "./auth.js";
import SearchComponent from "./SearchComponent";
import ConcertList from "./ConcertList";
import { useState } from "react";

function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null;
}

function App() {
  const [token, login] = useToken();
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
      <GetToken />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="sidebar/" element={<SideBar />} />
        <Route
          path="login/"
          element={<LoginForm token={token} login={login} />}
        />
        <Route path="*" element={<Navigate to="/" />} />
        <Route
          path="search"
          element={<SearchComponent getConcerts={getConcerts} />}
        />
        <Route path="concerts" element={<ConcertList concerts={concerts} />} />
      </Routes>
    </>
  );
}

export default App;
