import "./index.css";
import { useState } from "react";
import SideBar from "./Layout/SidebarNav";
import SearchComponent from "./SearchComponent";
import ConcertList from "./ConcertComponents/ConcertList";
import Header from "./Layout/Header";
import { useAuthContext } from "./auth";
// import SearchComponent from "./SearchComponent";

export default function Landing() {
	const { token } = useAuthContext();
	const [concerts, setConcerts] = useState([]);
	async function getConcerts(city, state) {
		const concertsUrl = `http://localhost:8000/concerts/${city},${state}`;
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
		}
	}

	return (
		<>
			<div className="bg-scroll bg-hero bg-cover bg-blend-overlay from-indigo-500">
				{token ? <SideBar /> : <Header />}
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
					<div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 bg-white opacity-70 sm:rounded-lg p-8">
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
							{concerts.length > 0 && (
								<ConcertList concerts={concerts} setConcerts={setConcerts} />
							)}
						</div>
					</div>

					{/*  */}
				</div>
			</div>
		</>
	);
}
