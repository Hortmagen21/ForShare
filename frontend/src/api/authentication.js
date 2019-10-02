import axios from "axios";

export default {
    async signIn(username, password) {
        return axios
            .post("http://localhost:8000/api/login", { username, password })
            .then(res => res.data);
    },
    async fetchMe() {
        // return axios.get("http://localhost:8000/api/me").then(res => res.data);
        return new Promise(f => setTimeout(() => f(null), 1000));
        return new Promise(f =>
            setTimeout(
                () =>
                    f({
                        id: "hash-234.h23tnauue-344",
                        username: "cturtle",
                        bio: "passionate about coding"
                    }),
                1000
            )
        );
    }
};
