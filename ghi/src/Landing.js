import "./index.css";
import { useState } from "react";
import SideBar from "./SidebarNav";
import SearchComponent from "./SearchComponent";
import ConcertList from "./ConcertList";
// import SearchComponent from "./SearchComponent";
export default function Landing() {
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
			<SideBar />
			{/* background */}
			<div className="bg-indigo-700 h-screen">
				{/* header and h2 */}
				<div className="mx-auto max-w-2xl py-16 px-4 text-center sm:py-20 sm:px-6 lg:px-8">
					<h1 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
						<span className="block">Concerto</span>
					</h1>
					<h2 className="mt-4 text-lg  text-indigo-200">
						A place for music lovers.
					</h2>
				</div>
				{/* search box */}
				<div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 bg-white opacity-70 sm:rounded-lg p-8 overflow-x-scroll">
					<div className="text-center">
						<h3 className="text-base text-center tracking-tight text-black sm:text-4xl">
							Search concerts here:
						</h3>
					</div>
					<SearchComponent
						getConcerts={getConcerts}
						setConcerts={setConcerts}
					/>
					<div>
						{concerts.length > 0 && <ConcertList concerts={concerts} />}
					</div>

					{/*  */}
				</div>
			</div>
		</>
	);
}
