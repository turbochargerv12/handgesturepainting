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
// import axios from 'axios';
export default{
  data() {
    return {
      cameraMode: "user",
      cameraOrientation: "normal",
      socket: null,
    };
  },
  mounted() {
    // sendImage();
    this.startCamera();

    // Get the user's camera stream
    // navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
    //   // Attach the camera stream to the video element
    //   this.$refs.video.srcObject = stream;
    //   this.startCamera(); 
    //   // Connect to the WebSocket server
    //   const ws = new WebSocket("ws://localhost:5000/video");
    //   // Send each video frame to the WebSocket server
    //   const canvas = document.createElement("canvas");
    //   const ctx = canvas.getContext("2d");
    //   const sendFrame = () => {
    //     canvas.width = this.$refs.video.videoWidth;
    //     canvas.height = this.$refs.video.videoHeight;
    //     ctx.drawImage(this.$refs.video, 0, 0);
    //     const dataUrl = canvas.toDataURL("image/jpeg");
    //     ws.send(dataUrl);
    //     requestAnimationFrame(sendFrame);
    //   };
    //   requestAnimationFrame(sendFrame);
    


    // });

  },
  methods:{
    // isOpen(ws) { return ws.readyState === ws.OPEN;},
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
};    
// async function sendImage() {
    //   try{
    //       const constraints = { video: true }
    //       const stream = await navigator.mediaDevices.getUserMedia(constraints)
    //       const video = document.querySelector('video')
    //       video.srcObject = stream
    //       const canvas = document.createElement('canvas')
    //       const context = canvas.getContext('2d')
    //       setInterval(() => {
    //         context.drawImage(video, 0, 0, canvas.width, canvas.height)
    //         canvas.toBlob(async (blob) => {
    //           const formData = new FormData()
    //           formData.append('image', blob, 'image.jpg')
    //           const response = await axios.post('/image', formData)
    //           console.log(response.data)
    //         }, 'image/jpeg', 0.7)
    //       }, 1000)
    //     }
    //     catch (error) {
    //       console.log(error);
    //       // Do something with error
    //       }     
    // }

import io from 'socket.io-client';
const socket = io('http://localhost:5000/video_stream');

// Capture video from webcam
const videoElement = document.querySelector('video');
navigator.mediaDevices.getUserMedia({ video: true })
  .then((stream) => {
    videoElement.srcObject = stream;

    // Send video frames to FastAPI endpoint using WebSocket
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    setInterval(() => {
      canvas.width = videoElement.videoWidth;
      canvas.height = videoElement.videoHeight;
      context.drawImage(videoElement, 0, 0);
      const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
      socket.emit('video_frame', imageData);
    }, 1000/30);
  });


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
