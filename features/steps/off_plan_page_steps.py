from behave import given, when, then


@then('Verify Off-Plan page opens')
def verify_off_plan_opens(context):
    context.app.off_plan_page.verify_off_plan_opens()

@when('Filter by sales status of "{status}"')
def filter_by_status(context, status):
    context.app.off_plan_page.filter_by_status(status)

@then('Verify each product has "{status}"')
def verify_product_status(context, status):
    context.app.off_plan_page.verify_product_status(status)