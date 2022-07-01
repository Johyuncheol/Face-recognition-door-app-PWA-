//firebase.js
import "firebase/firestore";
import firebase from 'firebase/app';
import "firebase/auth"
import "firebase/database"

const firebaseConfig = {
    apiKey: "AIzaSyAYN_pMYdHba9tVYj_0XYPoRYXetZvevBw",
    authDomain: "lock-2674d.firebaseapp.com",
    databaseURL: "https://lock-2674d-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "lock-2674d",
    storageBucket: "lock-2674d.appspot.com",
    messagingSenderId: "130079254258",
    appId: "1:130079254258:web:ca22eac6546f91eb1c926b",
    measurementId: "G-K2ZFQVJY2X"
};


// firebaseConfig 정보로 firebase 시작
//firebase.initializeApp(firebaseConfig);

// firebase의 firestore 인스턴스를 변수에 저장
//const firestore = firebase.firestore();


// 필요한 곳에서 사용할 수 있도록 내보내기
export const firebaseApp = firebase.initializeApp(firebaseConfig);
export const db = firebase.firestore();
