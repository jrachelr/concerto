import { NavLink } from "react-router-dom";
import { GiHarp } from "react-icons/gi";

export default function SideBar() {
  return (
    <div
      className="fixed top-0 left-0 w-30
     min-h-0 flex-1 flex-col bg-indigo-700"
    >
      <div className="flex flex-1 flex-col h-screen overflow-y-auto pt-5 pb-4">
        <nav
          className="mt-5 flex-1 space-y-1 px-2 text-white"
          aria-label="Sidebar"
        >
          <NavLink to="/">
            <span className="place-content-center hover:bg-indigo-600 hover:bg-opacity-75 group flex text-right px-2 py-2 text-5xl font-medium rounded-md ">
              <GiHarp />
            </span>
          </NavLink>

          <NavLink to="myconcerts/">
            <span className=" hover:bg-indigo-600 hover:bg-opacity-75 group flex items-center px-2 py-2 text-base font-medium rounded-md ">
              My Concerts
            </span>
          </NavLink>
          <NavLink to="logout/">
            <span className=" hover:bg-indigo-600 hover:bg-opacity-75 group flex items-center px-2 py-2 text-base font-medium rounded-md ">
              Logout
            </span>
          </NavLink>
        </nav>
      </div>
    </div>
  );
}
