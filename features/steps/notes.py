from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Initialize a Selenium WebDriver instance (you can use a different browser driver)
driver = webdriver.Chrome()

# Placeholder URLs and element IDs (replace with your actual URLs and IDs)
login_url = 'http://your-app-url/login/'
create_note_url = 'http://your-app-url/create-note/'
login_button_id = 'login-button'
note_title_input_id = 'note-title'
note_body_input_id = 'note-body'
note_tags_input_id = 'note-tags'
save_note_button_id = 'save-button'

@given('the user is logged in')
def step_user_logged_in(context):
    # Implement code to log in the user using Selenium
    driver.get(login_url)
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.ID, login_button_id)
    
    # Enter login credentials
    username_input.send_keys('testuser')
    password_input.send_keys('password')
    
    # Click the login button
    login_button.click()

@when('the user creates a new note with title "{title}" and body "{body}" and tags "{tags}"')
def step_create_new_note(context, title, body, tags):
    # Implement code to create a new note using Selenium
    driver.get(create_note_url)
    
    title_input = driver.find_element(By.ID, note_title_input_id)
    body_input = driver.find_element(By.ID, note_body_input_id)
    tags_input = driver.find_element(By.ID, note_tags_input_id)
    save_button = driver.find_element(By.ID, save_note_button_id)
    
    # Enter note details
    title_input.send_keys(title)
    body_input.send_keys(body)
    tags_input.send_keys(tags)
    
    # Click the save button
    save_button.click()

@then('the note "{title}" should be saved')
def step_check_note_saved(context, title):
    # Implement code to check if the note with the given title is saved using Selenium
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{title}')]"))
    )

@then('the note should have tags "{tags}"')
def step_check_note_tags(context, tags):
    # Implement code to check if the note has the expected tags using Selenium
    tags_text = driver.find_element(By.ID, note_tags_input_id).text
    expected_tags = tags.split(', ')
    actual_tags = [tag.strip() for tag in tags_text.split(',')]
    
    assert set(expected_tags) == set(actual_tags)

@when('the user deletes the note with title "{title}"')
def step_delete_existing_note(context, title):
    # Implement code to delete a note using Selenium
    # Navigate to the page where you can delete the note (e.g., note details page)
    driver.get('http://your-app-url/note-details/')  # Replace with your note details page URL
    
    # Locate the delete button and click it
    delete_button = driver.find_element(By.ID, 'delete-button')  # Replace with actual ID
    delete_button.click()

@then('the note "{title}" should be deleted')
def step_check_note_deleted(context, title):
    # Implement code to check if the note with the given title is deleted using Selenium
    # You can check if the note is no longer present on the page
    note_element = driver.find_elements(By.XPATH, f"//*[contains(text(), '{title}')]")
    assert len(note_element) == 0, f'Note with title "{title}" is still present.'

@when('the user edits the note with title "{title}" and updates the body to "{new_body}"')
def step_edit_existing_note(context, title, new_body):
    # Implement code to edit an existing note using Selenium
    # Navigate to the page where you can edit the note (e.g., note details page)
    driver.get('http://your-app-url/note-details/')  # Replace with your note details page URL
    
    # Locate the edit button and click it
    edit_button = driver.find_element(By.ID, 'edit-button')  # Replace with actual ID
    edit_button.click()
    
    # Find the body input field and update the text
    body_input = driver.find_element(By.ID, 'note-body')  # Replace with actual ID
    body_input.clear()
    body_input.send_keys(new_body)
    
    # Save the changes (if applicable)
    save_button = driver.find_element(By.ID, 'save-button')  # Replace with actual ID
    save_button.click()

@then('the note "{title}" should be updated with body "{new_body}"')
def step_check_note_updated(context, title, new_body):
    # Implement code to check if the note with the given title is updated using Selenium
    # Navigate to the page where you can view the note (e.g., note details page)
    driver.get('http://your-app-url/note-details/')  # Replace with your note details page URL
    
    # Find the element containing the updated body and verify its text
    updated_body_element = driver.find_element(By.ID, 'note-body')  # Replace with actual ID
    assert updated_body_element.text == new_body, f'Note with title "{title}" is not updated with body "{new_body}".'

@when('the user views their list of notes')
def step_view_list_of_notes(context):
    # Implement code to navigate to the user's list of notes using Selenium
    driver.get('http://your-app-url/list-of-notes/')  # Replace with your list of notes page URL

@then('they should see a list of their notes')
def step_check_list_of_notes(context):
    # Implement code to check if the user can see their list of notes using Selenium
    # You can verify the presence of notes on the page
    notes_elements = driver.find_elements(By.CLASS_NAME, 'note-item')  # Replace with actual class name
    assert len(notes_elements) > 0, 'No notes are visible in the list.'

@when('the user filters their notes by tag "{tag}"')
def step_filter_notes_by_tag(context, tag):
    # Implement code to filter notes by tag using Selenium
    driver.get('http://your-app-url/list-of-notes/')  # Replace with your list of notes page URL
    
    # Locate the tag filter input field and apply the filter
    tag_filter_input = driver.find_element(By.ID, 'tag-filter-input')  # Replace with actual ID
    tag_filter_input.send_keys(tag)
    tag_filter_input.send_keys(Keys.RETURN)  # Press Enter to apply the filter

@then('they should see a list of notes with tag "{tag}"')
def step_check_filtered_notes(context, tag):
    # Implement code to check if the user can see a list of notes with the specified tag using Selenium
    # You can verify the presence of notes with the tag on the page
    notes_elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{tag}')]")
    assert len(notes_elements) > 0, f'No notes with tag "{tag}" are visible in the list.'




