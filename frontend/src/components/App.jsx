import { useState, useEffect } from "react";

export default function App(){
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const backendUrl = process.env.REACT_APP_BACKEND_URL;
        fetch(backendUrl)
            .then(response => response.json().then(data => ({ status: response.status, body: data })))
            .then(({ status, body }) => {
                if (status === 200) {
                    setData(body);
                } else {
                    setError(body.error);
                }
            })
            .catch(err => setError('Error fetching data'));
    }, [])

    return (
        <div>
            <h1>My Microservice</h1>
            {error ? <p>{error}</p> : (data ? <p>{data.name}</p> : <p>Loading...</p>)}
        </div>
    )
}
