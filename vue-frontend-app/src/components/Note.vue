<template>
  <div class="container">
    <div class="row">
      <div class="wrapper" v-if="notes.length > 0">
        <Card
          v-for="(item, index) in notes"
          :key="index"
          :id="item.id"
          :tags="item.tags"
          :title="item.title"
          :body="item.body"
        />
      </div>
      <div v-else>You do not have any note yet...</div>
    </div>
  </div>
</template>

<script>
import Card from "./Card.vue"; // Import the Card component

export default {
  name: "NoteComponent",
  props: {
    notes: Array,
  },
  components: {
    Card, // Register the Card component
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.wrapper {
  display: grid;
  grid-gap: 1rem;
  justify-content: center;
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 250px), 250px));
  background-color: #fff;
  color: #444;
}
</style>
