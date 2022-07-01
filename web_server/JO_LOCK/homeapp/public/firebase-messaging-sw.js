importScripts("https://www.gstatic.com/firebasejs/8.7.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.7.1/firebase-messaging.js");

firebase.initializeApp({
    apiKey: "AIzaSyCQ28W2WS1tIKXRUIgOz4ECDEnfde8ajw8",
    authDomain: "jolcok-f6c42.firebaseapp.com",
    databaseURL: "https://jolcok-f6c42-default-rtdb.firebaseio.com",
    projectId: "jolcok-f6c42",
    storageBucket: "jolcok-f6c42.appspot.com",
    messagingSenderId: "643614501080",
    appId: "1:643614501080:web:25412323fd79b5ad53cfad",
    measurementId: "G-HMTNRCLBXK"
  });

const messaging = firebase.messaging();

