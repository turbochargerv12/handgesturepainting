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
export default {
  data() {
    return {
      cameraMode: "user",
      cameraOrientation: "normal",
      socket: null,
    };
  },
  mounted() {
    this.startCamera();
    // this.socket = new WebSocket('ws://localhost:5000/');
    // const canvas = document.createElement('canvas');
    // const context = canvas.getContext('2d');
    
    // this.submitForm();
    // const sendFrame = () => {
    //   context.drawImage(this.$refs.video, 0, 0, canvas.width, canvas.height);
    //   const imageData = canvas.toDataURL('image/jpeg', 0.5);
    //   this.socket.send(imageData);
    //   requestAnimationFrame(sendFrame);
    // };
    // requestAnimationFrame(sendFrame);
    // https://a2i2.deakin.edu.au/2020/04/23/real-time-data-transfer-using-vue-and-socket-io-part-1-of-3/
    // navigator.mediaDevices.getUserMedia({ video: true })
    //   .then((stream) => {
    //     this.$refs.video.srcObject = stream;
    //     this.$refs.video.play();
    //   })
    //   .catch((err) => {
    //     console.log("Error accessing the webcam:", err);
    //   });
  },
  methods:{
    startCamera() {
      navigator.mediaDevices.getUserMedia({ video: { facingMode: this.cameraMode } })
        .then((stream) => {
          this.$refs.video.srcObject = stream;
          this.sm = stream;
          this.$refs.video.play();
          this.submitForm(this.$refs.video.play())
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
    submitForm(hello) {
      axios.post('http://localhost:5000/media', {
        name: hello, 
      })
        .then((response) => {
          if (response.data.status == true) {
            console.log('Data sent successfully!');
          }
        })
        .catch((error) => {
          console.log('Error sending data:', error);
        });
    },
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
