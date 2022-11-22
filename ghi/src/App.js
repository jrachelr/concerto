import { useEffect, useState } from "react";
import Construct from "./Construct.js";
import ErrorNotification from "./ErrorNotification";
import "./App.css";
import { useToken } from "./auth.js";

function GetToken() {
    // Get token from JWT cookie (if already logged in)
    useToken();
    return null
}


function App() {
  const [launch_info, setLaunchInfo] = useState([]);
  const [error, setError] = useState(null);

  const[token] = useToken()

  return (
    <div>
      <ErrorNotification error={error} />
      <Construct info={launch_info} />
    </div>
  );
}

export default App;
