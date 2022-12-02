import usePlacesAutocomplete from "use-places-autocomplete";
import { useState } from "react";

const SearchComponent = ({ getConcerts, setConcerts }) => {
	const {
		ready,
		value,
		suggestions: { status, data },
		setValue,
		clearSuggestions,
	} = usePlacesAutocomplete({
		requestOptions: {
			/* Define search scope here */
		},
		debounce: 300,
	});
	const [city, setCity] = useState("");
	const [state, setState] = useState("");

	const handleInput = (e) => {
		// Update the keyword of the input element
		setValue(e.target.value);
	};

	const handleSelect =
		({ description }) =>
		() => {
			setValue(description, false);
			clearSuggestions();
			setCity(description.split(",")[0].split(" ").join("%20"));
			setState(description.split(",")[1]);
		};

	const renderSuggestions = () =>
		data.map((suggestion) => {
			const {
				place_id,
				structured_formatting: { main_text, secondary_text },
			} = suggestion;

			return (
				<li key={place_id} onClick={handleSelect(suggestion)}>
					<strong>{main_text}</strong> <small>{secondary_text}</small>
				</li>
			);
		});

	const handleSubmit = async (event) => {
		event.preventDefault();
		setConcerts([]);
		getConcerts(city, state);
		setCity("");
		setState("");
		event.target.reset();
	};

	return (
		<form id="search-location" onSubmit={handleSubmit}>
			<div className="rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-indigo-600 focus-within:ring-1 focus-within:ring-indigo-600">
				<label
					htmlFor="name"
					className="block text-xs font-medium text-gray-900">
					Location
				</label>
				<input
					value={value}
					onChange={handleInput}
					disabled={!ready}
					placeholder="Where are you going?"
					className="block w-full rounded-md bg-white opacity-100 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
				/>
			</div>
			{status === "OK" && <ul>{renderSuggestions()}</ul>}
			<div className="flex justify-center">
				<button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
					Button
				</button>
			</div>
		</form>
	);
};

export default SearchComponent;
