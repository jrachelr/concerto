import { useAuthContext } from "./auth";
import { useState, useEffect } from "react";
import SideBar from "./Layout/SidebarNav";

// stop continuous loop
// add remove button
// insert logic if no concerts infavorites
// add 'hello user'
// styling

export default function Favorites() {
  const { token, user } = useAuthContext();
  const [concerts, setConcerts] = useState([]);

  useEffect(() => {
    async function getFavoriteConcerts() {
      const favoritesURL = `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/concerts/favorites/${user.id}`;

      const fetchConfig = {
        method: "get",
        headers: {
          Authorization: "Bearer " + token,
          "Content-Type": "application/json",
        },
      };

      const response = await fetch(favoritesURL, fetchConfig);
      if (response.ok) {
        const data = await response.json();
        setConcerts(data.concerts);
      }
    }
    getFavoriteConcerts();
  }, [token, user, concerts]);

  async function removeFavorite(concert) {
    const removeURL = `${process.env.REACT_APP_SAMPLE_SERVICE_API_HOST}/concerts/favorites/${user.id}/${concert.id}`;
    const fetchConfig = {
      method: "delete",
      headers: {
        Authorization: "Bearer " + token,
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(removeURL, fetchConfig);
    if (response.ok) {
      console.log(removeURL);
      console.log(response);
      setConcerts([...concerts]);
    }
  }

  return (
    <>
      <SideBar />
      <h2 className="pt-8 text-center text-3xl font-bold leading-8 tracking-tight text-gray-900 sm:text-4xl">
        Your favorites:
      </h2>
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-3xl">
          <div className="bg-white">
            <div className="mx-auto max-w-7xl overflow-hidden py-16 px-4 sm:py-24 sm:px-6 lg:px-8">
              <div className="grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-3 lg:grid-cols-3 lg:gap-x-8 ">
                {concerts.map((concert) => (
                  <div
                    key={concert.id}
                    className="group text-sm border-solid border-slate-900"
                  >
                    <div className="aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-lg bg-gray-200   ">
                      <img
                        src={concert.image_url}
                        alt={concert.imageAlt}
                        className="h-full w-full object-cover object-center"
                      />
                    </div>
                    <h3 className="mt-4 font-medium text-gray-900">
                      {concert.artist_name}
                    </h3>
                    <h3 className="mt-4 font-medium text-gray-900">
                      {concert.concert_name}
                    </h3>
                    <p className=" text-gray-500">{concert.start_date}</p>
                    <p className="mt-2 font-medium text-gray-900">
                      ${concert.max_price}
                    </p>
                    <p className="mt-2 font-medium text-gray-900">
                      {concert.venue}
                    </p>
                    <button
                      concert={concert.id}
                      className="text-center inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800"
                      onClick={() => removeFavorite(concert)}
                    >
                      Remove from Favorites
                    </button>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
