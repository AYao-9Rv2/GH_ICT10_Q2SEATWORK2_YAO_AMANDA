from pyscript import display, document

def student_grade(e):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    name = fname + lname

    display(f'hello {name}, thank you for using this calculator! here is your general weighted average:', target='output')
