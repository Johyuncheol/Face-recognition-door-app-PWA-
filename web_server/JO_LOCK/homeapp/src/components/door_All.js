import {db} from '../firebase.js'
import firebase from 'firebase/app';
import "firebase/auth"
import "firebase/database"

import React, { useEffect } from 'react'
import { useState } from 'react';
import $ from "jquery";
import '../App.css';

const Door_All = ({location}) =>{


useEffect(()=>{

  var changeDataRef = firebase.database().ref('전체사진'); 
  changeDataRef.on("value", (snapshot)=>{
   
    var a= [];
    a=snapshot.val()
    a.reverse()
    console.log(a)
    $('.content').empty()
    for (let i = 1; i < 10; i++){
      if(a[i]===undefined)
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


return(
  <div >

    <div className="contents_box"></div>
        
  </div>
);
}

export default Door_All;