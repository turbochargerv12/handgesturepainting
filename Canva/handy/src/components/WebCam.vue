<template>
  <video ref="video" autoplay></video>
</template>

<script>
export default {
  mounted() {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        const video = this.$refs.video;
        video.srcObject = stream;
        const socket = new WebSocket('ws://localhost:5000/video');
        const CHUNK_SIZE = 1024 * 1024; // 1MB
        let offset = 0;
        const sendChunk = () => {
          const stream = video.captureStream();
          const recorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
          
          recorder.ondataavailable = function (event) {
            socket.send(event.data);
          };

          recorder.start();

          setTimeout(() => {
            recorder.stop();
            if (offset < stream.size) {
              sendChunk();
            }
          }, 100);
          offset += CHUNK_SIZE;
        };
        sendChunk();
      });
  }
}
</script>
