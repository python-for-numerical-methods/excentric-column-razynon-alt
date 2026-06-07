def find_critical_load(L, E, A, r, c, e, sigma_allow):
    """
    L: אורך במ"מ
    E: מודול אלסטיות ב-MPa
    A: שטח חתך בממ"ר
    r: רדיוס אינרציה במ"מ
    c: מרחק לסיב קיצוני במ"מ
    e: אקסצנטריות במ"מ
    sigma_allow: מאמץ מותר ב-MPa

    Return: העומס P בניוטון (float)
    """
 def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    # פרמטרים לדוגמה
    #A, E, L, r, e, c = 5000, 200000, 3000, 50, 20, 100
    
    # נוסחת הסקנט
    sec_term = 1 / np.cos((L/(2*r)) * np.sqrt(P/(E*A)))
    sigma_max = (P/A) * (1 + (e*c/r**2) * sec_term)
    
    return sigma_max - sigma_allow

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    P_critical = optimize.newton(lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow), 500000)
    return P_critical
