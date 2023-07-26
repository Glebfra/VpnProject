import './App.css';
import LoginForm from "./Modules/Auth/Login";
import axios from "axios";

axios.defaults.baseURL = 'http://localhost-api/api';

function App() {
    if (localStorage.getItem('token') == null) {
        return (
            <div className='app'>
                <LoginForm/>
            </div>
        );
    } else {
        return (
            <div className='App'>
                <Main/>
            </div>
        );
    }
}

export default App;
