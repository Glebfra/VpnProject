import './App.css';
import Login from "./Modules/Auth/Login";
import Main from "./Modules/Main/Main";

function App() {
    if (localStorage.getItem('token') == null) {
        return (
            <div className='App'>
                <Login/>
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
