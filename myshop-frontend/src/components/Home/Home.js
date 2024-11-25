import config from '../../config/config';
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