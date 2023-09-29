<template>
  <div>
    <div v-for="(tag, index) in tags" :key="index" class="tag">
      {{ tag.name }}
      <button @click="removeTag(index)" class="remove-tag">Remove</button>
    </div>
    <input
      v-model="newTag"
      @keyup.enter="addTag"
      placeholder="Add tags (press Enter to add)"
    />
  </div>
</template>

<script>
export default {
  name: "TagComponent",
  data() {
    return {
      tags: [],
      newTag: "",
    };
  },
  methods: {
    addTag() {
      if (this.newTag.trim() !== "") {
        this.tags.push({ name: this.newTag.trim() });
        this.newTag = "";
      }
    },
    removeTag(index) {
      this.tags.splice(index, 1);
    },
  },
};
</script>

<style scoped>
.tag {
  display: inline-block;
  margin-right: 8px;
  background-color: #007bff;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
}

.remove-tag {
  background-color: #dc3545;
  color: white;
  border: none;
  cursor: pointer;
}

input {
  margin-top: 8px;
  padding: 4px 8px;
}
</style>
