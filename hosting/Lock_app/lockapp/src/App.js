import {Route} from 'react-router-dom';
import Door from './components/door.js';
import Door_unknown from './components/door_unknown.js';
import Door_All from './components/door_All.js';
import Door_known from './components/door_known.js';
import Home from './components/home.js';
import Profiles from './components/profiles';
//import History_home from './components/history_home.js';
import { Header } from './components/header';
import React,{ useEffect }from 'react';
import './App.css';
import firebase from "firebase/app";
import {db} from './firebase.js'
import "firebase/auth"
import "firebase/database"



//import { firebaseApp } from "./firebase";

function App() {



useEffect(()=>{

  var changeDataRef = firebase.database().ref('도어락').child('미확인시도알림'); 
  changeDataRef.on("value", (snapshot)=>{
   console.log(snapshot.val())

    if(snapshot.val()=='on')
    {
      alert("문앞에 누가 왔어요")
    }
  });
},[])

useEffect(()=>{

  var changeDataRef = firebase.database().ref('도어락').child('문열림알림'); 
  changeDataRef.on("value", (snapshot)=>{
    if(snapshot.val()=='on')
    {
      alert("문이 열렸습니다")
    }
  });
},[])


useEffect(()=>{

  var changeDataRef = firebase.database().ref('도어락').child('얼굴학습'); 
  changeDataRef.on("value", (snapshot)=>{
   console.log(snapshot.val())
    if(snapshot.val()=='on')
    {
      alert('얼굴학습중')
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
      alert('얼굴학습완료 적용중')
    }
  });
},[])


// useEffect(()=>{
//   db.collection('알림').where('경고','==','on').onSnapshot((querySnapshot)=>{
//     querySnapshot.forEach((doc) => {
          
//       // const send_who =()=>{
//       //   const client = axios.create();   // axios 기능생성
//       //   const name = '누구';   
//       //   client.post('/who' , {name} );   //axios 기능을 통한 post 사용및 name 값 전달.
//       // }
      
//       // send_who()
//       alert("문앞에 누가 왔어요")
//     });
//   });
//   },)


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
