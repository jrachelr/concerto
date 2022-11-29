import { Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import LoginForm from "./Users/Login";
import Landing from "./Landing";
import SideBar from "./SidebarNav";
import { useToken } from "./auth.js";

// function GetToken() {
// 	// Get token from JWT cookie (if already logged in)
// 	useToken();
// 	return null;
// }

function App() {
	// const[token] = useToken()
	const [token, login] = useToken();

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
