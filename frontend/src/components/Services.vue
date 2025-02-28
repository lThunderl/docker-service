<template>
  <div>
    <p v-if="loading">Загрузка данных...</p>
    <p v-if="error">Ошибка: {{ error }}</p>
    <ul v-if="data">
      <li v-for="service in data">
        Service info: {{ service.id }} - {{ service.Service_Name }} 
      </li>
      
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: null,
      loading: false,
      error: null,
    };
  },
  async mounted() {
    this.loading = true;
    this.error = null;
    try {
      var response = await axios.get('http://127.0.0.1:8893/');
      this.data = response.data;
    } catch (err) {
      this.error = err.message;
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style>
.services-container {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.services-heading {
  font-size: 24px;
  font-weight: bold;
  color: #42b983;
  text-align: center;
  margin-bottom: 20px;
}

.services-list {
  list-style: none;
  padding: 0;
}

.service-link {
  display: block;
  padding: 10px 15px;
  background-color: #35495e; /* Цвет фона */
  color: white;
  text-decoration: none;
  border-radius: 5px; /* Уголки */
  margin: 5px 0; /* Отступы между элементами */
  transition: background-color 0.3s;
}

.service-link:hover {
  background-color: #42b983; /* Цвет на наведение */
}

.container-details {
  margin-top: 20px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9; /* Цвет фона формы */
}

.container-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 15px;
}

.form-container {
  display: flex;
  flex-direction: column;
}

.form-fields {
  margin-bottom: 15px;
}

.form-field {
  margin-bottom: 10px; /* Отступ между полями */
}

.input-field {
  width: 100%; /* Полная ширина */
  padding: 8px;
  border: 1px solid #ccc; /* Граница полей */
  border-radius: 4px; /* Углы */
  font-size: 14px;
}

.submit-button {

  padding: 10px;
  background-color: #42b983; /* Цвет кнопки */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #35495e; /* Цвет кнопки на наведение */
}
</style>
