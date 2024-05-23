import { useState, useEffect } from "react";

export default function App(){
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('http://localhost:5000/')
            .then(response => response.json())
            .then(data => setData(data))
    }, [])

    return (
        <div>
            <h1>My Microservice </h1>
            {data ? <p>{data.name}</p> : <p>Loading...</p>}
        </div>
    )
}