<template>
  <Transition>
    <div v-show="isVisible">
    <div class = "topcontainer">
        <div class="tab">
            <RouterLink :to="{ name : 'Deposit' }" class="notsubbox">
            예금
            </RouterLink> <p style="filter: invert(100%);"> | </p>
            <RouterLink :to="{ name : 'Saving' }" class="subbox">
            적금
            </RouterLink>
        </div>
        <div class="gap-3">
          <input class="form-control me-auto depositman" type="text" placeholder="검색" aria-label="Add your item here..." v-model.trim="inputText">
        </div>
    </div>
    <div class="container">
      <div v-if="filteredSavings.length > 0">
        <table class="table">
        <thead>
          <tr>
            <th>공시 날짜</th>
            <th>회사 이름</th>
            <th>상품 이름</th>
            <th @click="six">6개월</th>
            <th @click="tweleve">12개월</th>
            <th @click="twentyfour">24개월</th>
            <th @click="thirtysix">36개월</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(saving, index) in filteredSavings" @click="clickfunction(saving.fin_prdt_cd)">
              <td>{{ currentTime }}</td>
              <td>{{ saving.kor_co_nm }}</td>
              <td>{{ saving.fin_prdt_nm }}</td>
              <td>{{ store.savingOptions[index].save_trm6 }}</td>
              <td>{{ store.savingOptions[index].save_trm12 }}</td>
              <td>{{ store.savingOptions[index].save_trm24 }}</td>
              <td>{{ store.savingOptions[index].save_trm36 }}</td>
            </tr>
          </tbody>
      </table>
      </div>
      <div v-else>
        <table class="table">
        <thead>
          <tr>
            <th>공시 날짜</th>
            <th>회사 이름</th>
            <th>상품 이름</th>
            <th @click="six">6개월</th>
            <th @click="tweleve">12개월</th>
            <th @click="twentyfour">24개월</th>
            <th @click="thirtysix">36개월</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(saving, index) in store.savingOptions" @click="clickfunction(saving.fin_prdt_cd)">
              <td>{{ currentTime }}</td>
              <td>{{ saving.kor_co_nm }}</td>
              <td>{{ saving.fin_prdt_nm }}</td>
              <td>{{ store.savingOptions[index].save_trm6 }}</td>
              <td>{{ store.savingOptions[index].save_trm12 }}</td>
              <td>{{ store.savingOptions[index].save_trm24 }}</td>
              <td>{{ store.savingOptions[index].save_trm36 }}</td>
            </tr>
          </tbody>
      </table>
      </div>
    </div>
      </div>
    </Transition>
  </template>

<script setup>
import dayjs from "dayjs";
import { ref,  computed, Fragment } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from "vue-router";
import { useRouter } from "vue-router";

const isVisible = ref(false)
const currentTime = ref(dayjs().format('YYYYMMDD'))
const inputText = ref(null)
const store = useCounterStore()
const router = useRouter()
const sixTrue = ref(true)
const tweTrue = ref(true)
const fouTrue = ref(true)
const thrTrue = ref(true)

const clickfunction = function (key) {
  router.push({name:'DetailSavingView', params:{id:key}})
}

const filteredSavings = computed(() => {
  return store.savingOptions.filter(opt => opt.kor_co_nm.includes(inputText.value))
})

const six = function() {
  if (sixTrue.value) {
    sixTrue.value = !sixTrue.value
    store.savingOptions.sort(function(a,b){
      return b.save_trm6 - a.save_trm6
  })} else if (!sixTrue.value) {
    sixTrue.value = !sixTrue.value
    store.savingOptions.sort(function(a,b){
      return a.save_trm6 - b.save_trm6
    })
}}

const filteredsix = function() {
  if (sixTrue.value) {
    sixTrue.value = !sixTrue.value
    sortedDeposits.sort(function(a,b){
      return b.save_trm6 - a.save_trm6
  })} else if (!sixTrue.value) {
    sixTrue.value = !sixTrue.value
    sortedDeposits.sort(function(a,b){
      return a.save_trm6 - b.save_trm6
    })
}}

const tweleve = function() {
  if (tweTrue.value) {
    tweTrue.value = !tweTrue.value
    store.savingOptions.sort(function(a,b){
      return b.save_trm12 - a.save_trm12
  })} else if (!tweTrue.value) {
    tweTrue.value = !tweTrue.value
    store.savingOptions.sort(function(a,b){
      return a.save_trm12 - b.save_trm12
    })
}}

const filteredtweleve = function() {
  if (tweTrue.value) {
    tweTrue.value = !tweTrue.value
    filteredDeposits.sort(function(a,b){
      return b.save_trm12 - a.save_trm12
  })} else if (!tweTrue.value) {
    tweTrue.value = !tweTrue.value
    filteredDeposits.sort(function(a,b){
      return a.save_trm12 - b.save_trm12
    })
}}

const twentyfour = function() {
  if (fouTrue.value) {
    fouTrue.value = !fouTrue.value
    store.savingOptions.sort(function(a,b){
      return b.save_trm24 - a.save_trm24
  })} else if (!fouTrue.value) {
    fouTrue.value = !fouTrue.value
    store.savingOptions.sort(function(a,b){
      return a.save_trm24 - b.save_trm24
    })
}}

const filteredtwenty = function() {
  if (fouTrue.value) {
    fouTrue.value = !fouTrue.value
    filteredDeposits.sort(function(a,b){
      return b.save_trm24 - a.save_trm24
  })} else if (!fouTrue.value) {
    fouTrue.value = !fouTrue.value
    filteredDeposits.sort(function(a,b){
      return a.save_trm24 - b.save_trm24
    })
}}

const thirtysix = function() {
  if (thrTrue.value) {
    thrTrue.value = !thrTrue.value
    store.savingOptions.sort(function(a,b){
      return b.save_trm36 - a.save_trm36
  })} else if (!thrTrue.value) {
    thrTrue.value = !thrTrue.value
    store.savingOptions.sort(function(a,b){
      return a.save_trm36 - b.save_trm36
    })
}}

const filteredthritysix = function() {
  if (thrTrue.value) {
    thrTrue.value = !thrTrue.value
    filteredDeposits.sort(function(a,b){
      return b.save_trm36 - a.save_trm36
  })} else if (!thrTrue.value) {
    thrTrue.value = !thrTrue.value
    filteredDeposits.sort(function(a,b){
      return a.save_trm36 - b.save_trm36
    })
}}


// store.savings.forEach((dep) => {
//   const finPrdtCd = dep.fin_prdt_cd
//   if (!maingrouping[finPrdtCd]) {
//     maingrouping[finPrdtCd] = []
//   }
//   maingrouping[finPrdtCd] = store.savingOptions.filter(saving => saving.fin_prdt_cd === finPrdtCd)
// })


// const groupSavings = computed(() => {
//   const grouped = {}
//   store.savings.forEach((deposit) => {
//       const finPrdtCd = deposit.fin_prdt_cd
//       if (!grouped[finPrdtCd]) {
//           grouped[finPrdtCd] = [];
//       }
//       store.savingOptions.forEach((opt) => {
//           if (opt.fin_prdt_cd === finPrdtCd) {
//             grouped[finPrdtCd].push(opt['intr_rate'])
//           }
//       })
//   })
//   return grouped
// })

setTimeout(() => {
    isVisible.value = true
}, 200)

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');
/* 전체 레이아웃에 대한 스타일 */

.depositman{
  margin-top: 13px;
}
.topcontainer {
    width:70%;
    margin: 0 auto;
    display: flex;
}

input {
  width: 200px;
  height: 35px;
}
.tab {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 10px 20px;
  flex:1;
}
.input-container {
  display: flex;
  justify-content: flex-end; /* input을 오른쪽에 배치 */
  flex: 1; /* 나머지 공간을 차지하도록 flex-grow 설정 */
  align-items: center; /* 세로축 중앙 정렬 */
}
.subbox {
  border:1px solid rgba(0,0,0,0.8);
  border-radius: 5px;
  width:50px;
  height:35px;
  background-color:black;
  text-align: center;
  line-height: 35px;
  color:white;
}

.notsubbox {
border:1px solid rgba(0,0,0,0.8);
  border-radius: 5px;
  width:50px;
  height:35px;
  background-color:white;
  text-align: center;
  line-height: 35px;
}
.container {
  width: 80%;
  margin: 0 auto; /* 가운데 정렬 */
  background-color: white;
  font-size: 20px;
  border:none;
}

/* 탭 / 버튼 활성화 상태 */
.tab.active {
  background-color: blue;
  color: white;
}

/* 테이블 스타일 */
.table {
  width: 100%;
  border-collapse: collapse;
}

/* 테이블 헤더 스타일 */
.table th {
    font-family: 'Noto Sans KR', sans-serif;
  background-color: white;
  color: black;
  padding: 15px;
  text-align: center;
}

/* 테이블 셀 스타일 */
.table td {
font-family: 'Noto Sans KR', sans-serif;
  padding: 10px;
  text-align: center;
  border-bottom: 1px solid #ddd;
  font-size: 20px;
  background-color: white;
}

a {
  text-decoration: none;
}


.tab p {
  display: inline-block; /* 인라인 블록 요소로 변경 */
  margin: 0 10px; /* 좌우 여백 추가 */
  color: #ccc; /* 색상 변경 */
}

.v-enter-from{
    opacity: 0;
    transform: translateY(10px);
    
}

.v-leave-to {
    opacity: 0;
    transform: translateY(10px);
    
}

.v-enter-active, .v-leave-active {
    transition: opacity 1.2s ease;
}

</style>