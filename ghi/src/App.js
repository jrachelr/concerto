import { Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import LoginForm from "./Users/Login";
import Landing from "./Landing";
import Homepage from "./Homepage";
import Logout from "./Users/Logout";
import SignupForm from "./Users/Signup";
import { useToken } from "./auth.js";

function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null;
}

function App() {
  const [token, login, signup] = useToken();

  return (
    <>
      <GetToken />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="home/" element={<Homepage />} />
        <Route
          path="signup/"
          element={<SignupForm token={token} signup={signup} />}
        />

        <Route
          path="login/"
          element={<LoginForm token={token} login={login} />}
        />
        <Route path="logout/" element={<Logout />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </>
  );
}

export default App;
