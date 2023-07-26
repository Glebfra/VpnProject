import Main from "./Modules/Main/Main";
import Login from "./Modules/Auth/Login";
import Register from "./Modules/Auth/Register";
import {Route} from "react-router";
import App from "./App";

export default (
    <Route component={App} path={'/'}>
        <Route component={Login} path={'login'}/>
        <Route component={Register} path={'register'}/>
        <Route component={Main} path={'main'}/>
    </Route>
);