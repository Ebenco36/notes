<template>
  <div>
    <h2>Tags</h2>
    <ul>
      <li v-for="(tag, index) in tags" :key="index">
        {{ tag }}
        <button @click="deleteTag(index)">Delete</button>
      </li>
    </ul>
    <div>
      <label for="tag">Add Tag:</label>
      <input type="text" v-model="newTag" @keydown.enter="addTag" />
    </div>
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
      const tag = this.newTag.trim();
      if (tag !== "") {
        this.tags.push(tag);
        this.newTag = "";
      }
    },
    deleteTag(index) {
      this.tags.splice(index, 1);
    },
  },
};
</script>
