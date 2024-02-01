import requests

def obter_informacoes_dia(cidade):

    API_KEY = ""
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
            
    requisicao= requests.get(link)
    requisicao_dic = requisicao.json()
    

    return requisicao_dic