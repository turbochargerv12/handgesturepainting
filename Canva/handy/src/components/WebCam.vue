<template>
  <video ref="video" autoplay></video>
</template>

<script>
import flvjs from 'flv.js';

export default {
  mounted() {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        const video = this.$refs.video;
        video.srcObject = stream;
        const flvPlayer = flvjs.createPlayer({
          type: 'flv',
          isLive: true,
          url: 'rtmp://your-streaming-server:1935/live/stream-name',
        });
        flvPlayer.attachMediaElement(video);
        flvPlayer.load();
        flvPlayer.play();
      });
  }
}
</script>
