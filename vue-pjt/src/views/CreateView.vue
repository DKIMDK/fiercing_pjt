<template>
    <div class="toptoptoptop">
      <p class="logincss">게시글 작성</p>
      <hr>
      <div class="gap-3">
        <input class="form-control me-auto mans" placeholder="제목" aria-label="Add your item here..." v-model.trim="title">
      </div>
      <div class="gap-3">
        <textarea class="form-control me-auto womans" placeholder="내용" aria-label="Add your item here..." v-model.trim="content">
        </textarea>
        </div>
        <button type="button" class="btn btn-primary createView" @click="createArticle">작성</button>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()

const createArticle = function () {
  axios ({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data : {
      title : title.value,
      content : content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((res) => {
      console.log(res)
      router.push({name:'ArticleView'})
    }).catch((err) => {
      console.log(err)
    })
}


</script>

<style>
.logincss {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  margin-right:720px;
}

.toptoptoptop {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 80vh; 
  width: 100vw;
}

.mans {
  font-family: 'Noto Sans KR', sans-serif;
  width: 1000px !important;
}

.womans{
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: bold;
  display: block;
  width: 1000px !important;
  height:300px;
  margin-top:20px
}

hr {
  width: 1000px !important;
}

.createView {
  margin-top: 5px;
  margin-left:940px;
}

</style>
