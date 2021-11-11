<template>
  <div>
    <li @click="selectVideo">
      <img :src="videoImg" alt="thumbnail image">
      <span>{{ videoTitle }}</span>
    </li>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    videoTitle: function () {
      return _.unescape(this.video.snippet.title)
    },
    videoImg: function () {
      return this.video.snippet.thumbnails.default.url
    },
  },
  methods: {
    selectVideo: function () {
      this.$store.dispatch('selectVideo', this.video)
    },
  },
}
</script>

<style>

</style>