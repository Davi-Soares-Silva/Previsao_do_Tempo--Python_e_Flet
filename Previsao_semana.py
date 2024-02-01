import requests
from datetime import datetime

def obter_informacoes_por_semana(cidade):
    API_KEY = ""

    link_semana = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

    requisicao_semana = requests.get(link_semana)
    requisicao_semana_dic = requisicao_semana.json()

    informacoes_bruta_por_dia = {}

    for i, previsao in enumerate(requisicao_semana_dic['list'], start=1):
        dia = datetime.utcfromtimestamp(previsao['dt']).strftime('%d/%m')

        if dia not in informacoes_bruta_por_dia:
            informacoes_bruta_por_dia[dia] = []

        informacoes_bruta_por_dia[dia].append({
            'temperatura': previsao['main']['temp'],
            'umidade': previsao['main']['humidity'],
            'icone': previsao['weather'][0]['icon']
        })

    
    informacoes_por_dia = {}

    for i, (dia, informacoes) in enumerate(informacoes_bruta_por_dia.items(), start=1):
        temperaturas = [info['temperatura'] for info in informacoes]
        umidades = [info['umidade'] for info in informacoes]
        icons = [info['icone'] for info in informacoes]

        menor_temperatura = min(temperaturas)
        maior_temperatura = max(temperaturas)
        media_umidade = sum(umidades) / len(umidades)
        icone_mais_comum = max(set(icons), key=icons.count)

        informacoes_por_dia[f"{i}_dia"] = {
            'dia': dia,
            'menor_temperatura': menor_temperatura,
            'maior_temperatura': maior_temperatura,
            'media_umidade': media_umidade,
            'icone_mais_comum': icone_mais_comum
        }


    return informacoes_por_dia
