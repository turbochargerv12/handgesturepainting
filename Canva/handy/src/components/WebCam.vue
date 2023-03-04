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
import WebSocket from 'ws';
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
    this.socket = new WebSocket('ws://localhost:8000');
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');

    const sendFrame = () => {
      context.drawImage(this.$refs.video, 0, 0, canvas.width, canvas.height);
      const imageData = canvas.toDataURL('image/jpeg', 0.5);
      this.socket.send(imageData);
      requestAnimationFrame(sendFrame);
    };
    requestAnimationFrame(sendFrame);
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
    }
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
