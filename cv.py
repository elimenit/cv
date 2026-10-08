"""Archivo que genera PDF para el Curriculum Vitae de Elmer Yachak Vilcapuma Chachavot.
@Autor: Elmer Yachak Vilcapuma Chachavot
"""
from weasyprint import HTML
from pypdf import PdfReader

def check_count_pages(file_pdf: str, count_pages: int)-> bool:
    """Comprueb si un PDF tiene count_pages paginas.
    """
    reader = PdfReader(file_pdf)
    pages: int = len(reader.pages)
    return pages == count_pages


def generate_pdf(html_path: str, pdf_path: str)-> None:
    """Genera el archivo PDF a partir de la ruta del archivo HTML.
    """
    HTML(filename=html_path).write_pdf(pdf_path)

def main()-> None:
    """Funcion principal.
    """
    roles: list = [
        "devops",
        "cloud_security",
        "cybersecurity_analyst"
    ]
    print("Generando CVS....")
    for file in roles:
        generate_pdf(file+".html", (file+"_Elmer_Yachak"+".pdf").capitalize())
        print(f"CV generado exitosamente: {(file+".pdf").capitalize()}")
        
    
if __name__ == '__main__':
    """Se ejecuta siempre y cuando estes en este directorio.
    """
    main()