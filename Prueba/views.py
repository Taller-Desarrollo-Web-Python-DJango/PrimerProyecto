from django.shortcuts import render, HttpResponse # Importamos HttpResponse para devolver respuestas HTTP.

# Create your views here.

# Vista para la página de inicio.

# Primera forma de devolver una respuesta HTTP simple.
# def home(request):
    # return HttpResponse("<h1>Esto es una prueba</h1><h2>Hola Mundo en Django</h2>")

# Segunda forma de devolver una respuesta HTTP con un bucle.
# def home(request):
    # http_response = ""
    # for i in range (6):
        # http_response += "<h" + str(i+1) + ">" + "Hola Mundo en Django" + "</h" + str(i+1) + ">"
        # return HttpResponse(http_response)

# Tercera forma de devolver una respuesta HTTP con HTML y CSS embebido.
def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&family=Roboto:wght@400&display=swap');
            
            body {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Roboto', sans-serif;
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 3rem;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                border: 1px solid rgba(255, 255, 255, 0.18);
            }
            h1 {
                font-family: 'Poppins', sans-serif;
                font-size: 4rem;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            h2 {
                font-size: 2rem;
                color: #00d4ff;
                font-weight: 300;
            }
            .emoji {
                font-size: 5rem;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🚀</div>
            <h1>¡Esto es una prueba!</h1>
            <h2>Hola Mundo en Django ✨</h2>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)