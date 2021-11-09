<template>
  <div>
    <input @keypress.enter="onInputKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInputKeyword: function (event) {
      // console.log(event.target.value)
      this.$emit('input-search', event.target.value)  // SearchBar -> App, payload에 event.target.value 실어 보내기
    },
  },
}
</script>

<style>

</style>