<template>
    <div v-if="store.articles.length === 0">
      <div class="articleView_top">
        <p class="noop">첫 게시글을 작성해보세요</p>
        <RouterLink :to="{ name: 'CreateView' }">
          <button type="button" class="btn btn-primary articleviewbutton">게시글 작성</button>
        </RouterLink>
      </div>
    </div>
    <div v-else>
      <div class="toptop">
      <div class="article_bottom">
        <p class="logincss noop">게시글</p>
        <RouterLink :to="{ name: 'CreateView' }">
          <button type="button" class="btn btn-primary articleviewbutton">게시글 작성</button>
        </RouterLink>
      </div>
      <hr>
        <ArticleList 
        />
      </div>
    </div>
</template>

<script setup>
// 최상단 훅인 ArticleView.vue에 mounted 시켜야 한다.
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'


const store = useCounterStore()
const isVisible = ref(false)

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>
.articleView_top {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 25px;
  align-items: center;
  height: 80vh; /* 전체 뷰포트 높이를 사용 */
  width: 100vw; /* 전체 뷰포트 너비를 사용 */
}
.toptop {
  display: flex;
  flex-direction: column;
  margin-top: 25px;
  align-items: center;
  height: 80vh; /* 전체 뷰포트 높이를 사용 */
  width: 100vw; /* 전체 뷰포트 너비를 사용 */
}
.noop {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px !important;
}

.articleviewbutton {
  margin-top:40px;
}


.article_bottom {
  display:flex;
}
</style>
