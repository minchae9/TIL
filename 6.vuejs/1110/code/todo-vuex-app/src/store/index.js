import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todos: [],
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      // 1. indexOf (삭제 대상 찾기)
      const index = state.todos.indexOf(todoItem)
      // 2. splice (1개 항목 삭제하기)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          return {
            // JS spread syntax: 객체 복사
            ...todo,
            isCompleted: !todo.isCompleted,
          }
        } else {
          return todo
        }
      })
    },
  },
  actions: {
    createTodo: function ({ commit }, todoItem) {
      commit('CREATE_TODO', todoItem) // 첫 번째 인자로 context를 그대로 받으면 context.commit()
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodoStatus: function ({ commit }, todoItem) {
      commit ('UPDATE_TODO_STATUS', todoItem)
    },
  },
  getters: {
    completedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return !todo.isCompleted
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    },
  },
  modules: {
  }
})
