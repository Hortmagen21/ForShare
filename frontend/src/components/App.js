import React, { Fragment } from "react";

import Routes from "./Routes";
import { withAuthContainer } from "../containers/AuthContainer";
import BusyLoader from "./BusyLoader";

class App extends React.Component {
    componentDidMount() {
        this.props.AuthContainer.fetchMe();
    }

    render() {
        console.log(
            this.props.AuthContainer.isReady,
            this.props.AuthContainer.isAuthenticated
        );
        return (
            <Fragment>
                {this.props.AuthContainer.isReady && (
                    <Routes
                        isAuthenticated={
                            this.props.AuthContainer.isAuthenticated
                        }
                    />
                )}
                <BusyLoader active={!this.props.AuthContainer.isReady} />
            </Fragment>
        );
    }
}

export default withAuthContainer(App);
