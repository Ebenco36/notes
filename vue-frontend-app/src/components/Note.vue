<template>
  <div>
    <h2>Notes</h2>
    <ul>
      <li v-for="(note, index) in notes" :key="index">
        {{ note.text }}
        <button @click="deleteNote(index)">Delete</button>
        <div>
          <label for="tag">Add Tag:</label>
          <input type="text" v-model="newTag" @keydown.enter="addTag(index)" />
        </div>
        <div v-for="tag in note.tags" :key="tag">
          {{ tag }}
        </div>
      </li>
    </ul>
    <div>
      <label for="note">Add Note:</label>
      <input type="text" v-model="newNote" @keydown.enter="addNote" />
    </div>
  </div>
</template>
<script>
export default {
    name: "NoteComponent",
  data() {
    return {
      notes: [],
      newNote: "",
      newTag: "",
    };
  },
  methods: {
    addNote() {
      if (this.newNote.trim() !== "") {
        this.notes.push({ text: this.newNote, tags: [] });
        this.newNote = "";
      }
    },
    deleteNote(index) {
      this.notes.splice(index, 1);
    },
    addTag(noteIndex) {
      const tag = this.newTag.trim();
      if (tag !== "") {
        this.notes[noteIndex].tags.push(tag);
        this.newTag = "";
      }
    },
  },
};
</script>
