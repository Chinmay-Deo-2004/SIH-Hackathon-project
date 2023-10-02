import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Typography, { Divider } from '@material-ui/core'; 
import TextField from '@material-ui/core';
import FormHelperText from '@material-ui/core';
import FormControl from '@material-ui/core';
import { link } from 'react-router-dom';
import FormControlLabel from '@material-ui/core';
import { useState } from 'react';

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
            audio_file: event.target.files[0],
        })
    }

    handleCreateAudioButtonPressed() {
        const formData = new FormData();
        formData.append('audio_file', this.state.audio_file);
        fetch("/api/create-audio-entry", {
            method: "POST",
            body: formData,
        }).then(response => response.json())
        .then(data => {
            console.log(data);
        }).catch(error => {
            console.log(error);
        });
    }

    render() {
        return (
            <div>
            <div>hi</div>
            <form>
                <input
                    type = "file"
                    value = {audio_file}
                    onChange = {this.handleAudioFileChange}
                />
            </form>
            </div>
        );
    }
}
