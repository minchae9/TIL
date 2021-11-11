<template>
  <div>
    <h1>Video List</h1>
    <ul>
      <VideoListItem
        v-for="(video, index) in videoList" :key="index"
        :video="video" 
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  computed: {
    videoList: function () {
      return this.$store.state.searchResult
    },
  },
}
</script>

<style>

</style>