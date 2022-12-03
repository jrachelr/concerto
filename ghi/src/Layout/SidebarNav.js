import { NavLink } from "react-router-dom";

export default function SideBar() {
  return (
    <div
      className="fixed top-0 left-0 w-30
     min-h-0 flex-1 flex-col bg-indigo-700"
    >
      <div className="flex flex-1 flex-col h-screen overflow-y-auto pt-5 pb-4">
        <div className="flex flex-shrink-0 items-center px-4">
          <img
            className="h-8 w-auto"
            src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=300"
            alt="Your Company"
          />
        </div>
        <nav
          className="mt-5 flex-1 space-y-1 px-2 text-white"
          aria-label="Sidebar"
        >
          <NavLink href="myconcerts/">
            <span className=" hover:bg-indigo-600 hover:bg-opacity-75 group flex items-center px-2 py-2 text-sm font-medium rounded-md ">
              My Concerts
            </span>
          </NavLink>
          <NavLink href="myaccount/">
            <span className=" hover:bg-indigo-600 hover:bg-opacity-75 group flex items-center px-2 py-2 text-sm font-medium rounded-md ">
              My Account
            </span>
          </NavLink>
          <NavLink to="logout/">
            <span className=" hover:bg-indigo-600 hover:bg-opacity-75 group flex items-center px-2 py-2 text-sm font-medium rounded-md ">
              Logout
            </span>
          </NavLink>
        </nav>
      </div>
    </div>
  );
}
