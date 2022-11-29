import "./index.css";
import SideBar from "./SidebarNav";
export default function Landing() {
	return (
		<>
			<div className="bg-indigo-700">
				<div className="mx-auto max-w-2xl py-16 px-4 text-center sm:py-20 sm:px-6 lg:px-8">
					<h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
						<span className="block">Concerto</span>
					</h2>
					<p className="mt-4 text-lg leading-6 text-indigo-200">
						A place for music lovers.
					</p>
					<a
						href="login/"
						className="mt-8 inline-flex w-full items-center justify-center rounded-md border border-transparent bg-white px-5 py-3 text-base font-medium text-indigo-600 hover:bg-indigo-50 sm:w-auto">
						Log In
					</a>
					{/* <a
            href="signup/"
            className="mt-8 inline-flex w-full items-center justify-center rounded-md border border-transparent bg-white px-5 py-3 text-base font-medium text-indigo-600 hover:bg-indigo-50 sm:w-auto"
          >
            Create Account
          </a> */}
				</div>
			</div>
		</>
	);
}
