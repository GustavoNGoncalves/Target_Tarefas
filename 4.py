# 4) Valor Faturamento.

def calculo_percent(estado,total):
    return (estado / total) * 100

def main():
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    outros = 19849.53

    total = sp + rj + mg + es + outros

    perc_sp = calculo_percent(sp,total)
    perc_rj = calculo_percent(rj,total)
    perc_mg = calculo_percent(mg,total)
    perc_es = calculo_percent(es,total)
    perc_outros = calculo_percent(outros,total)

    print(f"Percentual de SP: {perc_sp:.2f}%")
    print(f"Percentual de RJ: {perc_rj:.2f}%")
    print(f"Percentual de MG: {perc_mg:.2f}%")
    print(f"Percentual de ES: {perc_es:.2f}%")
    print(f"Percentual de outros estados: {perc_outros:.2f}%")
    Soma = perc_sp + perc_rj + perc_mg + perc_es + perc_outros
    print(f"Soma dos percentuais: {Soma:.2f}%")

main()
