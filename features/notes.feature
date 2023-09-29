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
    
  Scenario: User searches for notes with keywords
    Given the user is logged in
    When the user searches for notes containing the keyword "important"
    Then they should see a list of notes containing the keyword "important"
    
  Scenario: User creates a public note
    Given the user is logged in
    When the user creates a new public note with title "Public Note" and body "This is a public note." and tags "public, note"
    Then the note "Public Note" should be saved as public
    
  Scenario: Public notes can be viewed without authentication
    Given a public note exists with title "Public Note"
    When an unauthenticated user tries to view the note
    Then they should be able to view the note
    
  Scenario: Public notes cannot be modified
    Given a public note exists with title "Public Note"
    When an unauthenticated user tries to edit the note
    Then they should not be able to edit the note
    
  Scenario: User management API to create new users
    Given the application has a user management API
    When a new user registers with email "newuser@example.com" and password "password123"
    Then a new user account should be created
    
  Scenario: Users must be logged in to perform note actions
    Given the user is not logged in
    When the user tries to add, delete, modify, or view notes
    Then they should be redirected to the login page
