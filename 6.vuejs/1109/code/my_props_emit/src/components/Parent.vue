<template>
  <div>
    <h1>AppParent</h1>
    <p>ParentData: {{ parentData }}</p>
    <input v-model="parentData" type="text" @input="inputParentData">
    <p>appData: {{ appData }}</p>
    <p>ChildData: {{ childData }}</p>
    <Child :appData="appData" :parentData="parentData"
      @child-input="inputChildData" />
  </div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent', // Vue Devtools로 볼 때 뜨는 이름
  data: function () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    inputChildData: function(data) {
      // console.log('text from child!')
      this.childData = data // Child -> Parent
      this.$emit('child-input', this.childData) // Child - Parent -> App
    },
    inputParentData: function () {
      this.$emit('parent-input', this.parentData) // Parent -> App
    },
  },
  components: {
    Child,
  },
  props: {
    appData: String,  // 이름과 자료형
  },
}
</script>

<style>

</style>