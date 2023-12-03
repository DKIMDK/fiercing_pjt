<template>
  <div class="toptoptoptopin">
    <div class="profile_main">
      <p class="profile_profile">프로필</p>
      <div class="gap-3">
        <button type="button" class="btn btn-primary profile_update" @click="goUpdate">회원 정보 수정</button>
      </div>
    </div>
    <div>
      {{ store.SavingProfileData }}

    </div>
      id {{ store.username }}
      닉네임 {{ store.nickname }}
      내 연봉{{ store.salary }}
      내 자산{{ store.asset }}
      나이{{ store.age }}
    </div>
    <div>
      <h2>나에게 맞는 상품 찾기</h2>
    <div>
      <button @click="getDepositRecommendation">적금</button>
      <div v-if="store.rec_deposit">{{ store.rec_deposit }}</div>
      <button @click="getSavingRecommendation">예금</button>
      <div v-if="store.rec_saving"> {{  store.rec_saving }}</div>
      
    </div>
    </div>

</template>

<script setup>
import { useCounterStore } from "@/stores/counter"
import { onMounted, ref } from "vue"
import { useRouter } from "vue-router"

const store = useCounterStore();
const router = useRouter()

onMounted(() => {
  store.SavingProfile()
})


const goUpdate = function () {
  router.push({name : 'ProfileUpdateView'})
}
const getDepositRecommendation = function () {
  store.getDepositRecommendation()
  
}
const getSavingRecommendation = function () {
  store.getSavingRecommendation()
}

</script>

<style scoped>
.profile_update{
  margin-left: 500px;
  margin-top: 40px;
}
.profile_profile {
  font-size: 60px;
}

.toptoptoptopin {
  margin-top:60px;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 80vh; /* 전체 뷰포트 높이를 사용 */
  width: 100vw; /* 전체 뷰포트 너비를 사용 */
}

.profile_main {
  display: flex;
}

</style>
