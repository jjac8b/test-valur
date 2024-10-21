<template>
  <div class="multiplierbox">
    <input v-model.number="num1" type="number" />
    <input v-model.number="num2" type="number" />
    <button @click="multiply" :disabled="loading">Multiply</button>
    <div v-if="loading">Loading...</div>
    <div v-if="error">{{ error }}</div>
    <div v-if="result !== null">Result: {{ result }}</div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  setup() {
    const num1 = ref(0);
    const num2 = ref(0);
    const result = ref(null);
    const loading = ref(false);
    const error = ref(null);

    const multiply = async () => {
      loading.value = true;
      error.value = null;
      result.value = null;

      try {
        const { data } = await axios.get(`${process.env.VUE_APP_API_BASE_URL}/multiply/`, {
          params: { num1: num1.value, num2: num2.value },
        });
        result.value = data.result; 
      } catch {
        error.value = 'Failed to get the result. Please try again.';
      } finally {
        loading.value = false;
      }
    };

    return {
      num1,
      num2,
      result,
      loading,
      error,
      multiply,
    };
  },
};
</script>

<style scoped>
</style>
