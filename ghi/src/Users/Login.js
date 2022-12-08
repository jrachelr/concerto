import React from "react";
import { useState } from "react";
import { useToken } from "../auth.js";
import { NavLink, useNavigate } from "react-router-dom";
// import {login} from "../auth.js"


const LoginForm = () => {
  const [, login] = useToken();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  // const [loggedIn, setLoggedIn] = useState(false);
  // const [formValues, setFormValues] = useState(
  //     {
  //       username: "",
  //       password: "",
  //     }
  // );

  // const handleUsernameChange = (e) => {
  //   setLoggedIn(false);
  //   setFormValues((entries) => ({
  //     ...entries,
  //     username: e.target.value,
  //   }));
  // }

  // const handlePasswordChange = (e) => {
  //   setLoggedIn(false);
  //   setFormValues((entries) => ({
  //     ...entries,
  //     password: e.target.value
  //   })
  //   )
  // }


  // const handleLogin = async (e) => {
  //   e.preventDefault();
  //   const url = `${process.env.REACT_APP_USERS_API_HOST}/token`
  //   const form = new FormData();
  //   form.append("username", formValues["username"])
  //   form.append("password", formValues["password"])

  //   const response = await fetch(url, {
  //     method: "post",
  //     credentials: "include",
  //     body: form,
  //   });
  //   if (response.ok) {
  //       const tokenURL = `${process.env.REACT_APP_USERS_API_HOST}/token`;

  //     try {
  //       const response = await fetch(tokenURL, {
  //           credentials: "include",
  //       });
  //       if (response.ok) {
  //         const data = await response.json();
  //         const token = data.token;
  //         setLoggedIn(true)
  //         console.log(token)
  //       }
  //       } catch (e) {}
  //       return false;
  // }
  // let error = await response.json();
  // console.log(error)

  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(username, password);
    login(username, password);
    navigate("/");
  };


  

  return (
    <>
      <div className="flex min-h-full flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div className="sm:mx-auto sm:w-full sm:max-w-md">
          <img
            className="mx-auto h-12 w-auto"
            src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600"
            alt="Your Company"
          />
          <h2 className="mt-6 text-center text-3xl font-bold tracking-tight text-gray-900">
            Sign in to your account
          </h2>
        </div>

        <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
          {/* {loggedIn ?
          <div className="py-2">
            <NavLink to="/">
              <div className="alert alert-success">Login Successful!</div>
            </NavLink>
          </div>
          : null} */}
          <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
            <form
              onSubmit={handleSubmit}
              id="username"
              value={username}
              className="space-y-6"
              action="#"
              method="POST"
            >
              <div>
                <label
                  htmlFor="email"
                  className="block text-sm font-medium text-gray-700"
                >
                  Email address
                </label>
                <div className="mt-1">
                  <input
                    onChange={(e) => setUsername(e.target.value)}
                    value={username}
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="email"
                    required
                    // onInvalid={(e)=>{e.target.setCustomValidity("error message: Wrong Email")}}
                    className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                  />
                </div>
              </div>

              <div>
                <label
                  htmlFor="password"
                  className="block text-sm font-medium text-gray-700"
                >
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
                    // onInvalid={(e)=>{e.target.setCustomValidity("error message: Wrong Password")}}
                    className="block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-indigo-500 sm:text-sm"
                  />
                </div>
              </div>

              <div>
                <button
                  type="submit"
                  className="flex w-full justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                >
                  Log In
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginForm;
