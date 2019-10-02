import React from "react";
import { Subscribe } from "unstated";

export default function withContext(containers, WrappedComponent) {
    return function WithContext(props) {
        return (
            <Subscribe to={containers}>
                {(...containers) => {
                    const mappings = containers.reduce(
                        (acc, container) => ({
                            ...acc,
                            [container.propName]: container
                        }),
                        {}
                    );

                    return <WrappedComponent {...mappings} {...props} />;
                }}
            </Subscribe>
        );
    };
}
