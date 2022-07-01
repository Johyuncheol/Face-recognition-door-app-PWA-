const express = require('express');
const path = require('path');
const app = express();
var router = express.Router();
const bodyParser = require('body-parser');


//ajax 위해서 
app.use(express.json());
var cors = require('cors');
app.use(cors());
const spawn = require('child_process').spawn; 

app.listen(8080, function () {
  console.log('listening on 8080')
}); 

app.use(express.static(path.join(__dirname, '../homeapp/build')));

app.get('/', function (요청, 응답) {
  응답.sendFile(path.join(__dirname, '../homeapp/build/index.html'));
});

app.get('*', function (요청, 응답) {
  응답.sendFile(path.join(__dirname, '../homeapp/build/index.html'));
});


//firebase
var admin = require("firebase-admin")
var firestore = require("firebase-admin/firestore");

var serviceAccount = require("./lock-2674d-firebase-adminsdk-1vxls-912772558b.json");

admin.initializeApp({ // 서비스계정으로 초기화 권한부여
  credential: admin.credential.cert(serviceAccount)
});

const db = firestore.getFirestore();

app.post('/who', (req, res)=>{
  let name = req.body.name;
    console.log(name);
    console.log('옴 ');

  const result = spawn('python', ['./FCM_who.py']);
  result.stdout.on('data', (result)=>{ console.log(result.toString()); });

});

app.post('/doorOption', (req, res)=>{
  let name = req.body.name;
    console.log(name);
    console.log('open하세요 ');

  const result = spawn('python', ['./socket_server.py','open']);
  result.stdout.on('data', (result)=>{ console.log(result.toString()); });

});

app.post('/face', (req, res)=>{
  let name = req.body.name;
    console.log(name);
    console.log('얼굴학습');

  const result = spawn('python', ['./dnn_real.py']);
  result.stdout.on('data', (result)=>{ console.log(result.toString()); });

});

app.post('/facedown', (req, res)=>{
  let name = req.body.name;
    console.log(name);
    console.log('얼굴다운');

  const result = spawn('python', ['./socket_server.py','train']);
  result.stdout.on('data', (result)=>{ console.log(result.toString()); });

});
