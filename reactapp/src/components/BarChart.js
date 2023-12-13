import React from 'react';
import { Line, Bar, Pie } from 'react-chartjs-2';

function BarChart({ data }) {
    const chartData = {
        labels: data.map(entry => entry.title),
        datasets: [
            {
                label: 'Intensity',
                fill: false,
                lineTension: 0.1,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: 'rgba(75,192,192,1)',
                pointBackgroundColor: '#fff',
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                pointHoverBorderColor: 'rgba(220,220,220,1)',
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: data.map(entry => entry.intensity),
            },
        ],
    };

    const chartOptions = {
        scales: {
            x: {
                type: 'category',
            },
            y: {
                beginAtZero: true,
            },
        },
    };

    return (
        <>
            <div>
                <Line data={chartData} options={chartOptions} />
            </div>
            <div>
                <Bar data={chartData} options={chartOptions} />
            </div>
            <div>
                <Pie data={chartData} options={chartOptions} />
            </div>

        </>
    );
}

export default BarChart;
