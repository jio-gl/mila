

import re, requests

html_content = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charSet="utf-8"/>
    <meta name="viewport" content="width=device-width"/>
    <title>Sueldo: Empleado en Argentina 2024 | Glassdoor</title>
    <meta property="og:title" content="Sueldo: Empleado en Argentina 2024"/>
    <meta name="description" content="El sueldo promedio de Empleado es $ 402.625 por año en Argentina. Haz clic aquí para ver el pago total, sueldos compartidos recientemente y más."/>
    <meta property="og:description" content="El sueldo promedio de Empleado es $ 402.625 por año en Argentina. Haz clic aquí para ver el pago total, sueldos compartidos recientemente y más."/>
    <!-- Other meta tags and HTML content -->
</head>
<body>
    <!-- Page content -->
</body>
</html>
'''

def salaryArgentinaARS(debug=False):

    url = 'https://www.glassdoor.com.ar/Sueldos/empleado-sueldo-SRCH_KO0,8.htm'
    url = 'https://www.google.com/search?q=Sueldos+para+Empleado+en+Argentina+glassdoor&sca_esv=182cfa181496f90a&source=hp&ei=dP-8Zs_nH5LY5OUPo-i86QY&iflsig=AL9hbdgAAAAAZr0NhDzzi9SqIZ2HrG6qkHUTECvpHzhL&ved=0ahUKEwjP8b6HlvWHAxUSLLkGHSM0L20Q4dUDCA0&uact=5&oq=Sueldos+para+Empleado+en+Argentina+glassdoor&gs_lp=Egdnd3Mtd2l6IixTdWVsZG9zIHBhcmEgRW1wbGVhZG8gZW4gQXJnZW50aW5hIGdsYXNzZG9vcjIFECEYoAFI8AFQAFgAcAB4AJABAJgBfKABfKoBAzAuMbgBA8gBAPgBAvgBAZgCAaACggGYAwCSBwMwLjGgB_0B&sclient=gws-wiz#vhid=zephyr:0&vssid=atritem-https://www.glassdoor.com.ar/Sueldos/empleado-sueldo-SRCH_KO0,8.htm'
    url = 'https://www.google.com/search?q=Sueldos+para+Empleado+en+Argentina+glassdoor'
    html_content = requests.get(url).text
    open('glassdoor.html', 'w').write(html_content)

    pattern = r'\$ ([\d.]+)'
    match = re.search(pattern, html_content)

    if match:
        salary_amount = match.group(1)
        salary_amount = int(salary_amount.replace('.', ''))*13
        if debug:   
            print(f"The average salary for an employee is: ${salary_amount}")
        return int(salary_amount)
    else:
        if debug:
            print("Salary information not found.")
        return None
    
if __name__ == "__main__":
    salaryArgentinaARS(debug=True)
