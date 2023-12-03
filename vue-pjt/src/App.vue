<template>
  <header class="container">
    <nav>
      <RouterLink :to="{ name : 'ArticleView' }" class="nav"> 
        게시판
      </RouterLink> <p style="filter: invert(100%);"> | </p>

      <RouterLink :to="{name : 'Maps'}" class="nav">
        카카오맵
      </RouterLink> <p style="filter: invert(100%);"> | </p>

      <RouterLink :to="{name : 'Exchange'}" class="nav">
        환율 정보
      </RouterLink> <p style="filter: invert(100%);"> | </p>

      <RouterLink :to="{name : 'Deposit'}" class="nav">
        예금/적금 조회
      </RouterLink>


    </nav>
    <div class="rightsir">
      <div v-if="!store.isLogin">
        <RouterLink :to="{ name : 'SignUpView' }" class="nav-dropdown signup">
        회원가입
      </RouterLink>
      <RouterLink :to="{ name : 'LogInView' }" class="nav-dropdown">
        로그인
      </RouterLink>
      </div>
      <p class="helloworld" style="margin-right: 7px;">{{ store.isLogin ? `Hi, ${store.nickname}` : '' }}</p>
      <li class="menu-item" v-if="store.isLogin">
        <a class="menu-name" href="#">
          <img src="@/assets/profile.png" alt="">
        </a>
        <ul class="dropdown">
            <li><a class="menu-name" href="#">
              <RouterLink :to="{ name : 'Profile' }" class="nav-dropdown">
                Profile
              </RouterLink>
            </a></li>
            <li><a class="menu-name" href="#">
              <RouterLink :to="{ name : 'LogOut' }" class="nav-dropdown">
                로그아웃
              </RouterLink>
            </a></li>
        </ul>
      </li>
    </div>
  </header>
  <RouterView />
</template>

<script setup>

import { RouterView, RouterLink } from "vue-router"
import { useCounterStore } from "@/stores/counter"
import { onMounted, ref } from "vue"

const store = useCounterStore()
onMounted(() => {
  store.getUsername()
  store.DepositSaving()
  store.DepositOptions()
  store.Saving()
  store.SavingOption()
  store.fullDepositOption()
  store.fullSavingOption()
})


</script>

<style scoped>

.helloworld {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
  font-size : 16px;
  margin-top:12px;
  color:white;
}

a {
  text-decoration: none;
}

nav {
  flex-grow: 1; /* 가능한 모든 공간을 차지 */
  display: flex;
  justify-content: center; /* 자식 요소들을 중앙에 정렬 */
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
  margin-left:120px;
  margin-top: 10px;
}

.rightsir {
  margin-left: auto; /* 자동으로 오른쪽 정렬 */
  display: flex; /* flexbox 사용 */
  align-items: center; /* 수직 중앙 정렬 */
  margin-right:20px;
}


.nav {
  margin-right: 25px;
  margin-left: 25px;
  color:rgba(255,255,255,0.8);
  font-size: 22px;
}
.nav-dropdown {
  color: white;
  font-size: 15px;
  font-weight: bold;
}

.container {
  display: flex;
  justify-content: center; /* 가로축 중앙 정렬 */
  align-items: center; /* 세로축 중앙 정렬 */
  border: 1px solid black;
  background-color: rgba(0,0,0,0.9);
  font-size: 20px;
  padding: 5px;
  line-height: 50px;
}

img {
  width: 40px;
  height: 40px;
  background-color: white;
  filter: invert(100%);
}


/* 여기서부터 드롭다운 */
#menu{
    margin-top: 10vh;
    border-radius: var(--border-rad);
    
}
.menu-item {
    display: inline-block;
    position: relative;
    margin-left:5px;
}
.dropdown {
  background-color: white;
  display: none;
  position: absolute;
  top: 100%; /* 변경: 부모 요소의 높이에 기반하여 위치를 설정 */
  left: 50%; /* 중앙에 위치하도록 left를 50%로 설정 */
  transform: translateX(-50%); /* 중앙에 오도록 X축 기준으로 왼쪽으로 50% 이동 */
  white-space: nowrap; /* 드롭다운 항목이 여러 줄로 나누어지지 않도록 설정 */
  list-style: none;
  padding: 0; /* 패딩 초기화 */
  margin: 0; /* 마진 초기화 */
  text-align: center; /* 중앙 정렬 */
  border-radius: 0 0 let(--border-rad) let(--border-rad);
}
.dropdown-item {
    position: relative;
}

.menu-item:hover>.dropdown{
    display: block;
}
.dropdown-item:hover>.second {
    background-color: rgb(233, 233, 233);
    display: block;
    position: absolute;
    left : var(--menu-width);
    top : 0;
    border-radius: 0 var(--border-rad) var(--border-rad) var(--border-rad);

}
.menu-name {
  display: block; /* 블록 요소로 설정 */
  color: rgb(61, 61, 61);
  padding: 4px 8px; /* 드롭다운 항목의 패딩을 설정하여 너비를 조절 */
  text-decoration: none;
  background-color: black;
}

.signup {
  margin-right:20px
}

</style>
