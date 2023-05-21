import React from "react";


class LoginForm extends React.Component {
    state = {
        name: "",
        surname: ""
    };

    onFirstNameChanged = event =>
        this.setState({
            name: event.target.value
        });

    onLastNameChanged = event =>
        this.setState({
            surname: event.target.value
        });

    render() {
        return (
            <div align='center'>
                <li>
                    <ul>
                        <text>First Name</text>
                        <input type='text' name='name' onChange={this.onFirstNameChanged}/>
                    </ul>
                    <ul>
                        <text>Last Name</text>
                        <input type='text' name='surname' onChange={this.onLastNameChanged}/>
                    </ul>
                </li>
            </div>
        );
    }
}

export default LoginForm;
