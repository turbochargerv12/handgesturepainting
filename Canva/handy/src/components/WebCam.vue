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
export default {
  data() {
    return {
      cameraMode: "user",
      cameraOrientation: "normal"
    };
  },
  mounted() {
    this.startCamera();
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
