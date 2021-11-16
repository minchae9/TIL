<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password"
      @keypress.enter="login(credentials)">
    </div>
    <button @click="login(credentials)">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login: function (credentials) {
      console.log(credentials)
      // axios 요청 보내기
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          //console.log(res)
          // 토큰을 로컬 저장소에 저장하기
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login') // App.vue에 로그인됐음을 알림
          this.$router.push({ name: 'TodoList' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>