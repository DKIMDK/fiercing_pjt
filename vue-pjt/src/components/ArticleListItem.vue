<template>
  <Transition>
    <div class="maintopsir" v-show="isVisible">
      <p class="article_title">{{ article.title }}</p>
    </div>
  </Transition>
</template>

<script setup>
import { ref } from 'vue'
const isVisible = ref(false)
const delay = 225 * index

setTimeout(() => {
  isVisible.value = true;
}, delay);


const { article, index } = defineProps({
  article: Object,
  index: Number
})
</script>

<style scoped>
.maintopsir {
  border: 3px solid pink;
  border-radius: 6px;
  width: 1000px;
  height: 130px;
  text-overflow: clip;
  margin-top: 20px;
  margin-bottom: 40px;
}

.article_title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 40px;
  text-align: center;
  line-height: 130px;
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
