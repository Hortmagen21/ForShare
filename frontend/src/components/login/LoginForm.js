import React from "react";
import {
    Button,
    Form,
    Grid,
    Header,
    Image,
    Message,
    Segment
} from "semantic-ui-react";

const LoginForm = ({
    username,
    password,
    onUsernameChange,
    onPasswordChange,
    onSubmit,
    isLoggedIn,
    isSubmitting,
    hasError
}) => (
    <Grid textAlign="center" style={{ height: "100vh" }} verticalAlign="middle">
        <Grid.Column style={{ maxWidth: 450 }}>
            <Header as="h2" color="teal" textAlign="center">
                Log in your messenger account
            </Header>
            <Form size="large" onSubmit={onSubmit}>
                <Segment stacked>
                    <Form.Input
                        fluid
                        icon="user"
                        iconPosition="left"
                        placeholder="Username"
                        name="username"
                        value={username}
                        onChange={onUsernameChange}
                    />
                    <Form.Input
                        fluid
                        icon="lock"
                        iconPosition="left"
                        placeholder="Password"
                        name="password"
                        type="password"
                        value={password}
                        onChange={onPasswordChange}
                    />

                    <Button
                        color="teal"
                        fluid
                        size="large"
                        loading={isSubmitting}
                        positive={isLoggedIn}
                        negative={hasError}
                    >
                        Login
                    </Button>
                </Segment>
            </Form>
            <Message>
                New to us? <a href="#">Sign Up</a>
            </Message>
        </Grid.Column>
    </Grid>
);

export default LoginForm;
