import React from "react";
import { useState, useEffect } from "react";
import { useToken } from "../auth.js";
import { useNavigate } from "react-router-dom";
import { GiHarp } from "react-icons/gi";

const SignupForm = () => {
	// this destructuring has to be in the same order as in auth
	const [, login, , signup] = useToken();
	const [firstName, setFirstName] = useState("");
	const [lastName, setLastName] = useState("");
	const [username, setUsername] = useState("");
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const navigate = useNavigate();
	const [usernameList, setUsernameList] = useState(null);
	const [emailList, setEmailList] = useState(null);
	const [usernameTaken, setUsernameTaken] = useState(false);
	const [emailTaken, setEmailTaken] = useState(false);

	useEffect(() => {
		async function fetchUserList() {
			const response = await fetch(
				`${process.env.REACT_APP_USERS_API_HOST}/users`,
				{
					method: "get",
					credentials: "include",
				}
			);
			const data = await response.json();

			const usernames = [];
			const emails = [];

			for (const user of data.users) {
				usernames.push(user.username);
				emails.push(user.email);
			}
			setUsernameList(usernames);
			setEmailList(emails);
		}
		fetchUserList();

		if (usernameList !== null || emailList !== null) {
			if (usernameList.includes(username)) {
				console.log("username taken");
				setUsernameTaken(true);
			} else {
				setUsernameTaken(false);
			}

			if (emailList.includes(email)) {
				console.log("email taken");
				setEmailTaken(true);
			} else {
				setEmailTaken(false);
			}
		}
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [username, email]);

	const handleSubmit = async (e) => {
		e.preventDefault();
		signup(username, password, email, firstName, lastName);
		// login(username, password);
		if (usernameTaken || emailTaken) {
			return;
		} else {
			navigate("/");
		}
	};

	return (
		<>
			<div className="overflow-y-scroll bg-hero bg-cover bg-blend-overlay from-indigo-500 h-screen">
				<div className="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
					<div className="w-screen flex flex-wrap flex-row place-items-center">
						<div className="m`x-auto h-12 w-auto text-white place-content-center text-5xl">
							<GiHarp />
						</div>
					</div>
					<div className="sm:mx-auto sm:w-full sm:max-w-md">
						<h2 className="mt-6 text-center text-3xl font-bold tracking-tight text-white">
							Create an account
						</h2>
					</div>

					<div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
						<div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
							<form
								onSubmit={handleSubmit}
								id="signup form"
								value={username}
								className="space-y-6"
								action="#"
								method="POST">
								<div>
									<label
										htmlFor="firstName"
										className="block text-sm font-medium text-gray-700">
										First name
									</label>
									<div className="mt-1">
										<input
											onChange={(e) => setFirstName(e.target.value)}
											value={firstName}
											id="firstName"
											name="firstName"
											type="firstName"
											autoComplete="firstName"
											required
											className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
										/>
									</div>
								</div>

								<div>
									<label
										htmlFor="lastName"
										className="block text-sm font-medium text-gray-700">
										Last name
									</label>
									<div className="mt-1">
										<input
											onChange={(e) => setLastName(e.target.value)}
											value={lastName}
											id="lastName"
											name="lastName"
											type="lastName"
											autoComplete="lastName"
											required
											className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
										/>
									</div>
								</div>

								<div>
									<label
										htmlFor="username"
										className="block text-sm font-medium text-gray-700">
										Username
									</label>
									<div className="mt-1">
										<input
											onChange={(e) => setUsername(e.target.value)}
											value={username}
											id="username"
											name="username"
											type="username"
											autoComplete="username"
											required
											className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
										/>
									</div>
								</div>
								{usernameTaken === true && (
									<div
										className="mt-4 flex items-center bg-red-100 border border-red-400 text-red-700 text-sm font-bold px-4 py-3"
										role="alert">
										<svg
											className="fill-current w-4 h-4 mr-2"
											xmlns="http://www.w3.org/2000/svg"
											viewBox="0 0 20 20">
											<path d="M12.432 0c1.34 0 2.01.912 2.01 1.957 0 1.305-1.164 2.512-2.679 2.512-1.269 0-2.009-.75-1.974-1.99C9.789 1.436 10.67 0 12.432 0zM8.309 20c-1.058 0-1.833-.652-1.093-3.524l1.214-5.092c.211-.814.246-1.141 0-1.141-.317 0-1.689.562-2.502 1.117l-.528-.88c2.572-2.186 5.531-3.467 6.801-3.467 1.057 0 1.233 1.273.705 3.23l-1.391 5.352c-.246.945-.141 1.271.106 1.271.317 0 1.357-.392 2.379-1.207l.6.814C12.098 19.02 9.365 20 8.309 20z" />
										</svg>
										<p>Username is already taken.</p>
									</div>
								)}

								<div>
									<label
										htmlFor="email"
										className="block text-sm font-medium text-gray-700">
										Email address
									</label>
									<div className="mt-1">
										<input
											onChange={(e) => setEmail(e.target.value)}
											value={email}
											id="email"
											name="email"
											type="email"
											autoComplete="email"
											required
											className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
										/>
									</div>
								</div>
								{emailTaken === true && (
									<div
										className="mt-4 flex items-center bg-red-100 border border-red-400 text-red-700 text-sm font-bold px-4 py-3"
										role="alert">
										<svg
											className="fill-current w-4 h-4 mr-2"
											xmlns="http://www.w3.org/2000/svg"
											viewBox="0 0 20 20">
											<path d="M12.432 0c1.34 0 2.01.912 2.01 1.957 0 1.305-1.164 2.512-2.679 2.512-1.269 0-2.009-.75-1.974-1.99C9.789 1.436 10.67 0 12.432 0zM8.309 20c-1.058 0-1.833-.652-1.093-3.524l1.214-5.092c.211-.814.246-1.141 0-1.141-.317 0-1.689.562-2.502 1.117l-.528-.88c2.572-2.186 5.531-3.467 6.801-3.467 1.057 0 1.233 1.273.705 3.23l-1.391 5.352c-.246.945-.141 1.271.106 1.271.317 0 1.357-.392 2.379-1.207l.6.814C12.098 19.02 9.365 20 8.309 20z" />
										</svg>
										<p>Email is already taken.</p>
									</div>
								)}

								<div>
									<label
										htmlFor="password"
										className="block text-sm font-medium text-gray-700">
										Password
									</label>
									<div className="mt-1">
										<input
											onChange={(e) => setPassword(e.target.value)}
											value={password}
											id="password"
											name="password"
											type="password"
											autoComplete="current-password"
											required
											className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
										/>
									</div>
								</div>

								<div>
									<button
										type="submit"
										className="flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
										Create account
									</button>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</>
	);
};
export default SignupForm;
