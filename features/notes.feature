Feature: Note Management

  Scenario: User adds a new note
    Given the user is logged in
    When the user creates a new note with title "Sample Note" and body "This is a sample note." and tags "tag1, tag2"
    Then the note "Sample Note" should be saved
    And the note should have tags "tag1, tag2"
    
  Scenario: User deletes an existing note
    Given the user is logged in
    When the user deletes the note with title "Sample Note"
    Then the note "Sample Note" should be deleted
    
  Scenario: User modifies an existing note
    Given the user is logged in
    When the user edits the note with title "Sample Note" and updates the body to "Updated sample note."
    Then the note "Sample Note" should be updated with body "Updated sample note."
    
  Scenario: User views a list of their notes
    Given the user is logged in
    When the user views their list of notes
    Then they should see a list of their notes
    
  Scenario: User filters notes by tags
    Given the user is logged in
    When the user filters their notes by tag "tag1"
    Then they should see a list of notes with tag "tag1"
    
