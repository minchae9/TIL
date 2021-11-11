<template>
  <div>
    <h2>로또번호 추천</h2>
    <button @click="getLuckyNums">추천 번호 보기!</button>
    <p>로또 추천 번호 {{ $route.params.lottoNum }}개</p>
    <!-- <p>{{ $route.params }}</p> -->
    <ul>
      <li v-for="(num, index) in selectedLuckyNums" :key="index">{{ num }}</li>
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      selectedLuckyNums: [],
    }
  },
  methods: {
    getLuckyNums: function () {
      const numbers = _.range(1, 46)
      // this.sampleNums = _.sampleSize(numbers, 6)
      // this.selectedLuckyNums = _.sortBy(this.sampleNums)
      this.selectedLuckyNums = _.sampleSize(numbers, this.$route.params.lottoNum)
      this.selectedLuckyNums = _.sortBy(this.selectedLuckyNums)
    }
  }
}
</script>

<style>

</style>