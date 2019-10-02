import { Container } from "unstated";
import api from "../api";
import withContext from "../helpers/withContext";

export default class AuthContainer extends Container {
    propName = "AuthContainer";

    state = {
        credentials: undefined
    };

    get isReady() {
        return this.state.credentials !== undefined;
    }

    get isAuthenticated() {
        return this.state.credentials != null;
    }

    get credentials() {
        return this.state.credentials;
    }

    async signIn(username, password) {
        const credentials = await api.authentication.signIn(username, password);
        const done = () => this.setCredentials(credentials);

        return [credentials, done];
    }

    setCredentials(credentials) {
        this.setState({ credentials });
    }

    fetchMe = async () => {
        try {
            const credentials = await api.authentication.fetchMe();

            this.setCredentials(credentials);
        } catch (err) {
            /// todoo
        }
    };
}

export const withAuthContainer = WrappedComponent =>
    withContext([AuthContainer], WrappedComponent);
