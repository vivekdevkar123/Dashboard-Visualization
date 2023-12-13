// YourComponent.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BarChart from './BarChart';

function Dashboard() {
    const [data, setData] = useState([]);

    useEffect(() => {
        // Fetch data from Django API
        axios.get('http://localhost:8000/api/insights/')
            .then(response => setData(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div className="App">
            <h1>Chart.js Dashboard</h1>
            <BarChart data={data} />  {/* Render your Chart component with the fetched data */}
        </div>
    );
}

export default Dashboard;
