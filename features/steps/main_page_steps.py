from behave import given, when, then


@when('Click on Settings option')
def click_settings(context):
    context.app.main_page.click_settings()

@when('Click on Off-Plan option')
def click_off_plan(context):
    context.app.main_page.click_off_plan()