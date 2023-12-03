<template>
    <transition>
        <div class="top" v-show="isVisible">
            <p class="exchange">환율 정보</p>
            <form class="bottom">
                <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="box-fix">
                        {{ coun1 }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" @click="setpk('coun1', 0, '1')">미국 달러</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun1', 1, '1')">유로</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun1', 2, '1')">위안화</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun1', 3, '1')">엔화</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun1', 4, '1')">원화</a></li>
                    </ul>
                </div>
                    <input type="number" v-model="much1" @input="exchangeCreate" id="leftdropdown">
                    
            </form>
            <div>
                <img src="@/assets/1194036.png" class="firstimg">
            </div>
            <form @submit.prevent = "exchangeCreate" class="bottom">
                <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="box-fix">
                        {{ coun2 }}
                    </button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" @click="setpk('coun2', 0, '2')">미국 달러</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun2', 1, '2')">유로</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun2', 2, '2')">위안화</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun2', 3, '2')">엔화</a></li>
                        <li><a class="dropdown-item" @click="setpk('coun2', 4, '2')">원화</a></li>
                    </ul>
                </div>
                <div id="upbox">
                    <p id="leftdropdown" style="padding:5px" v-if="result">{{ (result.price).toLocaleString() }}</p>
                </div>
            </form>
        </div>
    </transition>
    
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const isVisible = ref(false)
const pk1 = ref(null)
const pk2 = ref(null)
const much1 = ref(null)
const store = useCounterStore()
const result = ref(null)
const coun1 = ref('나라 선택')
const coun2 = ref('나라 선택')

setTimeout(() => {
    isVisible.value = true
}, 200)

const setpk = (counKey, value, pk) => {
    let coun_
    if (value === 0) coun_ = '미국 달러'
    else if (value === 1) coun_ = '유로'
    else if (value === 2) coun_ = '위안화'
    else if (value === 3) coun_ = '엔화'
    else if (value === 4) coun_ = '원화'

    if (counKey === 'coun1') {
        coun1.value = coun_
    } else if (counKey === 'coun2') {
        coun2.value = coun_
    }

    if (pk === '1') pk1.value = value
    else if (pk === '2') pk2.value = value
}

const exchangeCreate = function () {
    if (!pk1 || !pk2 || !much1){
        alert('입력값을 입력해주세요.')
    } else {
        axios ({
            method: 'post',
            url : `${store.API_URL}/api/v1/articles/exchange/${pk1.value}/${pk2.value}/${much1.value}/`,
        }).then((res) => {
            console.log(res)
            result.value = res.data
        }).catch((err) => {
            console.log(err)
        })
    }
}


</script>

<style scoped>
.exchange {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 60px;
    margin-bottom:100px
}

#primary {
    margin-top: 20px;
}

#box-fix {
    width:120px;
    box-sizing: border-box;
}

.top {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 150px;
}

.bottom, .firstimg {
    margin: 12px 0; /* 위 아래 각각 20px의 마진을 추가 */
}

.firstimg {
    width: 40px;
    height: 40px;
}

p {
    text-align: center;
}

.bottom {
    display : flex;
}

#leftdropdown {
    width:500px;
    text-align: right;
}

#upbox {
    border: 1px solid black;
    height: 37px;
    width: 500px
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