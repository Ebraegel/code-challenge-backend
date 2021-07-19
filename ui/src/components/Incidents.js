import './Incidents.css'
import axios from 'axios';
import React, { useState, useEffect } from 'react'

export default function Incidents(props) {
    const [incidents, setIncidents] = useState([]);
    const [location, setLocation] = useState({})

    const getIncidents = async () => {
        const response = await axios.get('/backend/incidents', {params: {lat: 57.29905319213867, long: 13.135849952697754}})
        console.log('Got incidents:');
        console.log(response.data);
        setIncidents(response.data)
    }

    const getLocation = async () => {
        navigator.geolocation.getCurrentPosition(function(position) {
            console.log("Latitude is :", position.coords.latitude);
            console.log("Longitude is :", position.coords.longitude);
            setLocation({lat: position.coords.latitude, long: position.coords.longitude})

        },
            function(error){console.log(error)});    }


    useEffect(() => {
        getLocation()
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
