<template>
    <div class="toptoptoptop">
  <p class="log">회원정보수정</p>
    <div class="gap-3">
      <input class="form-control me-auto updateman" type="userid" placeholder="닉네임 변경" aria-label="Add your item here..." v-model.trim="nickname" @keyup.enter="editInfo">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto updateman" type="number" placeholder="나이 변경" aria-label="Add your item here..." v-model.trim="age" @keyup.enter="editInfo">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto updateman" type="number" placeholder="자산 변경" aria-label="Add your item here..." v-model.trim="asset" @keyup.enter="editInfo">
    </div>
    <div class="gap-3">
      <input class="form-control me-auto updateman" type="number" placeholder="연봉 변경" aria-label="Add your item here..." v-model.trim="salary" @keyup.enter="editInfo">
    </div>
</div>
  
</template>

<script setup>
  import { useCounterStore } from "@/stores/counter"
  import { onMounted, ref } from "vue"
  import { useRouter } from "vue-router"
  const age = ref(null)
  const asset = ref(null)
  const salary = ref(null)
  const nickname = ref(null)
  const store = useCounterStore();
  const editInfo = function () {
  const payload = {
    nickname: nickname.value || store.nickname,
    age: age.value || store.age,
    asset: asset.value || store.asset,
    salary: salary.value || store.salary,
  }
  store.editInfo(payload)
}
  </script>

<style scoped>
  .log {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
}

.updateman {
  width: 300px;
  margin-top: 20px;
  padding: 8px;
}

</style>