from behave import given, when, then


@then('Verify Community page opens')
def verify_right_page(context):
    context.app.community_page.verify_right_page()

@then('Verify the “Contact support” button is available and clickable')
def verify_support_button(context):
    context.app.community_page.verify_support_button()