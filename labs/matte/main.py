import random
from pyscript.web import page, when

(input_content,) = page["#input-content"]
result = None


def success():
    page["#result"][0].textContent = "✅"


def fail():
    page["#result"][0].textContent = "❌"


def verify(e):
    try:
        if int(result) == int(input_content.value):
            new_equation()
            success()
        else:
            fail()
    except ValueError:
        pass


def new_equation():
    global result
    input_content.value = ""

    x = random.randint(0, 10)
    y = random.randint(0, 10)
    result = x * y

    # create task
    ekv = f"{x} x {y}"

    page["#ekvation"][0].textContent = ekv


@when("click", "#verify-btn")
def add_task(e):
    verify(e)


def add_task_event(e):
    if e.key == "Enter":
        verify(e)


input_content.onkeypress = add_task_event
new_equation()
