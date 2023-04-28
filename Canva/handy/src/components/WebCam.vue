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
          const blob = video.captureStream().getVideoTracks()[0].stop();
          const chunk = blob.prototype.slice(offset, offset + CHUNK_SIZE);
          socket.send(chunk);
          offset += CHUNK_SIZE;
          if (offset < blob.size) {
            setTimeout(sendChunk, 100);
          }
        };
        sendChunk();
      });
  }
}
</script>