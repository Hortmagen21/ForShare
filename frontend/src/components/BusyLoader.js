import React from "react";
import { Dimmer, Loader } from "semantic-ui-react";

const BusyLoader = ({ active }) => (
    <Dimmer active={active} inverted>
        <Loader inverted>Please wait...</Loader>
    </Dimmer>
);

export default BusyLoader;
