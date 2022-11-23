import React from "react";
import { useState } from "react";
import { useToken, login } from "./auth.js";
import { useNavigate } from 'react-router-dom';

const LoginForm = () => {
    const [login] = useToken();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    // const [submitted, setSubmitted] = useState(false);
    // const [invalid, setInvalid] = useState(false);
    const navigate = useNavigate();



    const handleSubmit = async e => {
        e.preventDefault();
        await login(username, password); 
        console.log(username, "is logged in")
        navigate('/');
    };


  return (
    <>
      <div>
            <div>
                <div>
                    <h1>Sign in</h1>
                    <form 
                    onSubmit={handleSubmit} 
                    id="LoginForm">
                        <div>
                            <input onChange={e => setUsername(e.target.value)} placeholder="you@gmail.com" type="email" id="username" value={username} />
                            <label htmlFor="email">Email Address</label>
                        </div> 
                        <div>
                            <input onChange={e => setPassword(e.target.value)} placeholder="Password" type="password" id="password" value={password}/>
                            <label htmlFor="password">Password</label>
                        </div> 
                        <button onClick={login}>Log In</button>
                    </form>
                </div>
            </div>
        </div>
    

    </>
  )
} 
export default LoginForm