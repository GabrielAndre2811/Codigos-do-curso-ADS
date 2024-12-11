from PyPDF2 import PdfFileReader

def obter_titulo_pdf(caminho_pdf):
    try:
        pdf_document = PdfFileReader(caminho_pdf)
        info = pdf_document.getDocumentInfo()
        titulo = info.title if info.title else 'Sem Título'
        return titulo
    except Exception as e:
        print(f"Erro ao obter título do PDF: {e}")
        return 'Sem Título'
