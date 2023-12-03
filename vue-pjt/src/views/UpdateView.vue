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
      <button type="button" class="btn btn-primary createView" @click="updateArticle">작성</button>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useCounterStore()
const router = useRouter()
const route = useRoute()
onMounted(() => {
  fetchArticle()
  store.getUsername()
})

const fetchArticle = () => {
    axios ({
      method: 'get',
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
      
      headers: {
      Authorization: `Token ${store.token}`
    }
    })
    .then((res) => {
      title.value = res.data.title
      content.value = res.data.content
    })
    .catch((err) => {
      console.log(err)
    })
  }
  
const updateArticle = function () {
  axios ({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/update/`,
    data : {
      title : title.value,
      content : content.value,
      user : store.userId,
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((res) => {
      console.log(res)
      router.push({ name : 'DetailView', params: { id:route.params.id }})
    }).catch((err) => {
      console.log(err)
    })
}



</script>

<style>

</style>
