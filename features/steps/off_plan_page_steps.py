from behave import given, when, then


@then('Verify Off-Plan page opens')
def verify_off_plan_opens(context):
    context.app.off_plan_page.verify_off_plan_opens()

@when('Filter by sale status of "Announced"')
def filter_by_announced(context):
    context.app.off_plan_page.filter_by_announced()

@then('Verify each product has "Announced"')
def verify_announced_badge(context):
    context.app.off_plan_page.verify_announced_badge()