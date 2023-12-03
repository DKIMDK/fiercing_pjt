<template>
  <div class="toptoptoptop">
  <p class="log">회원 가입</p>
    <div class="gap-3">
      <input class="form-control me-auto man" type="userid" placeholder="아이디 입력" aria-label="Add your item here..." v-model.trim="username">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="password" placeholder="비밀번호를 입력해주세요" aria-label="Add your item here..." v-model.trim="password1">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="password" placeholder="비밀번호를 확인해주세요" aria-label="Add your item here..." v-model.trim="password2">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="text" placeholder="닉네임을 입력해주세요" aria-label="Add your item here..." v-model.trim="nickname">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="number" placeholder="나이 입력" aria-label="Add your item here..." v-model.trim="age">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="number" placeholder="현재 자산 입력" aria-label="Add your item here..." v-model.trim="asset">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="number" placeholder="연봉 입력" aria-label="Add your item here..." v-model.trim="salary">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto man" type="text" placeholder="이메일 입력" aria-label="Add your item here..." v-model.trim="email" @keyup.enter="signUp">
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null);
const age = ref(null);
const asset = ref(null);
const salary = ref(null);
const email = ref(null);

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    age: age.value,
    asset: asset.value,
    salary: salary.value,
    email: email.value,
  }
  store.signUp(payload)
  console.log(payload)
}

</script>

<style>
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
