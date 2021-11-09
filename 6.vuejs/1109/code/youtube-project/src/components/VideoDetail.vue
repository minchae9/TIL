<template>
  <div v-if="video">
    <iframe :src="videoURL" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: [String, Object], // 처음에 아무것도 안 고른 경우엔 빈 문자열이므로
    }
  },
  computed: {
    videoURL: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
}
</script>

<style>

</style>