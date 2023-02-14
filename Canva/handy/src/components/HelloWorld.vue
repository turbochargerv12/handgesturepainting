<template>
  <div>
    <!-- SOURCE -->
    <div ref="printMe">
      <h1>Print me!</h1>
    </div>
    <!-- OUTPUT -->
    <img :src="output">
  </div>
</template>
 
<script>
export default {
  data() {
    return {
      output: null
    }
  },
  methods: {
    async print() {
      const el = this.$refs.printMe;
      // add option type to get the image version
      // if not provided the promise will return 
      // the canvas.
      const options = {
        type: 'dataURL'
      }
      this.output = await this.$html2canvas(el, options);
    }
  }
}
</script> 
