<template>
  <div class="box">
    <span
      class="badge badge-primary"
      style="background-color: gray"
      v-for="tag in tags"
      :key="tag"
      >{{ tag }}</span
    >
    <h5 class="card-title">{{ title }}</h5>
    <p class="card-text">{{ body }}</p>
    <button class="btn-info btn-xs" @click="viewNote(id)">View</button>
    <button class="btn-success btn-xs" @click="editNote(id)">edit</button>
  </div>
</template>

<script>
export default {
  name: "NoteCard",
  props: {
    id: Number,
    tags: Array,
    title: String,
    body: String,
  },
  methods: {
    viewNote(id) {
      console.log(id);
      this.$router.push({ name: "view-note", params: { key: id } });
    },
    editNote(id) {
      console.log(id);
      this.$router.push({ name: "add-note", params: { key: id } });
    },
  },
};
</script>
<style scoped>
.box {
  background-color: #fff;
  color: black;
  border-radius: 5px;
  padding: 20px;
  border: 1px solid grey;
}
</style>
