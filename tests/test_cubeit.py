from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8000/"
def test_cube(page: Page):
    page.goto(BASE_URL)
    input_box = page.get_by_role("spinbutton")
    input_box.fill("3")
    submit_button = page.get_by_role("button", name="Calculate Cube")
    submit_button.click()
    result = page.locator("css=p#resultText")
    expect(result).to_contain_text("27")

def test_empty_input(page: Page):
    page.goto(BASE_URL)
    input_box = page.get_by_role("spinbutton")
    input_box.fill("")
    submit_button = page.get_by_role("button", name="Calculate Cube")
    submit_button.click()
    result = page.locator("css=p#resultText")
    expect(result).to_contain_text("Please enter a valid number.")