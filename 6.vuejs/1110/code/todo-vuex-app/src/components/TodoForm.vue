<template>
  <div>
    <input @keyup.enter="createTodo" v-model.trim="todoTitle" type="text">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      if (todoItem.title) { // 빈값 입력 방지
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = null
    },
  },
}
</script>

<style>

</style>