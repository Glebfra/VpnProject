import './App.css';
import Login from "./Modules/Auth/Login";
import {redirect} from 'react-router-dom'

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
          <b> Main page </b>
        </div>
    );
  }
}

export default App;
