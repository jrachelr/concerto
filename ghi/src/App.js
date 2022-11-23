import { useEffect, useState } from "react";
import SearchComponent from "./SearchComponent";
import "./App.css";
import { useToken } from "./auth.js";

function GetToken() {
	// Get token from JWT cookie (if already logged in)
	useToken();
	return null;
}

function App() {
	return (
		<>
			<h1>Concerto</h1>
			<SearchComponent />
		</>
	);
}

export default App;
