import './Incidents.css'
import axios from 'axios';
import React, { useState, useEffect } from 'react'

export default function Incidents(props) {
    const [incidents, setIncidents] = useState([]);

    const getIncidents = async () => {
        const response = await axios.get('http://localhost:5000/incidents')
        console.log('Got incidents:');
        console.log(response.data);
        setIncidents(response.data.incidents)
    }

    useEffect(() => {
        getIncidents()
    }, [])

    return (
        <div id="incidents">
            <h1>Traffic Incidents</h1>
            <hr></hr>
            {
                incidents.length === 0 ? 'No incidents created yet' : (
                    <table align="center">
                        <thead>
                            <tr>
                                <th>Priority</th>
                                <th>Title</th>
                                <th>Location</th>
                                <th>Description</th>
                                <th>Category</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                incidents.map((incident) => {
                                    return (
                                        <tr key={incident.id}>
                                            <td>{incident.priority}</td>
                                            <td>{incident.title}</td>
                                            <td>{incident.exactlocation}</td>
                                            <td>{incident.description}</td>
                                            <td>{incident.category}</td>
                                        </tr>
                                    )
                                })
                            }
                        </tbody>
                    </table>
                )
            }
        </div>
    )

}
