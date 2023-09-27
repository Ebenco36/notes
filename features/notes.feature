Feature: Notes Management

    Scenario: Creating a new note
        Given a logged-in user
        When the user creates a new note with title "Test Note" and content "This is a test note"
        Then the note is created successfully

    Scenario: Viewing a note
        Given a logged-in user
        When the user views the note with title "Test Note"
        Then the note details are displayed

    Scenario: Editing a note
        Given a logged-in user
        When the user edits the note with title "Test Note" and updates the content to "Updated content"
        Then the note is updated successfully

    Scenario: Deleting a note
        Given a logged-in user
        When the user deletes the note with title "Test Note"
        Then the note is deleted successfully
