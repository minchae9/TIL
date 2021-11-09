<template>
  <div>
    <h1>AppChild</h1>
    <p>ChildData: {{ childData }}</p>
    <input v-model="childData" type="text" @input="inputChildData">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: String,
    parentData: String,
  },
  data: function () {
    return {
      childData: '',
    }
  },
  methods: {
    inputChildData: function () {
      this.$emit('child-input', this.childData) // 'child-input'라는 이름의 이벤트(신호)를 발생시킨다.
    }   // 두 번째 인자는 payload에 넣는 것
  },
}
</script>

<style>

</style>