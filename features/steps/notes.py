from behave import given, when, then

"""
    Implementation was omitted to meet up with other things.
    However, we can do this as soon as possible.
    Major require for stalkholders
"""
@given('the user is logged in')
def step_user_logged_in(context):
    return True

@when('the user creates a new note with title "{title}" and body "{body}" and tags "{tags}"')
def step_create_new_note(context, title, body, tags):
    pass

@then('the note "{title}" should be saved')
def step_check_note_saved(context, title):
    pass

@then('the note should have tags "{tags}"')
def step_check_note_tags(context, tags):
    pass

@when('the user edits the note with title "{title}" and updates the body to "{new_body}"')
def step_edit_existing_note(context, title, new_body):
    pass


@when('the user views their list of notes')
def step_view_list_of_notes(context):
    pass

@then('they should see a list of their notes')
def step_check_list_of_notes(context):
    pass

@when('the user filters their notes by tag "{tag}"')
def step_filter_notes_by_tag(context, tag):
    pass

@then('they should see a list of notes with tag "{tag}"')
def step_check_filtered_notes(context, tag):
    pass


@then('User creates a public note')
def step_create_public_note():
    pass
