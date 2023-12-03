<template>
  <div>
    <div class="toptoptoptop">
      <div class="shutdown">
        <p class="logincss">자세히 보기</p>
        <button type="button" class="btn btn-outline-primary detailbutton" @click="backbutton">뒤로가기</button>
      </div>
      <hr>
      <div v-if="article">
        <div class="column">
          <p class="columntarget">제목  </p>
          <p>{{ article.title }}</p>
        </div> 
        <div class="columncontent">
          <p class="columntarget">내용 </p>
          <p class="contentvalue">{{ article.content }}</p>
        </div>
        <div class="column">
          <p class="columntarget">작성 날짜  </p>
          <p>{{ article.created_at }}</p>
        </div>
        <div class="column">
          <p class="columntarget">수정 날짜  </p>
          <p>{{ article.updated_at }}</p>
        </div>
        <div class="bottom">
          <RouterLink :to="{ name: 'UpdateView' }">
            <button type="button" class="btn btn-primary" style="margin-right:10px;">수정</button>
          </RouterLink>
          <button type="button" class="btn btn-danger" @click="deleteArticle(route.params.id)">삭제</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

onMounted(() => {
  store.getUsername()
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  }).then((res) => {
  console.log(res.data.user)
  article.value = res.data
}).catch((error) => {
  console.log(error)
})

})

const backbutton = function() {
  router.push({ name: 'ArticleView' })
}

function deleteArticle() {
  axios ({
    method: 'delete',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/delete/`,
    data: {
      user: store.userId
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then((res) => {
    router.push({ name: 'ArticleView' })
  })
  .catch((err) => {
    console.log(err)
  })
}
</script>

<style scoped>
.detailbutton {
  width: 100px;
  height:40px;
  margin-top: 50px;
}
.shutdown {
  display: flex;
}
.contentvalue{
  width:930px;
  overflow-wrap: break-word;
}
.columntarget {
  font-size: 30px;
  margin-right: 20px;
}
.column {
  display:flex;
  line-height:25px;
  margin-bottom:10px;
  margin-right:650px;
}
.columncontent{
  display:flex;
  margin-bottom:20px;
}

.bottom {
  display:flex;
  margin-left: 850px;
}

p {
  font-family: 'Noto Sans KR', sans-serif;
}

</style>
