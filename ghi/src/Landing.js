import "./index.css";
import { useState } from "react";
import SideBar from "./SidebarNav";
import SearchComponent from "./SearchComponent";
import ConcertList from "./ConcertList";
import { NavLink } from "react-router-dom";
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
        <header className="bg-indigo-600">
          <nav
            className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8"
            aria-label="Top"
          >
            <div className="flex w-full items-center justify-between border-b border-indigo-500 py-6 lg:border-none">
              <div className="ml-10 space-x-4">
                <NavLink
                  to="login/"
                  className="inline-block rounded-md border border-transparent bg-indigo-500 py-2 px-4 text-base font-medium text-white hover:bg-opacity-75"
                >
                  Sign in
                </NavLink>
                <NavLink
                  to="signup/"
                  className="inline-block rounded-md border border-transparent bg-white py-2 px-4 text-base font-medium text-indigo-600 hover:bg-indigo-50"
                >
                  Sign up
                </NavLink>
              </div>
            </div>
          </nav>
        </header>
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
            <form>
              <div className="rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-indigo-600 focus-within:ring-1 focus-within:ring-indigo-600">
                <label
                  htmlFor="name"
                  className="block text-xs font-medium text-gray-900"
                >
                  Location
                </label>
                <input
                  type="text"
                  name="name"
                  id="name"
                  className="block w-full rounded-md bg-white opacity-100 border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                  placeholder="Los Angeles"
                />
              </div>
              <button>Go</button>
            </form>
          </div>
          <SearchComponent getConcerts={getConcerts} />
          <ConcertList concerts={concerts} />

          {/*  */}
        </div>
      </div>
    </>
  );
}
