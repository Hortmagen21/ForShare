import React from "react";

import LoginForm from "./LoginForm";
import api from "../../api";

class Login extends React.Component {
    state = {
        username: "",
        password: "",
        isLoggedIn: false,
        isSubmitting: false,
        hasError: false
    };

    handleInputEvent = (event, name) => {
        this.setState({ [event.target.name || name]: event.target.value });
    };

    handleSubmit = async () => {
        try {
            const loginCallback = await api.authentication.signIn(
                this.state.username,
                this.state.password
            );

            this.handleLoginSuccess(loginCallback);
        } catch (error) {
            this.handleLoginFail(error, "Login failed :(");
        }
    };

    handleLoginSuccess(callback) {
        this.setState(
            {
                isLoggedIn: true,
                isSubmitting: false,
                hasError: false
            },
            callback
        );
    }

    handleLoginFail(error, fallbackMessage) {
        const errorMessage =
            (error && error.response && error.response.data) || fallbackMessage;

        // somehow notify

        this.setState({
            isLoggedIn: false,
            isSubmitting: false,
            hasError: true
        });
    }

    render() {
        const {
            username,
            password,
            isLoggedIn,
            isSubmitting,
            hasError
        } = this.state;

        return (
            <LoginForm
                username={username}
                password={password}
                isLoggedIn={isLoggedIn}
                isSubmitting={isSubmitting}
                hasError={hasError}
                onUsernameChange={this.handleInputEvent}
                onPasswordChange={this.handleInputEvent}
                onSubmit={this.handleSubmit}
            />
        );
    }
}

export default Login;
