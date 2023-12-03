import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const deposits = ref([])
  const depositsOption = ref([])
  const savings = ref([])
  const savingOptions = ref([])
  const username = ref(null)
  const userId = ref(null)
  const age = ref(null)
  const salary = ref(null)
  const nickname = ref(null)
  const asset = ref(null)
  const fullDepositOptions = ref([])
  const fullSavingOptions = ref([])
  const SavingProfileData = ref([])
  const DepositProfileData = ref([])
  const rec_deposit = ref([])
  const rec_saving = ref([])
  

  const SavingProfile = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v3/savingsend/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res) => {
      console.log(res)
      SavingProfileData.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }


  const SavingData = function(saving_pk, isTrue) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v3/${saving_pk}/databaseSaving/`,
      data: {
        'isTrue' : isTrue
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res) => {
      console.log(res)
    }).catch((err) => {
      console.log(err)
    })
  }

  const DepositData = function(deposit_pk, isTrue) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v3/${deposit_pk}/databaseDeposit/`,
      data: {
        'isTrue' : isTrue
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res)=>{
      console.log(res)
    }).catch((err) => {
      console.log(err)
    })
  }

  const fullDepositOption = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v2/ddd/`,
    }).then((res) => {
      fullDepositOptions.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const fullSavingOption = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v2/dddd/`,
    }).then((res) => {
      fullSavingOptions.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }
  
  const isLogin = computed(() => {
    if(token.value === null) {
      return false
    } else {
      return true
    }
  })

  const firstDeposits = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v2/database/`,
    }).then((res)=>{
      console.log(res)
    }).catch((err)=>{
      console.log(err)
    })
  }

  const firstSavings = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v2/savings/`,
    }).then((res)=>{
      console.log(res)
    }).catch((err)=>{
      console.log(err)
    })
  }
  
  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    }).then((res) => {
      articles.value = res.data
    }).catch((error) => {
      console.log(error)
    })
  }
  const getDepositRecommendation = function () {
    axios({
      method : 'post',
      url : `${API_URL}/api/v3/deposit/`,
      data: {
        'age': age.value,
        'asset': asset.value,
        'salary': salary.value,
      }
    })
    .then((res) => {
      console.log(res.data.recommended_deposit_products_info)
      rec_deposit.value = res.data.recommended_deposit_products_info
      alert('적금정보입니다.')
    })
    .catch((err) => {
      console.log(err)
    })
  }
  const getSavingRecommendation = function () {
    axios({
      method : 'post',
      url : `${API_URL}/api/v3/saving/`,
      data: {
        'age': age.value,
        'asset': asset.value,
        'salary': salary.value,
      }
    })
    .then((res) => {
      console.log(res.data.recommended_saving_products_info)
      rec_saving.value = res.data.recommended_saving_products_info
      alert('예금정보입니다.')
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const signUp = function (payload) {
    axios({
      method : 'post',
      url: `${API_URL}/accounts/signup/`,
      data : {
        'username': payload.username,
        'password1': payload.password1,
        'password2': payload.password2,
        'nickname': payload.nickname,
        'age': payload.age,
        'asset': payload.asset,
        'salary': payload.salary,
        'email': payload.email,
      }
    })
    .then((res) => {
      alert('회원 가입 성공')
      router.push({name : 'LogInView'})
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const login = function (payload) {
    // const { inputUsername, password } = payload
    // console.log(inputUsername, password)
    axios({
      method : 'post',
      url: `${API_URL}/accounts/login/`,
      data : {
        'username' : payload.username, 
        'password' : payload.password,
      }
    }).then((res) => {
      alert("로그인에 성공했습니다.")
      console.log(res.data.key)
      username.value = payload.username
      token.value = res.data.key
      router.push({name : 'ArticleView'})
      
    }).catch((err) => {
      alert("아이디 혹은 비밀번호를 확인해주세요")
      router.go({name : 'LogInView'})
    })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
    .then((res) => {
      username.value = null
      token.value = null
      alert('정상적으로 로그아웃되었습니다.')
      router.push({ name: 'LogInView' })
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const DepositSaving = function() {
    return axios({
      method : 'get',
      url: `${API_URL}/api/v2/dview/`,
    }).then((res) => {
      deposits.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const DepositOptions = function() {
    return axios({
      method : 'get',
      url: `${API_URL}/api/v2/doview/`,
    }).then((res) => {
      depositsOption.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const Saving = function() {
    return axios({
      method : 'get',
      url: `${API_URL}/api/v2/sview/`,
    }).then((res) => {
      savings.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const SavingOption = function() {
    return axios({
      method : 'get',
      url: `${API_URL}/api/v2/soview/`,
    }).then((res) => {
      savingOptions.value = res.data
    }).catch((err) => {
      console.log(err)
    })
  }

  const getUsername = function() {
    axios({
      method: "get",
      url: `${API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then((res) => {
        console.log(res)
        username.value = res.data.username;
        userId.value = res.data.pk;
        salary.value = res.data.salary
        asset.value = res.data.asset
        age.value = res.data.age
        nickname.value = res.data.nickname
      })
      .catch((err) => {
        console.log(err);
      });
  }

  const editInfo = function (payload) {
    const { nickname, age, asset, salary, } = payload
    axios({
      method: 'patch',
      url: `${API_URL}/profile/update/user/`,
      data: {
        nickname, age, asset, salary,
      },
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
    .then((res) => {
      console.log(res)
      alert('회원 정보가 수정되었습니다.')
      router.push( { name : 'Profile' })
      getUsername()
    })
    .catch((err) => {
      console.log(err)
    })
  } 
  const islike = function(product_id) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v3/${product_id}/islike/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    }).then((res) => {
      console.log(res)
    }).catch((err) => {
      console.log(err)
    })
  }

  return {getDepositRecommendation, rec_deposit, getSavingRecommendation, rec_saving, DepositData, DepositProfileData, SavingProfileData, SavingProfile, SavingData, fullSavingOption, fullDepositOption, fullSavingOptions, fullDepositOptions, islike, firstDeposits, firstSavings, getUsername, Saving, SavingOption, savings, savingOptions, articles, API_URL, getArticles, signUp, login, token, isLogin, DepositSaving, deposits, DepositOptions, depositsOption, logOut, userId, username, asset, salary, age, nickname, editInfo }
}, { persist: true })
