<template>
  <!-- Bootstrap CSS -->
  <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    rel="stylesheet"
  />

  <div class="home-page">
    <!-- Header Section -->
    <header class="navbar navbar-expand-lg navbar-dark bg-dark py-3">
      <div class="container">
        <a class="navbar-brand fw-bold text-danger" href="#">
          <img src="../assets/logo.jpg" alt="iFutureBD" class="brand-logo" />
          iFutureBD
        </a>
        <form class="d-flex mx-auto w-50">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search for products, categories..."
            aria-label="Search"
          />
          <button class="btn btn-danger" type="submit">Search</button>
        </form>
        <div class="d-flex">
          <a href="/cart" class="btn btn-outline-danger">
            <i class="bi bi-cart"></i> Cart
          </a>
        </div>
      </div>
    </header>

    <!-- Main Banner -->
    <section class="main-banner bg-danger text-white py-5">
      <div class="container text-center">
        <h1>Welcome to iFutureBD</h1>
        <p class="lead">Your one-stop shop for the latest gadgets and tech</p>
        <a href="/products" class="btn btn-light btn-lg">Shop Now</a>
        <div class="mt-3">
          <a href="/register" class="btn btn-outline-light me-2">Register</a>
          <a href="/login" class="btn btn-outline-light">Login</a>
        </div>
      </div>
    </section>

    <!-- Category Highlights -->
    <section class="category-highlights py-5">
      <div class="container">
        <h2 class="text-center mb-4 text-danger">Explore Our Categories</h2>
        <div class="row">
          <div
            class="col-md-4"
            v-for="category in categories"
            :key="category.id"
          >
            <div class="card shadow-sm">
              <img
                :src="getCategoryImage(category)"
                alt="Category Image"
                class="card-img-top"
              />
              <div class="card-body">
                <h5 class="card-title text-danger">{{ category.name }}</h5>
                <p class="card-text">
                  Explore the best products in {{ category.name }}.
                </p>
                <button
                  class="btn btn-danger"
                  @click="toggleCategory(category.id)"
                >
                  View Products
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Hierarchical Display -->
    <section class="product-list py-5 bg-light" v-if="activeCategory">
      <div class="container">
        <h2 class="text-center mb-4 text-danger">
          Products in {{ getCategoryName(activeCategory) }}
        </h2>
        <div class="accordion" id="subcategoryAccordion">
          <div
            class="accordion-item"
            v-for="subCategory in activeSubCategories"
            :key="subCategory.id"
          >
            <h2 class="accordion-header" :id="'heading-' + subCategory.id">
              <button
                class="accordion-button"
                type="button"
                data-bs-toggle="collapse"
                :data-bs-target="'#collapse-' + subCategory.id"
                aria-expanded="true"
                :aria-controls="'collapse-' + subCategory.id"
              >
                {{ subCategory.name }}
              </button>
            </h2>
            <div
              :id="'collapse-' + subCategory.id"
              class="accordion-collapse collapse show"
              :aria-labelledby="'heading-' + subCategory.id"
            >
              <div class="accordion-body">
                <div class="row">
                  <div
                    class="col-md-3"
                    v-for="product in subCategory.products"
                    :key="product.id"
                  >
                    <div class="card shadow-sm">
                      <img
                        :src="product.image"
                        alt="Product Image"
                        class="card-img-top"
                      />
                      <div class="card-body">
                        <h5 class="card-title">{{ product.name }}</h5>
                        <p class="card-text">${{ product.price }}</p>
                        <button class="btn btn-outline-danger">
                          Add to Cart
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
    <footer class="bg-dark text-white py-4">
      <div class="container text-center">
        <p>&copy; 2024 iFutureBD. All Rights Reserved.</p>
        <div class="d-flex justify-content-center">
          <a href="/about" class="text-white mx-2">About</a>
          <a href="/contact" class="text-white mx-2">Contact</a>
          <a href="/privacy" class="text-white mx-2">Privacy</a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import config from '../config/config';
export default {
  name: "Home",
  data() {
    return {
      categories: [],
      activeCategory: null,
      activeSubCategories: [],
    };
  },
  mounted() {
    this.fetchCategories();
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await fetch(
          `${config.base_url}/products/products/hierarchical/`
        );
        const data = await response.json();
        this.categories = data.categories.filter(
          (category) =>
            category.subCategories.length &&
            category.subCategories.some((sub) => sub.products.length)
        );
      } catch (error) {
        console.error("Failed to fetch categories", error);
      }
    },
    toggleCategory(categoryId) {
      this.activeCategory = categoryId;
      const category = this.categories.find(
        (cat) => cat.id === categoryId
      );
      this.activeSubCategories = category ? category.subCategories : [];
    },
    getCategoryImage(category) {
      return category.image;
    },
    getCategoryName(categoryId) {
      const category = this.categories.find((cat) => cat.id === categoryId);
      return category ? category.name : "";
    },
  },
};
</script>

<style scoped>
.brand-logo {
  width: 50px;
}
.hero-section {
  background: linear-gradient(to right, #e74c3c, #2c3e50);
}
.category-highlights .card {
  border: none;
  overflow: hidden;
  transition: transform 0.3s ease;
}
.category-highlights .card:hover {
  transform: scale(1.05);
}
.product-list .accordion-button {
  font-weight: bold;
}
.product-list .card {
  border: none;
  overflow: hidden;
  transition: transform 0.3s ease;
}
.product-list .card:hover {
  transform: scale(1.05);
}
</style>
