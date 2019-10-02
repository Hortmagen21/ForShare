import React from "react";

import {
    BrowserRouter as Router,
    Switch,
    Route,
    Redirect
} from "react-router-dom";

import Login from "./login/Login";

const UnauthenticatedRoutes = () => (
    <Switch>
        <Route exact path="/login" component={Login} />
        <Redirect
            to={{
                pathname: "/login",
                state: { referrer: window.location.pathname }
            }}
        />
    </Switch>
);

const AuthenticatedRoutes = () => <Switch></Switch>;

const Routes = ({ isAuthenticated }) => (
    <Router>
        {isAuthenticated ? <AuthenticatedRoutes /> : <UnauthenticatedRoutes />}
    </Router>
);

export default Routes;
