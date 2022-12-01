import { NavLink } from "react-router-dom";
export default function Header() {
  return (
    <>
      <header className="bg-indigo-600 opacity-75">
        <nav
          className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8"
          aria-label="Top"
        >
          <div className="flex w-full items-center justify-between border-b border-indigo-500 opacity-100 py-6 lg:border-none">
            <div className="ml-10 space-x-4">
              <NavLink
                to="login/"
                className="inline-block rounded-md border border-transparent bg-indigo-500 opacity-100 py-2 px-4 text-base font-medium text-white hover:bg-opacity-75"
              >
                Sign in
              </NavLink>
              <NavLink
                to="signup/"
                className="inline-block rounded-md border border-transparent bg-white py-2 px-4 text-base font-medium text-indigo-600 opacity-100 hover:bg-indigo-50"
              >
                Sign up
              </NavLink>
              <NavLink
                to="logout/"
                className="inline-block rounded-md border border-transparent bg-white py-2 px-4 text-base font-medium text-indigo-600 opacity-100 hover:bg-indigo-50"
              >
                Logout
              </NavLink>
            </div>
          </div>
        </nav>
      </header>
    </>
  );
}
