<template>
  <div>
    <!-- 하위 컴포넌트 -->
    <ArticleListItem
      v-for="(article, index) in store.articles"
        :key="article.id"
        :article="article"
        :index="index"
        @click="godetail(article.id)"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import ArticleListItem from '@/components/ArticleListItem.vue'
import { useRouter } from 'vue-router';

const store = useCounterStore()
const router = useRouter()
const godetail = function(id) {
  router.push({ name : 'DetailView', params: { id:id }})
}

</script>
