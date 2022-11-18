from behave import given, when, then

@given(u'que acesso a pagina do google')
def step_impl(context):
    context.web.get("https://google.com.br")

@when(u'realizo uma pesquisa')
def step_impl(context):
    context.element = driver.find_element("name", "q")
    context.element.click()
    context.element.send_keys("Marvel")
    context.element.submit()

@when(u'pesquisa e realizada')
def step_impl(context):
    assert context.web.title == "Marvel - Pesquisa Google"

@then(u'o titulo da pagina deve ser validado')
def step_impl(context):
    pass

