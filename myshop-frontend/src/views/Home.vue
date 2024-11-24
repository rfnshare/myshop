<template>
  <div class="home-page">
    <header class="hero">
      <div class="hero-content">
        <h1>Welcome to iFutureBD</h1>
        <p>Your one-stop shop for the latest gadgets and tech.</p>
        <div class="actions">
          <router-link to="/register" class="btn btn-primary">Register</router-link>
          <router-link to="/login" class="btn btn-secondary">Login</router-link>
        </div>
      </div>
    </header>

    <!-- Featured Products Section -->
    <section class="featured-products">
      <h2>Featured Products</h2>
      <div class="product-grid">
        <div class="product-card" v-for="product in products" :key="product.id">
          <img :src="product.image" :alt="product.name" />
          <h3>{{ product.name }}</h3>
          <p>${{ product.price }}</p>
          <button class="btn btn-secondary">View Details</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      products: [
        { id: 1, name: "Smartphone", price: 699, image: "/images/smartphone.jpg" },
        { id: 2, name: "Laptop", price: 999, image: "/images/laptop.jpg" },
        { id: 3, name: "Headphones", price: 199, image: "/images/headphones.jpg" },
      ],
    };
  },
};
</script>

<style scoped>
/* General Page Layout */
.home-page {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  color: #fff;
}

/* Hero Section */
.hero {
  background: linear-gradient(to right, #e74c3c, #2c3e50);
  text-align: center;
  padding: 50px 20px;
  color: white;
}

.hero h1 {
  font-size: 3.5rem;
  margin-bottom: 10px;
}

.hero p {
  font-size: 1.5rem;
  margin-bottom: 20px;
}

.hero .btn {
  padding: 10px 20px;
  font-size: 1rem;
  background-color: white;
  color: #e74c3c;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.hero .btn:hover {
  background-color: #c0392b;
  color: white;
}

/* Featured Products Section */
.featured-products {
  padding: 20px;
  background: #333;
}

.featured-products h2 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 2rem;
  color: #e74c3c;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.product-card {
  background: #222;
  border: 1px solid #444;
  border-radius: 10px;
  padding: 15px;
  text-align: center;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.product-card img {
  max-width: 100%;
  border-radius: 10px;
}

.product-card h3 {
  font-size: 1.2rem;
  margin: 10px 0;
  color: #fff;
}

.product-card p {
  font-size: 1rem;
  color: #e74c3c;
}

.product-card .btn {
  padding: 5px 10px;
  font-size: 0.9rem;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.product-card .btn:hover {
  background-color: #c0392b;
}
</style>
