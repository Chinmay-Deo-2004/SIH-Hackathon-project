import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core'; 
import TextField from '@material-ui/core';
import FormHelperText from '@material-ui/core';
import FormControl from '@material-ui/core';
import { link } from 'react-router-dom';
import FormControlLabel from '@material-ui/core';

export default class CreateAudioFile extends Component {
    constructor(props){
        super(props);
        this.state = {
            audio_file : null,
        }

        this.handleAudioFileChange = this.handleAudioFileChange.bind(this); // This binding is necessary to make `this` work in the callback
        this.handleCreateAudioButtonPressed = this.handleCreateAudioButtonPressed.bind(this);

    } 

    handleAudioFileChange = (event) => {
        this.setState({
            audio_file: event.target.value,
        })
    }

    handleCreateAudioButtonPressed() {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ audio_file: this.state.audio_file })
        };
        fetch("/api/create-audio-entry", requestOptions).then((response) => {
            return response.json();
        }).then((data) => {
            console.log(data);
        });
    }

    render() {
        return <p>hi</p>;
    }
}
