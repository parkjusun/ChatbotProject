// @ts-ignore
import React, {Component} from "react";

// @ts-ignore
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import { Home, MyChatBot, Join, Login } from "./components/index";
import './App.css';

class App extends Component<any, any>{
  public render(){
    return  <Router>
      <Link to="/">홈 이동</Link><br/>
      <Link to="/chat">챗봇 이동</Link><br/>
      <Link to="/join">회원가입 이동</Link><br/>
      <Link to="/login">로그인 이동</Link>

      <Route exact path='/' component={Home}/>
      <Route exact path='/chat' component={MyChatBot}/>
      <Route exact path='/join' component={Join}/>
      <Route exact path='/login' component={Login}/>
    </Router>
  }
}

export default App;