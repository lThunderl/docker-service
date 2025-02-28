
<template>
  <div id="app">
    <h1>Данные из API</h1>
    <Services />
  </div>
</template>

<script>
import Services from './components/Services.vue';

export default {
  components: {
    Services,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between; 
  background-color: #35495e; /* темный цвет для навбара */
  padding: 10px 20px;
}

.logo {
  height: 50px; /* Настройте размер логотипа */
}

.nav-links {
  display: flex;
  gap: 20px; /* Промежуток между ссылками */
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-links a:hover {
  text-decoration: underline; /* Эффект наведения */
}
</style>
