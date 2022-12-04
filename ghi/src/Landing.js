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
	const [success, setSuccess] = useState(true);
	async function getConcerts(city, state) {
		const concertsUrl = `http://localhost:8000/concerts/${city},${state}`;
		const fetchConfig = {
			method: "get",
			headers: {
				"Content-Type": "application/json",
			},
		};
		fetch(concertsUrl, fetchConfig)
			.then((response) => {
				if (response.ok) {
					return response.json();
				}
				throw new Error("Something went wrong");
			})
			.then((responseJson) => {
				setConcerts(responseJson.concerts);
				setSuccess(true);
			})
			.catch((error) => {
				setSuccess(false);
			});

		// const response = await fetch(concertsUrl, fetchConfig);
		// if (response.ok) {
		// 	const data = await response.json();
		// 	setConcerts(data.concerts);
		// 	console.log(concerts);
		// } else {
		// 	console.log("ERROR");
		// }
	}

	return (
		<>
			<div className="overflow-y-scroll bg-hero bg-cover bg-blend-overlay from-indigo-500 h-screen">
				{token ? <SideBar /> : <Header />}
				{/* background */}
				<div>
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
					<div className="mx-auto max-w-3xl px-4 sm:px-6 lg:px-8 bg-white opacity-90 sm:rounded-lg p-8">
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
								<ConcertList
									concerts={concerts}
									setConcerts={setConcerts}
									success={success}
								/>
							)}
						</div>
						{!success && (
							<div
								className="mt-4 flex items-center bg-red-100 border border-red-400 text-red-700 text-sm font-bold px-4 py-3"
								role="alert">
								<svg
									className="fill-current w-4 h-4 mr-2"
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 20 20">
									<path d="M12.432 0c1.34 0 2.01.912 2.01 1.957 0 1.305-1.164 2.512-2.679 2.512-1.269 0-2.009-.75-1.974-1.99C9.789 1.436 10.67 0 12.432 0zM8.309 20c-1.058 0-1.833-.652-1.093-3.524l1.214-5.092c.211-.814.246-1.141 0-1.141-.317 0-1.689.562-2.502 1.117l-.528-.88c2.572-2.186 5.531-3.467 6.801-3.467 1.057 0 1.233 1.273.705 3.23l-1.391 5.352c-.246.945-.141 1.271.106 1.271.317 0 1.357-.392 2.379-1.207l.6.814C12.098 19.02 9.365 20 8.309 20z" />
								</svg>
								<p>
									No concerts for this location. Please select another location.
								</p>
							</div>
						)}
					</div>

					{/*  */}
				</div>
			</div>
		</>
	);
}
