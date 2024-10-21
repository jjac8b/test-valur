<template>
  <div>
    <input v-model.number="num1" type="number" />
    <input v-model.number="num2" type="number" />
    <button @click="multiply">Multiply</button>
    <div v-if="loading"> Loading...</div>
    <div v-if="error"> {{error}}</div>
    <div v-if="result !==null ">Result: {{ result }}</div>
  </div>
</template>

<script>
import axios from 'axios';
import {ref} from 'vue';
export default{
    setup() {
    // State variables
    const num1 = ref(0);
    const num2 = ref(0);
    const result = ref(null);
    const loading = ref(false);
    const error = ref(null);

    // Function to call the API
    const multiply = async () => {
      try {
        loading.value = true;
        error.value = null;
        result.value = null;

        const response = await axios.get(`http://localhost:3000/multiply/`, {
          params: {
            num1: num1.value,
            num2: num2.value,
          },
        });
        result.value = response.data.result; 
        
      } catch (err) {
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
