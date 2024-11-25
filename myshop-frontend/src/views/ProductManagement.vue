<template>
  <div class="product-management-container">
    <!-- Left Section: Product List -->
    <div class="product-list-section">
      <h2>Product List</h2>
      <div class="table-container">
  <table class="table table-bordered table-striped table-hover">
    <thead class="table-dark">
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Price</th>
        <th>Stock</th>
        <th>Product Image</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="product in products" :key="product.id">
        <td>{{ product.name }}</td>
        <td>{{ product.description }}</td>
        <td>{{ product.price }}</td>
        <td>{{ product.stock }}</td>
        <td>
          <img :src="product.image" alt="Product Image" class="img-fluid product-image" />
        </td>
        <td>
          <button @click="editProduct(product)" class="btn btn-warning btn-sm">Edit</button>
          <button @click="deleteProduct(product.id)" class="btn btn-danger btn-sm">Delete</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>

    </div>

    <!-- Right Section: Category, SubCategory, Product Form -->
    <div class="form-section">
      <!-- Category, SubCategory, Product Management Buttons -->
      <div class="management-buttons">
        <button @click="createCategory" class="btn btn-success">Create Category</button>
        <button @click="createSubCategory" class="btn btn-info">Create SubCategory</button>
        <button @click="createProduct" class="btn btn-warning">Create Product</button>
      </div>

      <!-- Category Form -->
      <div v-if="showCategoryForm">
        <h3>Create Category</h3>
        <form @submit.prevent="submitCategory">
          <div class="mb-3">
            <label for="categoryName" class="form-label">Category Name</label>
            <input
                type="text"
                class="form-control"
                id="categoryName"
                v-model="category.name"
                required
            />
          </div>
          <div class="mb-3">
            <label for="categoryDescription" class="form-label">Category Description</label>
            <textarea
                class="form-control"
                id="categoryDescription"
                v-model="category.description"
                required
            ></textarea>
          </div>
          <div class="mb-3">
            <label for="categoryImage" class="form-label">Category Image</label>
            <input
                type="file"
                class="form-control"
                id="categoryImage"
                @change="handleCategoryImage"
                required
            />
          </div>
          <button type="submit" class="btn btn-primary">Create Category</button>
        </form>
      </div>

      <!-- SubCategory Form -->
      <div v-if="showSubCategoryForm">
        <h3>Create SubCategory</h3>
        <form @submit.prevent="submitSubCategory">
          <input v-model="subCategory.name" placeholder="SubCategory Name" required/>
          <textarea v-model="subCategory.description" placeholder="SubCategory Description" required></textarea>

          <!-- Category Dropdown -->
          <select v-model="subCategory.category" required>
            <option v-for="cat in categories" :value="cat.id" :key="cat.id">{{ cat.name }}</option>
          </select>

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>

      <!-- Product Form -->
      <div v-if="showProductForm">
        <h3>Create Product</h3>
        <form @submit.prevent="submitProduct" enctype="multipart/form-data">
          <input v-model="product.name" placeholder="Product Name" required/>
          <textarea v-model="product.description" placeholder="Product Description" required/>
          <input v-model="product.price" type="number" placeholder="Price" required/>
          <input v-model="product.stock" type="number" placeholder="Stock" required/>
          <select v-model="product.category" required>
            <option v-for="cat in categories" :value="cat.id" :key="cat.id">{{ cat.name }}</option>
          </select>
          <select v-model="product.sub_category" required>
            <option v-for="sub in subCategories" :value="sub.id" :key="sub.id">{{ sub.name }}</option>
          </select>
          <input type="file" @change="handleProductImage" required/>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>

      <!-- Category & SubCategory List -->
      <div class="category-list">
        <h3>Categories</h3>
        <ul>
          <li v-for="category in categories" :key="category.id">◉ {{ category.name }}</li>
        </ul>

        <h3>SubCategories</h3>
        <ul>
          <li v-for="subCategory in subCategories" :key="subCategory.id">◉ {{ subCategory.name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import config from '../config/config'; // Import config for API base URL

export default {
  data() {

    return {
      categoryName: "",
      categoryImage: null,

      products: [],
      showProductManagementPage: false,

      // Category Form
      showCategoryForm: false,
      category: {name: '', description: ''},

      // SubCategory Form
      showSubCategoryForm: false,
      subCategory: {name: '', description: '', category: ''},

      // Product Form
      showProductForm: false,
      product: {name: '', description: '', price: '', stock: '', category: '', sub_category: ''},
    };
  },
  created() {
    this.fetchCategories(); // Fetch categories when the page loads
    this.fetchSubCategories(); // Fetch subcategories if needed
    this.fetchProducts();
  },
  methods: {
    showProductManagement() {
      this.showProductManagementPage = true
    },

    // Fetch all products
    async fetchProducts() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          const response = await axios.get(`${config.base_url}/products/product/`, {
            headers: {Authorization: `Bearer ${accessToken}`},
          });
          this.products = response.data.results;
          this.showProductManagement();
        } catch (error) {
          if (error.response?.status === 401) {
            console.error('Unauthorized access. Redirecting to login page.');
            this.$router.push('/admin/login');  // Redirect to admin login page
          } else {
            console.error('Error fetching products:', error);
          }
        }
      }
    },

    // Handle edit product
    editProduct(product) {
      this.$router.push(`/admin/product/edit/${product.id}`);  // Navigate to edit page
    },

    // Handle delete product
    async deleteProduct(productId) {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          await axios.delete(`${config.base_url}/products/product/${productId}/`, {
            headers: {Authorization: `Bearer ${accessToken}`},
          });
          this.fetchProducts();  // Reload the product list after deletion
        } catch (error) {
          if (error.response?.status === 401) {
            console.error('Unauthorized access. Redirecting to login page.');
            this.$router.push('/admin/login');  // Redirect to admin login page
          } else {
            console.error('Error deleting product:', error);
          }
        }
      }
    },

    handleCategoryImage(event) {
      this.categoryImage = event.target.files[0];
    },

    // Submit Category Form with Image Upload
    async submitCategory() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          const formData = new FormData();
          formData.append('name', this.category.name);
          formData.append('description', this.category.description);
          formData.append('image', this.categoryImage); // Append image to the form data

          await axios.post(`${config.base_url}/products/categories/`, formData, {
            headers: {
              Authorization: `Bearer ${accessToken}`,
              'Content-Type': 'multipart/form-data' // Set content type to multipart
            },
          });

          this.showCategoryForm = false;
          alert('Category created successfully!');
          this.fetchCategories(); // Reload categories
        } catch (error) {
          if (error.response?.status === 401) {
            console.error('Unauthorized access. Redirecting to login page.');
            this.$router.push('/admin/login');
          }
          console.error('Error creating category:', error);
        }
      }
    },

    // Fetch Categories (unchanged)
    async fetchCategories() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          const response = await axios.get(`${config.base_url}/products/categories/`, {
            headers: {Authorization: `Bearer ${accessToken}`},
          });
          this.categories = response.data.results; // Store categories from 'results'
        } catch (error) {
          if (error.response?.status === 401) {
            console.error('Unauthorized access. Redirecting to login page.');
            await this.$router.push('/admin/login'); // Redirect to admin login page
          }
          console.error('Error fetching categories:', error);
        }
      }
    },

    // Fetch SubCategories
    async fetchSubCategories() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          const response = await axios.get(`${config.base_url}/products/subcategories/`, {
            headers: {Authorization: `Bearer ${accessToken}`},
          });
          this.subCategories = response.data.results; // Store subcategories from 'results'
        } catch (error) {
          if (error.response?.status === 401) {
            console.error('Unauthorized access. Redirecting to login page.');
            await this.$router.push('/admin/login'); // Redirect to admin login page
          }
          console.error('Error fetching subcategories:', error);
        }
      }
    },

    // Show the form for creating categories, subcategories, or products
    createCategory() {
      this.showCategoryForm = true;
      this.showSubCategoryForm = false;
      this.showProductForm = false;
    },

    createSubCategory() {
      this.showSubCategoryForm = true;
      this.showCategoryForm = false;
      this.showProductForm = false;
    },

    createProduct() {
      this.showProductForm = true;
      this.showCategoryForm = false;
      this.showSubCategoryForm = false;
    },

    // Handle file upload for product image
    handleProductImage(event) {
      this.productImage = event.target.files[0];
    },


    // Submit SubCategory Form
    async submitSubCategory() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          await axios.post(`${config.base_url}/products/subcategories/`, this.subCategory, {
            headers: {Authorization: `Bearer ${accessToken}`},
          });
          this.showSubCategoryForm = false;
          alert('SubCategory created successfully!');
          this.fetchSubCategories(); // Reload subcategories
        } catch (error) {
          if (error.response?.status === 401) {
            console.error('Unauthorized access. Redirecting to login page.');
            this.$router.push('/admin/login');
          }
          console.error('Error creating subcategory:', error);
        }
      }
    },

    // Submit Product Form
    async submitProduct() {
      const accessToken = localStorage.getItem('access_token');
      if (accessToken) {
        try {
          const formData = new FormData();
          formData.append('name', this.product.name);
          formData.append('description', this.product.description);
          formData.append('price', this.product.price);
          formData.append('stock', this.product.stock);
          formData.append('category', this.product.category);
          formData.append('sub_category', this.product.sub_category);
          formData.append('image', this.productImage);

          await axios.post(`${config.base_url}/products/product/`, formData, {
            headers: {
              Authorization: `Bearer ${accessToken}`,
              'Content-Type': 'multipart/form-data'
            },
          });

          this.showProductForm = false;
          alert('Product created successfully!');
          this.fetchProducts(); // Reload products
        } catch (error) {
          if (error.response?.status === 401) {
            console.error('Unauthorized access. Redirecting to login page.');
            this.$router.push('/admin/login');
          }
          console.error('Error creating product:', error);
        }
      }
    },
  },
};
</script>

<style scoped>
.product-management-container {
  display: flex;
  gap: 20px;
}

.product-list-section {
  width: 50%;
  max-width: 600px;
}

.form-section {
  width: 50%;
  max-width: 400px;
}

.management-buttons {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.management-buttons button {
  padding: 10px;
}

.product-table {
  width: 100%;
  border-collapse: collapse;
}

.product-table th, .product-table td {
  padding: 10px;
  text-align: left;
  border: 1px solid #ddd;
}

.product-table th {
  background-color: #f4f4f4;
}

.product-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
}

.edit-btn,
.delete-btn {
  padding: 5px 10px;
  margin-top: 5px;
}

.edit-btn {
  background-color: #007bff;
  color: white;
}

.delete-btn {
  background-color: #dc3545;
  color: white;
}

.edit-btn:hover,
.delete-btn:hover {
  cursor: pointer;
}

form input,
form select,
form textarea {
  width: 100%;
  padding: 10px;
  margin: 5px 0;
}

form button {
  padding: 10px 20px;
  margin-top: 10px;
}

.category-list {
  margin-top: 30px;
}

.category-list h3 {
  margin-bottom: 10px;
}

.category-list ul {
  list-style-type: none;
  padding-left: 0;
}

.category-list li {
  padding: 5px;
  background-color: #f4f4f4;
  margin-bottom: 5px;
  border-radius: 5px;
}
</style>

