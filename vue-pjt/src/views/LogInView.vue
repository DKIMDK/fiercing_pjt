<template>
<div class="toptoptoptop">
  <p class="log">로그인</p>
    <div class="gap-3">
      <input class="form-control me-auto man" type="userid" placeholder="아이디를 입력해주세요" aria-label="Add your item here..." v-model.trim="username">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="password" placeholder="비밀번호를 입력해주세요" aria-label="Add your item here..." v-model.trim="password" @keyup.enter="login">
    </div>
</div>

</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue'
const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const login = function () {
  const payload = {
    username : username.value,
    password : password.value
  }
  store.login(payload)
}

</script>

<style scoped>
.log {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
}
/* 전체 화면을 채우고 내용을 중앙에 배치 */
.toptoptoptop {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 80vh; /* 전체 뷰포트 높이를 사용 */
  width: 100vw; /* 전체 뷰포트 너비를 사용 */
}

.man {
  width: 300px;
  margin-top: 20px;
  padding: 8px;
}

input::placeholder { 
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
    text-align: center;
}
</style>
