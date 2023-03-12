import React from "react";
import axios from "axios";
import logo from './logo.svg';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import './App.css';
import UserList from './components/User.js'
import ProjectList from "./components/Project";
import ToDoList from "./components/ToDo";
import Footer from "./components/Footer.js";
import Menu from "./components/Menu.js";

const DOMAIN = 'http://127.0.0.1:8001/api/'
const get_url = (url) => `${DOMAIN}${url}`


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            users: [],
            projects: [],
            notes: []
        };
    }

    componentDidMount() {
        axios.get(get_url('users/'))
            .then(response => {
                this.setState({users: response.data})
            }).catch(error => console.log(error))


        axios.get(get_url('projects/'))
            .then(response => {
                //console.log(response.data)
                this.setState({projects: response.data.results})
            }).catch(error => console.log(error))

        axios.get(get_url('notes/'))
            .then(response => {
                //console.log(response.data)
                this.setState({todos: response.data.results})
            }).catch(error => console.log(error))
    }

    render() {
        return (

            <Router>
                <Menu/>
                <div className="App">

                    <Switch>
                        <Route exact path='/' component={() => <UserList items={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.users} />} />
                        <Route exact path='/notes' component={() => <ToDoList items={this.state.users} />} />
                        <Route component={NotFound404} />

                    </Switch>
                </div>
                <Footer/>
            </Router>


        )
    }
}

export default App;
