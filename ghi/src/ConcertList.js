import { useEffect, useState } from "react";
import { useAuthContext } from "./auth";

const ConcertList = ({ concerts }) => {
	const [open, setOpen] = useState(false);
	const { token, user } = useAuthContext();
	// const [showFavButton, setShowFaveButton] = useState(true);

	useEffect(() => {
		if (concerts.length > 0) {
			console.log(concerts);
		}
	}, [concerts]);

	const addFavorite = async (concert) => {
		// take userID from user
		// create a post request to add the favorite concert to that user's list
		const favoriteUrl = `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/concerts/favorites/${user.id}`;

		const data = {
			concert_name: concert.concert_name,
			artist_name: concert.artist_name,
			start_date: concert.start_date,
			min_price: concert.min_price,
			max_price: concert.max_price,
		};

		const fetchConfig = {
			method: "post",
			body: JSON.stringify(data),
			headers: {
				Authorization: "Bearer " + token,
				"Content-Type": "application/json",
			},
		};

		const response = await fetch(favoriteUrl, fetchConfig);
		if (response.ok) {
			console.log("success!");
			// setShowFaveButton(false);
		}
	};

	return (
		<>
			<div className="flex justify-center grid grid-cols-4 gap-4">
				{concerts.map((concert, count) => {
					return (
						<>
							<div className="rounded-lg shadow-lg bg-white max-w-sm">
								<a
									href="#!"
									data-mdb-ripple="true"
									data-mdb-ripple-color="light">
									<img
										className="rounded-t-lg"
										src={concert.image_url}
										alt=""
									/>
								</a>
								<div className="p-6">
									<h5 className="text-gray-900 text-xl font-medium mb-2">
										{concert.artist_name}
									</h5>
									<p className="text-gray-700 text-base mb-4">
										<li>{concert.start_date}</li>
										<li>
											${concert.min_price}-${concert.max_price}
										</li>
										<li>{concert.venue}</li>
									</p>
									<button
										type="button"
										className="text-center inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
										onClick={() => setOpen(true)}>
										Details
									</button>{" "}
									{/* {showFavButton ? ( */}
									<button
										type="button"
										className="text-center inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
										onClick={(e) => addFavorite(concert)}>
										Favorite
									</button>
									{/* ) : null} */}
								</div>
							</div>
							{/* <ConcertModal open={open} setOpen={setOpen} concert={concert} /> */}
						</>
					);
				})}
			</div>
		</>
	);
};
export default ConcertList;
