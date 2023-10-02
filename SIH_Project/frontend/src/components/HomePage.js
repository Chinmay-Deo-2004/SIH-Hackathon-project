import React, { Component } from 'react';
import{ BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";
import CreateAudioFile from './CreateAudioFile';
import { useForm } from "react-hook-form";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }
    render(){
        return (
        <Router>
            <Routes>
                <Route path='/' element={
                    function app(){
                        const { register, handleSubmit} = useForm()
                        const onSubmit = (data) => {
                            console.log(data)
                        }
                        return (
                            <form onSubmit={handleSubmit(onSubmit)}>
                                <input ref={register} type="file" name="audio" />
                                <button>Upload</button>
                            </form>
                        );
                    }
                    export default app ;
                } />
                <Route path='/audio' element={<CreateAudioFile />} />
            </Routes>
        </Router>
        );
    }
}