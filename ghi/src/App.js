import { Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import LoginForm from "./Users/Login";
import Landing from "./Landing";
import Logout from "./Users/Logout";
import SignupForm from "./Users/Signup";
import { useToken, AuthProvider } from "./auth.js";
import Header from "./Layout/Header";
import SideBar from "./Layout/SidebarNav";
import Favorites from "./Users/ConcertFavorites";
import { useAuthContext } from "./auth.js";
function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null;
}

function App() {
  const { token } = useAuthContext();

  return (
    <>
      <AuthProvider>
        <GetToken />
        <Routes basename="/concerto">
          <Route path="/" element={<Landing />} />
          <Route path="header/" element={<Header />} />
          <Route path="sidebar/" element={<SideBar />} />
          <Route path="myconcerts/" element={<Favorites />} />
          <Route path="login/" element={<LoginForm />} />
          <Route path="signup/" element={<SignupForm />} />
          <Route path="logout/" element={<Logout />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </AuthProvider>
    </>
  );
}

export default App;
