<template>
    <div>

    </div>
</template>

<script setup>
import axios from 'axios'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
store.logOut()

</script>

<style scoped>

</style>