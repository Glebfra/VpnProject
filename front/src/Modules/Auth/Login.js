import React from "react";
import axios from 'axios'

class LoginForm extends React.Component {
    handleClick(e) {
        const form = e.target
        axios.post(
            '/login',
            {
                email: form.email.value,
                password: form.password.value
            }
        ).then(function (response) {
            console.log(response)
        })
    }

    onChange() {
        console.log('Change')
    }

    render() {
        return (
            <form className='LoginForm' onSubmit={this.handleClick}>
                <label>
                    <b> Email: </b>
                    <input name='email'/>
                </label><br/>
                <label>
                    <b> Password: </b>
                    <input name='password'/>
                </label><br/>

                <button type='submit'>
                    Отправить
                </button>
            </form>
        );
    }
}
export default LoginForm