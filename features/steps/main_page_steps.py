from behave import given, when, then


@when('Click on Settings option')
def click_settings(context):
    context.app.main_page.click_settings()