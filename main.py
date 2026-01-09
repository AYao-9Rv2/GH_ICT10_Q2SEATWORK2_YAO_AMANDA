from pyscript import display, document

def student_gwa(e):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    name = f"{fname} {lname}"

    eng = float(document.getElementById("eng").value)
    math = float(document.getElementById("math").value)
    sci = float(document.getElementById("sci").value)
    ss = float(document.getElementById("ss").value)
    ve = float(document.getElementById("ve").value)
    filo = float(document.getElementById("filo").value)

    gwa = (eng + math + sci + ss + ve + filo) / 6 

    display(
        f'hello {name}, thank you for using this calculator! '
        f'here is your general weighted average: {gwa:.2f}',
        target='output'
    )

    num1 = int(gwa)

    if num1 > 74:
        display('you passed', target='output')
    else:
        display('you failed', target='output')
