import React, { Component } from 'react';
import{ BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";
import CreateAudioFile from './CreateAudioFile';
export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return (
        <Router>
            <Routes>
                <Route path='/' element={<p>This is Home Page</p>} />
                <Route path='/audio' element={<CreateAudioFile />} />
            </Routes>
        </Router>
        );
    }
}