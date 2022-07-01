import React,{ useEffect, useState } from 'react'
import firebase from 'firebase/app';
import {Route} from 'react-router-dom';
import { Link } from 'react-router-dom'
import axios from 'axios'
import $ from "jquery";

const Door = ({location}) =>{


  const [faceId, setfaceId] = useState({
    id: "",
    name: "",
  });

  /* input value 변경 ==> onChange */
  const onChangefaceId = (e) => {
    setfaceId({
      ...faceId,
      [e.target.name]: e.target.value,
    });
    console.log(faceId)
  };


  useEffect(()=>{

    var changeDataRef = firebase.database().ref('총인원').child('등록자수'); 
    changeDataRef.on("value", (snapshot)=>{
     
      var a
      a=snapshot.val()
      console.log(a)

      
      var 탬플릿 = `현재 등록인원 ${a}`;
      $('.fid').append(탬플릿)

    });
  },[])


  const train = ()=>{
    firebase.database().ref('등록자이름').child(faceId.id).set(faceId.name)
    firebase.database().ref('도어락').child('얼굴학습').set('on')
    // alert("얼굴등록중")
    }


return(
  <div >
    <div className='fid'></div>
    <br/>
    <input type="text"  name="id" placeholder="등록할 Id" onChange={onChangefaceId} />
    <input type="text"  name="name" placeholder="등록할 이름" onChange={onChangefaceId} />

    <div class="btn-holder">
      <button onClick={train} className='btn btn-2 hover-slide-right'>
      <span>얼굴인식요청</span>
    </button>
    </div>
    
    <ul>
    <li><a  className='door_li' href='door_unknown'>미확인</a></li>
    <li><a  className='door_li' href='door_known'>인식</a></li>
    <li><a  className='door_li' href='door_all'>전체</a></li>
    </ul>   
  </div>
);
}

export default Door;