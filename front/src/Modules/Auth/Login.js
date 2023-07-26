import React from "react";
import axios from "axios";
import {useNavigate} from "react-router";

class Login extends React.Component{

    onSubmitHandle(event) {
        event.preventDefault();
        axios.post(
            'login/',
            {
                email: event.target.email.value,
                password: event.target.password.value
            }
        ).then(response => {
            localStorage.setItem('token', response.data.token);
        }).catch(reason => {
            console.log(reason);
        });
    }

    render() {
        return (
            <form onSubmit={this.onSubmitHandle} name='LoginForm'>
                <label>
                    <b> Login: </b>
                    <input type='text' name='email'/>
                </label><br/>
                <label>
                    <b> Password: </b>
                    <input type='password' name='password'/>
                </label><br/>
                <button type='submit'>
                    <b> Submit </b>
                </button>
            </form>
        );
    }
}

export default Login