<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">{{ defaultSaving[0].kor_co_nm }}의 적금 목록입니다.</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div v-if="filterSaving.length > 0">
                    <div v-for="filter in filterSaving">
                        <ul class="list-group box">
                            <li class="list-group-item scopedSaving">
                                {{ filter.rsrv_type_nm }}
                                {{ filter.intr_rate_type_nm }}
                                {{ filter.intr_rate }}
                                {{ filter.intr_rate2 }}
                            </li>
                        </ul>
                    </div>
                    
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary" @click="savingconfirm">관심 목록 추가</button>
            </div>
            </div>
        </div>
    </div>
    
    <Transition>
        <div v-show="isVisible">
    <div class="toptop">
        <p class="islike">
            <button class="btn btn-outline-primary" v-if="isTrue" data-bs-toggle="modal" data-bs-target="#exampleModal">관심 목록 보기</button>
            <a class="btn btn-primary" v-else aria-current="page" @click="savingcancel" id="unliveToast" >관심 목록 해제</a>
            <div class="toast-container position-fixed bottom-0 end-0 p-3">
                <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                    <div class="toast-header">
                    <strong class="me-auto">알림</strong>
                    <small>just now</small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                    </div>
                    <div class="toast-body" v-if="isclicked">
                        관심 목록에 제거되었습니다.
                    </div>
                    <div class="toast-body" v-else>
                        관심 목록에 추가되었습니다.
                    </div>
                </div>
            </div>
            <RouterLink :to="{ name : 'Saving' }" style="margin-left:30px;line-height:35px">
            뒤로가기
            </RouterLink>
        </p>
    
        <table class="table">
        <thead>
            <tr>
                <td class="title">상품 이름</td>
                <td>{{ defaultSaving[0].fin_prdt_nm }}</td>
            </tr>
            <tr>
                <td class="title">회사 이름</td>
                <td>{{ defaultSaving[0].kor_co_nm }}</td>
            </tr>
            <tr>
                <td class="title">유의 사항</td>
                <td>{{ defaultSaving[0].etc_note }}</td>
            </tr>
            <tr>
                <td class="title">가입 방법</td>
                <td>{{ defaultSaving[0].join_way }}</td>
            </tr>
            <tr>
                <td class="title">만기 후 이자율</td>
                <td>{{ defaultSaving[0].mtrt_int }}</td>
            </tr>
            <tr>
                <td class="title">최고 한도</td>
                <td>{{ defaultSaving[0].max_limit }}</td>
            </tr>
            <tr>
                <td class="title">가입 제한</td>
                <td>{{ defaultSaving[0].join_deny }}</td>
            </tr>
            <tr>
                <td class="title">가입 대상</td>
                <td>{{ defaultSaving[0].join_member }}</td>
            </tr>
            <tr>
                <td class="title">우대 조건</td>
                <td>{{ defaultSaving[0].spcl_cnd }}</td>
            </tr>
        </thead>
        <tbody>
        </tbody>
      </table>

    </div>
    </div>
    </Transition>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { inject } from 'vue';
import { RouterLink, useRoute } from 'vue-router' 

const route = useRoute()
const isTrue = ref(true)
const store = useCounterStore()
const id = route.params.id
const isVisible = ref(false)
const Toast = inject('toast')
const isclicked = ref(true)

onMounted(() => {
    setTimeout(() => {
        isVisible.value = true
    }, 200)
})

const changefunction = function() {
    const toastLiveExample = document.getElementById('liveToast')
    if (isTrue.value === true) {
        const toastBootstrap = Toast.getOrCreateInstance(toastLiveExample)
        toastBootstrap.show()
    } else {
        const toastBootstrap = Toast.getOrCreateInstance(toastLiveExample)
        toastBootstrap.show()
    }
    isTrue.value = !isTrue.value
    isclicked.value = !isclicked.value
}

const savingconfirm = function() {
    changefunction()
    store.SavingData(id, 1)
}

const savingcancel = function() {
    changefunction()
    store.SavingData(id, 2)
}

const defaultSaving = computed(() => {
    return store.savings.filter(depo => depo.fin_prdt_cd.includes(id))
})

const filterSaving = computed(() => {
    return store.fullSavingOptions.filter(sav => sav.fin_prdt_cd.includes(id))
})

</script>

<style scoped>
.box {
    padding: 10px
}
.scopedSaving {
    border: 0.1px solid blue;
    font-family: 'Noto Sans KR', sans-serif;
}

.islike {
    display:flex;
    float:right;
}

.title {
    width: 200px;
    line-height:250%
}
.toptop {
    width:80%;
    margin: 0 auto;
    padding:25px;
}
.table {
    width:100%;
    margin: 0 auto;
}
/* 테이블 헤더 스타일 */.table th {
    font-family: 'Noto Sans KR', sans-serif;
  background-color: white;
  color: black;
  padding: 10px;
}

/* 테이블 셀 스타일 */
.table td {
font-family: 'Noto Sans KR', sans-serif;
  padding: 13px;
  text-align: center;
  border-bottom: 1px solid #ddd;
  font-size: 18px;
  background-color: white;
  font-weight: 600;
}

a {
  text-decoration: none;
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