<template>
    <div>
      <v-layout wrap justify-center mt-2>
        <v-flex xs11> 
          <video :class="{ 'flip-horizontal': cameraOrientation === 'flipped' }" ref="video"></video>
         </v-flex>
         <v-flex xs2 text-center>
          <v-btn @click="toggleCamera"> 
            Flip
          </v-btn>
         </v-flex>
      </v-layout>
      <br>
    </div>
  </template>
  
  <script>
  // import WebSocket from 'ws';
  import axios from 'axios';
  export default{
    data() {
      return {
        cameraMode: "user",
        cameraOrientation: "normal",
        socket: null,
      };
    },
    mounted() {
      sendImage();
      this.startCamera();    
      // const ws = new WebSocket('ws://localhost:8000/');
      // ws.onopen = () => {
      //   const canvas = this.$refs.canvas;
      //   const ctx = canvas.getContext('2d');
      //   const img = new Image();
      //   img.onload = () => {
      //     canvas.width = img.width;
      //     canvas.height = img.height;
      //     ctx.drawImage(img, 0, 0, img.width, img.height);
      //     const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      //     const data = {
      //       type: 'mediapipe',
      //       imageData: imageData.data.buffer,
      //       width: imageData.width,
      //       height: imageData.height,
      //     };
      //     ws.send(JSON.stringify(data), [data.imageData]);
      //   };
      //   img.src = 'path/to/image.jpg';
      // };
    },
    methods:{
      startCamera() {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: this.cameraMode } })
          .then((stream) => {
            this.$refs.video.srcObject = stream;
            this.sm = stream;
            this.$refs.video.play();          
          })
          .catch((err) => {
            console.log("Error accessing the webcam:", err);
          });
      },
      toggleCamera() {
        if (this.cameraMode === "user") {
          this.cameraMode = { exact: "environment" };
          this.cameraOrientation = "flipped";
        } else {
          this.cameraMode = "user";
          this.cameraOrientation = "normal";
        }
        this.startCamera();
      },    
    }
  }
      async function sendImage() {
        try{
            const constraints = { video: true }
            const stream = await navigator.mediaDevices.getUserMedia(constraints)
            const video = document.querySelector('video')
            video.srcObject = stream
            const canvas = document.createElement('canvas')
            const context = canvas.getContext('2d')
            setInterval(() => {
              context.drawImage(video, 0, 0, canvas.width, canvas.height)
              canvas.toBlob(async (blob) => {
                const formData = new FormData()
                formData.append('image', blob, 'image.jpg')
                const response = await axios.post('/image', formData)
                console.log(response.data)
              }, 'image/jpeg', 0.7)
            }, 1000)
          }
          catch (error) {
            console.log(error);
            // Do something with error
            }     
      }
  
  </script>
  
  <style scoped>
  video {
    width: 100%;
    height: auto;
  }
  .flip-horizontal {
    transform: scaleX(-1);
  }
  </style>
  