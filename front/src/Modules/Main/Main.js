import React from "react";
import axios from "axios";


class Main extends React.Component {
    loadUser() {
        axios.post('/get_user')
    }

    render() {
        return (
            <div className='Main'>
                <b>Main page</b> <br/>
            </div>
        );
    }
}

export default Main