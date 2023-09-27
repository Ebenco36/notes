from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@given('a logged-in user')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('http://localhost:8000/admin/')
    # Implement user login with Selenium

@when('the user creates a new note with title "{title}" and body "{body}"')
def step_impl(context, title, body):
    # Navigate to the note creation page (e.g., /notes/create/)
    context.browser.get('http://localhost:8000/notes/create/')
    
    # Fill out the note creation form using Selenium
    title_input = context.browser.find_element_by_name('title')
    content_input = context.browser.find_element_by_name('body')

    title_input.send_keys(title)
    content_input.send_keys(body)

    # Submit the form
    content_input.send_keys(Keys.ENTER)

@then('the note is created successfully')
def step_impl(context):
    # Implement verification of successful note creation

@when('the user views the note with title "{title}"')
def step_impl(context, title):
    # Implement note viewing with Selenium

@then('the note details are displayed')
def step_impl(context):
    # Verify that the note details are displayed on the page
    # You can use Selenium to check for the presence of the note's title and content
    assert context.browser.find_element_by_id('note-title').text == context.text
    assert context.browser.find_element_by_id('note-content').text == context.text

@when('the user edits the note with title "{title}" and updates the content to "{body}"')
def step_impl(context, title, body):
    # Navigate to the page where the note with the specified title can be edited
    context.browser.get(f'http://localhost:8000/notes/{title}/edit/')

    # Find the content input field and update its value
    content_input = context.browser.find_element_by_name('content')
    content_input.clear()
    content_input.send_keys(body)

    # Submit the form
    context.browser.find_element_by_id('submit-button').click()

@then('the note is updated successfully')
def step_impl(context):
    # Implement verification of successful note update

@when('the user deletes the note with title "{title}"')
def step_impl(context, title):
    # Implement note deletion with Selenium

@then('the note is deleted successfully')
def step_impl(context):
    # Implement verification of successful note deletion

@after.each_scenario
def close_browser(context, scenario):
    if context.browser:
        context.browser.quit()