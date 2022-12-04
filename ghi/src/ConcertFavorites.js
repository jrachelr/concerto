import { useAuthContext } from "./auth";
import { useState } from "react";
import SideBar from "./Layout/SidebarNav";

export default function Favorites() {
  const { token, user } = useAuthContext();
  const [concerts, setConcerts] = useState([]);

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
      console.log(concerts);
    }
  }
  getFavoriteConcerts();

  return (
    <>
      <SideBar />
      <div className="bg-white">
        <div className="mx-auto max-w-7xl overflow-hidden py-16 px-4 sm:py-24 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-3 lg:gap-x-8">
            {concerts.map((concert) => (
              <div key={concert.id} className="group text-sm">
                <div className="aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-lg bg-gray-100 group-hover:opacity-75">
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
                  {concert.max_price}
                </p>
                <p className="mt-2 font-medium text-gray-900">
                  {concert.venue}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
