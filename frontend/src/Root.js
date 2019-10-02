import React from "react";
import { Provider } from "unstated";

import App from "./components/App";

const Root = () => (
    <Provider>
        <App />
    </Provider>
);

export default Root;
