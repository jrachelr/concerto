import { useState, useEffect } from "react";
import { useAuthContext } from "../auth";

export default function AccountInfo() {
	const [userInfo, setUserInfo] = useState({});
	const { token } = useAuthContext();

	useEffect(() => {
		async function getUserInfo() {
			const userURL = `${process.env.REACT_APP_USERS_API_HOST}/users/current`;

			const fetchConfig = {
				method: "get",
				headers: {
					Authorization: "Bearer " + token,
					"Content-Type": "application/json",
				},
			};
			const response = await fetch(userURL, fetchConfig);
			if (response.ok) {
				const data = await response.json();

				setUserInfo(data);
			}
		}
		if (token) {
			getUserInfo();
		}
	}, [token]);

	return (
		<>
			<h1 className="pt-8 text-center text-3xl font-bold leading-8 tracking-tight text-white sm:text-4xl">
				Hi {userInfo.first_name}!
			</h1>
		</>
	);
}
