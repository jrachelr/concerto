import React from "react";
import { useNavigate } from "react-router-dom";
import { useToken } from "../auth.js";

export default function Logout() {
  const [, , logout] = useToken();
  const navigate = useNavigate();

  const signout = async (e) => {
    e.preventDefault();
    logout();
    console.log("logged out");
    navigate("/");
  };

  return (
    <>
      <div>
        <h3>Are you sure you want to sign out?</h3>
        <button onClick={signout}>Sign out</button>
      </div>
    </>
  );
}
