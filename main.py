import flet as ft
from flet import *
from datetime import datetime, timedelta
from Previsao_semana import obter_informacoes_por_semana
from Previsao_dia import obter_informacoes_dia

def Main(tela):
    tela.bgcolor = "#F5F5F5"
    tela.title = "Previsão do Tempo"

    #On-click do botão
    def Buscar(e):
        tela.clean()
        
        informacoes_semana = obter_informacoes_por_semana(Buscar_cidade.value)
        informacoes_dia = obter_informacoes_dia(Buscar_cidade.value)
        
        codigo_icon = informacoes_dia['weather'][0]['icon']
        
        #Nascer e pôr do sol
        sunrise = datetime.utcfromtimestamp(informacoes_dia['sys']['sunrise'])
        sunset = datetime.utcfromtimestamp(informacoes_dia['sys']['sunset'])
        sunrise_local = sunrise + timedelta(seconds=informacoes_dia['timezone'])
        sunset_local = sunset + timedelta(seconds=informacoes_dia['timezone'])
        

            
        tela_principal = Row([
            Column([
                #Nome do local
                Container(
                    Text(
                        f"{Buscar_cidade.value.upper()}, {informacoes_dia['sys']['country']}", 
                        color=colors.BLACK, 
                        size=40, 
                        font_family="Cambria",
                    ),
                    padding = padding.only(top=10),
                ),
                #Temperatura atual
                Container(
                    Text(
                        f"{informacoes_dia['main']['temp']:.1f}°", 
                        size= 75, 
                        color= colors.BLACK,
                        font_family="Cambria",
                        text_align = "CENTER",
                    ),
                    width=300,
                ), 
                #Descrição
                Container(
                    Row([
                        Text(
                            informacoes_dia['weather'][0]['description'].capitalize(), 
                            color="#F5F5F5", 
                            size=30, 
                            font_family="Cambria",
                        ), 
                        Image(src=f"https://openweathermap.org/img/wn/{codigo_icon}@2x.png")
                    ], 
                    alignment="CENTER"),
                    bgcolor="#001F3F",
                    border_radius=100,
                    height= 70,
                    padding = padding.only(left=30),
                ), 
                #Sensação térmica
                Container(
                    Text(
                        f"Sensação térmica: {informacoes_dia['main']['feels_like']:.1f}°", 
                        size= 23, 
                        color= colors.BLACK,
                        font_family="Cambria",
                    ),  
                ), 
                #Min / Max
                Container(
                    Text(
                        f"Max: {informacoes_dia['main']['temp_max']:.1f}° / Min: {informacoes_dia['main']['temp_min']:.1f}°", 
                        size= 23, 
                        color= colors.BLACK,
                        font_family="Cambria",
                    ),
                ),
                #Nascer do Sol e Vento
                Container(
                    Row([
                        Row([
                            Text(
                                f"Nascer do sol: {sunrise_local.strftime('%H:%M')}", 
                                color=colors.BLACK, 
                                size=23, 
                                font_family="Cambria",
                            ),
                            ft.Icon(name=ft.icons.SUNNY, color=colors.YELLOW, size= 70)
                        ]),

                        Row([
                            Text(
                                f"Vento: {informacoes_dia['wind']['speed'] * 3.6:.0f} km/h", 
                                color=colors.BLACK, 
                                size=23, 
                                font_family="Cambria",
                            ),
                            ft.Icon(name=ft.icons.WIND_POWER, color=colors.BLACK, size= 60)
                        ])
                    ], alignment="spaceBetween")
                ),
                #Pôr do Sol e Umidade
                Container(
                    Row([
                        Row([
                            Text(
                                f"Pôr do sol: {sunset_local.strftime('%H:%M')}", 
                                color=colors.BLACK, 
                                size=23, 
                                font_family="Cambria",
                            ),
                            ft.Icon(name=ft.icons.SUNNY, color=colors.ORANGE_900, size= 70)
                        ]),
                        
                        Row([
                            Text(
                                f"Umidade: {informacoes_dia['main']['humidity']}%", 
                                color=colors.BLACK, 
                                size=20, 
                                font_family="Cambria",
                            ),
                            ft.Icon(name=ft.icons.WATER_DROP, color=colors.BLUE, size= 60)
                        ])
                    ], alignment="spaceBetween")
                )
            ], width=600),
            
            #Previsão da semana
            Container(
                Column([
                    Row([
                        Text(
                            f"{informacoes_semana['2_dia']['dia']}", 
                            color="#F5F5F5", 
                            size=20, 
                            font_family="Cambria",
                        ),
                        
                        Row([
                            ft.Icon(name=ft.icons.WATER_DROP, color=colors.BLUE, size= 20),
                            Text(
                                f"{informacoes_semana['2_dia']['media_umidade']:.0f}%", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ]),
                        Image(src=f"https://openweathermap.org/img/wn/{informacoes_semana['2_dia']['icone_mais_comum']}@2x.png"),
                        Row([
                            Text(
                                f"{informacoes_semana['2_dia']['menor_temperatura']:.1f} / {informacoes_semana['2_dia']['maior_temperatura']:.1f} ", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ])
                    ]),



                    Row([
                        Text(
                            f"{informacoes_semana['3_dia']['dia']}", 
                            color="#F5F5F5", 
                            size=20, 
                            font_family="Cambria",
                        ),
                        Row([
                            ft.Icon(name=ft.icons.WATER_DROP, color=colors.BLUE, size= 20),
                            Text(
                                f"{informacoes_semana['3_dia']['media_umidade']:.0f}%", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ]),
                        Image(src=f"https://openweathermap.org/img/wn/{informacoes_semana['3_dia']['icone_mais_comum']}@2x.png"),
                        Row([
                            Text(
                                f"{informacoes_semana['3_dia']['menor_temperatura']:.1f} / {informacoes_semana['3_dia']['maior_temperatura']:.1f} ", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ])
                    ]),



                    Row([
                        Text(
                            f"{informacoes_semana['4_dia']['dia']}", 
                            color="#F5F5F5", 
                            size=20, 
                            font_family="Cambria",
                        ),
                        Row([
                            ft.Icon(name=ft.icons.WATER_DROP, color=colors.BLUE, size= 20),
                            Text(
                                f"{informacoes_semana['4_dia']['media_umidade']:.0f}%", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ]),
                        Image(src=f"https://openweathermap.org/img/wn/{informacoes_semana['4_dia']['icone_mais_comum']}@2x.png"),
                        Row([
                            Text(
                                f"{informacoes_semana['4_dia']['menor_temperatura']:.1f} / {informacoes_semana['4_dia']['maior_temperatura']:.1f} ", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ])
                    ]),



                    Row([
                        Text(
                            f"{informacoes_semana['5_dia']['dia']}", 
                            color="#F5F5F5", 
                            size=20, 
                            font_family="Cambria",
                        ),
                        Row([
                            ft.Icon(name=ft.icons.WATER_DROP, color=colors.BLUE, size= 20),
                            Text(
                                f"{informacoes_semana['5_dia']['media_umidade']:.0f}%", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ]),
                        Image(src=f"https://openweathermap.org/img/wn/{informacoes_semana['5_dia']['icone_mais_comum']}@2x.png"),
                        Row([
                            Text(
                                f"{informacoes_semana['5_dia']['menor_temperatura']:.1f} / {informacoes_semana['5_dia']['maior_temperatura']:.1f} ", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ])
                    ]),



                    Row([
                        Text(
                            f"{informacoes_semana['6_dia']['dia']}", 
                            color="#F5F5F5", 
                            size=20, 
                            font_family="Cambria",
                        ),
                        Row([
                            ft.Icon(name=ft.icons.WATER_DROP, color=colors.BLUE, size= 20),
                            Text(
                                f"{informacoes_semana['6_dia']['media_umidade']:.0f}%", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ]),
                        Image(src=f"https://openweathermap.org/img/wn/{informacoes_semana['6_dia']['icone_mais_comum']}@2x.png"),
                        Row([
                            Text(
                                f"{informacoes_semana['6_dia']['menor_temperatura']:.1f} / {informacoes_semana['6_dia']['maior_temperatura']:.1f} ", 
                                color="#F5F5F5", 
                                size=20, 
                                font_family="Cambria",
                            ),
                        ])
                    ])
                ]),
                bgcolor="#001F3F",
                border_radius= 10,
                padding = padding.only(left=30, right=30, top=10, bottom=10),
            )
        ], alignment="spaceBetween",
        )
        
    

        tela.add(Barra, tela_principal)
        Buscar_cidade.value = ""
        tela.update()

    
    #Area de Busca
    Buscar_cidade = ft.TextField(
        label= "Buscar Cidade", 
        on_submit=Buscar,
        width=450,
        border_color="#F5F5F5",
        border_radius=100,
        color="#F5F5F5",
        cursor_color="#F5F5F5",
        content_padding=20,
        capitalization=ft.TextCapitalization.CHARACTERS
        )
    
    #Barra superior
    Barra = AppBar(
        toolbar_height= 120,
        bgcolor= "#001F3F",
        title=Row([
            Container(
                content = Text("Bem vindo(a)!\n\t\t\t\t\tVeja a previsão do tempo na sua cidade!", font_family= "Cambria", size= 30)
            ),

            Container(
                content=Buscar_cidade,
                padding = padding.only(left=300)
            ),

            ft.Icon(name=ft.icons.SEARCH, color="#F5F5F5", size= 25)
        ])
    )

    #Tela inicial
    TxT_Inicio = Row([

        Container(
            content=Text(
                "QUALQUER LUGAR",
                color= colors.BLACK, 
                size=25,  
                text_align = "LEFT",
                font_family= "Calibri",
                style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color ="#001F3F"),
                italic = True
                ),
            padding = padding.only(top=30),  
        ),

        Container(
            content=Text(
                "EM TEMPO REAL",
                color= colors.BLACK, 
                size=25,  
                text_align = "LEFT",
                font_family= "Calibri",
                style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color ="#001F3F"),
                italic = True
                ),
            padding = padding.only(top=30),
        ),

        Container(
            content=Text(
                "PRÁTICO E RÁPIDO",
                color= colors.BLACK, 
                size=25,  
                text_align = "LEFT",
                font_family= "Calibri",
                style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, decoration_color ="#001F3F"),
                italic = True
                ),
            padding = padding.only(top=30),
        )
    ], alignment="spaceEvenly")


    img_Inicio = Row([
        Container(
                Image(
                    src=f"assets\sol.png",
                    width= 100
                ),
                padding = padding.only(top=280),
           ),
        Container(
                Image(
                    src=f"assets\_Nuvem.png",
                    width= 100
                ),
                padding = padding.only(top=280),
           ),
        Container(
                Image(
                    src=f"assets\chuva.png",
                    width= 100
                ),
                padding = padding.only(top=280),
           )
    ], alignment="CENTER")
    
    
    
    tela.add(Barra, TxT_Inicio, img_Inicio)
    tela.update()
ft.app (target = Main, assets_dir="assets", web_renderer=ft.WebRenderer.HTML)

#view=ft.AppView.WEB_BROWSER