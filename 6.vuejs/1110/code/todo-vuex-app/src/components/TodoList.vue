<template>
  <div>
    <todo-list-item
      v-for="todo in todos"
      :key="todo.date"
      :todo="todo"
    >

    </todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
import { mapState } from 'vuex' // vuex 전체 구조 중 mapState만 (구조 분해 할당)

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // 1.
  // computed: {
  //   todos: function () {
  //     return this.$store.state.todos
  //   },
  // },

  // 2.
  // computed: mapState([
  //   'todos',
  // ]),

  // 3.
  computed: {       // spread syntax로 객체를 복사해와서 사용함으로써, 다른 헬퍼도 사용가능.
    ...mapState([
      'todos',
    ]),
  },
}
</script>

<style>

</style>