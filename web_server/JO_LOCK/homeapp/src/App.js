import {Route} from 'react-router-dom';
import Door from './components/door.js';
import Door_unknown from './components/door_unknown.js';
import Door_All from './components/door_All.js';
import Door_known from './components/door_known.js';
import Home from './components/home.js';
import Profiles from './components/profiles';
import History_home from './components/history_home';
import { Header } from './components/header';
import React,{ useEffect }from 'react';
import './App.css';
import firebase from "firebase/app";
import '@firebase/messaging';
import "firebase/auth"
import "firebase/database"
import axios from 'axios'

import { firebaseApp } from "./firebase";

function App() {


const db = firebase.firestore();

  useEffect(()=>{

    var changeDataRef = firebase.database().ref('도어락').child('미확인시도알림'); 
    changeDataRef.on("value", (snapshot)=>{
     console.log(snapshot.val())
      if(snapshot.val()=='on')
      {
        const send_who =()=>{
          const client = axios.create();   // axios 기능생성
          client.post('http://localhost:8080/who');   //axios 기능을 통한 post 사용및 name 값 전달.
        }
        
        send_who()
      }

      firebase.database().ref('도어락').child('미확인시도알림').set('off')
    });
  },[])


  useEffect(()=>{

    var changeDataRef = firebase.database().ref('도어락').child('상태'); 
    changeDataRef.on("value", (snapshot)=>{
     console.log(snapshot.val())
      if(snapshot.val()=='open')
      {
        const send_fcm =()=>{
          const client = axios.create();   // axios 기능생성
          const name2 = '안녕';   
          client.post('http://localhost:8080/doorOption' , {name2} );   //axios 기능을 통한 post 사용및 name 값 전달.
        }
        
        send_fcm()
      }
    });
  },[])


  useEffect(()=>{

    var changeDataRef = firebase.database().ref('도어락').child('문열림알림'); 
    changeDataRef.on("value", (snapshot)=>{
      if(snapshot.val()=='on')
      {
        // alert("문이 열렸습니다")
      }
    });
  },[])

  useEffect(()=>{

    var changeDataRef = firebase.database().ref('도어락').child('얼굴학습'); 
    changeDataRef.on("value", (snapshot)=>{
     console.log(snapshot.val())
      if(snapshot.val()=='on')
      {
        const face =()=>{
          const client = axios.create();   // axios 기능생성  
          client.post('http://localhost:8080/face');   //axios 기능을 통한 post 사용및 name 값 전달.
        }
        
        face()
      }
      firebase.database().ref('도어락').child('얼굴학습').set('off') 
    });
  },[])

  useEffect(()=>{

    var changeDataRef = firebase.database().ref('도어락').child('파일다운'); 
    changeDataRef.on("value", (snapshot)=>{
     console.log(snapshot.val())
      if(snapshot.val()=='on')
      {
        const face =()=>{
          const client = axios.create();   // axios 기능생성  
          client.post('http://localhost:8080/facedown');   //axios 기능을 통한 post 사용및 name 값 전달.
        }
        
        face()
      }
    });
  },[])



  return (
    <div className='App'>
      <header> 

        <Header></Header>
  
        </header>

      <body className='main'>
        
        <Route path ="/" component={Home} exact ={true} /> 
        <Route path ="/door" component={Door} />
        <Route path ="/window" component={Profiles} />
        <Route path ="/light" component={Profiles} />
        <Route path ="/speaker" component={Profiles} />
        <Route path ="/door_unknown" component={Door_unknown} />
        <Route path ="/door_known" component={Door_known} />
        <Route path ="/door_all" component={Door_All} />

      </body>
      

    </div>
  );
}

export default App;
