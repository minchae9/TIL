<template>
  <li @click="selectVideo">
    <img :src="youtubeImageSrc">
    {{ video.snippet.title | stringUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object, // 이런 방식도 가능
    },
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)  // '이 비디오를 골랐어' 신호와 함께 비디오 객체 전달
    },
  },
  computed: {
    youtubeImageSrc: function () {
      return this.video.snippet.thumbnails.default.url
    }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    },
  },
}
</script>

<style>

</style>