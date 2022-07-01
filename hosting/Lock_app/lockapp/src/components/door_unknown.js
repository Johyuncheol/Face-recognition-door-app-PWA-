import {db} from '../firebase.js'
import firebase from 'firebase/app';
import "firebase/auth"
import "firebase/database"
import React, { useEffect } from 'react'
import { useState } from 'react';
import $ from "jquery";
import '../App.css';
// import axios from 'axios'


const Door_unknown = ({location}) =>{
let [data,setData] = useState();

useEffect(()=>{

  var changeDataRef = firebase.database().ref('미확인사진'); 
  changeDataRef.on("value", (snapshot)=>{
   
    var a= [];
    a=snapshot.val()
    a.reverse()
    console.log(a)
    $('.content').empty()
    for (let i = 1; i < 10; i++){
      if(a[i]==undefined)
      {
        break
      }
      var time = a[i].slice(-29, -14);
      console.log(time)    
      var 탬플릿 = `<p><img  src='${a[i]}'/>'${time}'</p>`;
      $('.contents_box').append(탬플릿)

    }
  });
},[])


// useEffect(()=>{
// db.collection('방문자').where('미확인url','array-contains','미확인').onSnapshot((querySnapshot)=>{
//   querySnapshot.forEach((doc) => {
//     var a= [];
//     a=doc.data().미확인url
//     a.reverse()
//     $('.content').empty()
//     for (let i = 1; i < 10; i++){
//       if(a[i]===undefined)
//       {
//         break
//       }
//       var time = a[i].slice(-29, -14);
//       console.log(time)    
//       var 탬플릿 = `<p><img  src='${a[i]}'/>'${time}'</p>`;
//       $('.contents_box').append(탬플릿)
//     }
    
//   });
// });
// },)



const send = ()=>{
firebase.database().ref('도어락').child('상태').set('open')
alert("open 요청")
}


// useEffect(()=>{
// db.collection('도어락').where('상태','==','open').onSnapshot((querySnapshot)=>{
//   querySnapshot.forEach((doc) => {
        
//     // const send_fcm =()=>{
//     //   const client = axios.create();   // axios 기능생성
//     //   const name = '안녕';   
//     //   client.post('/doorOption' , {name} );   //axios 기능을 통한 post 사용및 name 값 전달.
//     // }
    
//     // send_fcm()
//     alert("문이 열렸습니다")
//   });
// });
// },)

return(
  <div >
    <div class="btn-holder">
      <button onClick={send} className='btn btn-2 hover-slide-right'>
        <span>open</span>
      </button>
     
    </div>
    
    <div className="contents_box"></div>
        
  </div>
);
}

export default Door_unknown;