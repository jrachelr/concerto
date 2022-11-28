import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import LoginForm from "./Users/Login";
import Landing from "./Landing";
import SideBar from "./SidebarNav";
import { useToken } from "./auth.js";

function GetToken() {
  // Get token from JWT cookie (if already logged in)
  useToken();
  return null;
}

function App() {
  const [token, login] = useToken();

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
      </Routes>
    </>
  );
}

export default App;
