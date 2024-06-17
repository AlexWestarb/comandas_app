from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from datetime import datetime
from io import BytesIO
from PIL import Image
import base64, re, os

class PDFGenerator:

    def __init__(self):
        self.buffer = BytesIO()
        self.c = canvas.Canvas(self.buffer, pagesize=A4)
        self.width, self.height = A4

    def header(self):
        self.c.drawImage("Comandas_app/scr/static/pastel.png", 10, self.height - 40, width=20, height=20)
        self.c.setFont("Helvetica-Bold", 15)
        self.c.drawCentredString(self.width / 2, self.height - 30, "Pastelaria do Zé")

    def footer(self, page_num):
        self.c.setFont("Helvetica-Oblique", 8)
        self.c.drawString(10, 15, f"Página {page_num}")
        self.c.drawCentredString(self.width / 2, 15, "Pastelaria do Zé")

    def save_pdf(self, filename):
        self.c.save()
        with open(filename, "wb") as f:
            f.write(self.buffer.getvalue())
        self.buffer.close()

    def generate_pdf_funcionarios(self, funcionarios):
        self.c.setAuthor("Pastelaria do Zé")
        self.c.setTitle("Funcionários")
        self.header()
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawCentredString(self.width / 2, self.height - 60, "Funcionários")
        self.c.setFont("Helvetica", 6)
        self.c.drawRightString(self.width - 10, self.height - 70, f"Emitido em: {datetime.now()}")
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(10, self.height - 100, "ID")
        self.c.drawString(40, self.height - 100, "Nome")
        self.c.drawString(150, self.height - 100, "Matrícula")
        self.c.drawString(200, self.height - 100, "CPF")
        self.c.drawString(250, self.height - 100, "Telefone")
        self.c.drawString(300, self.height - 100, "Grupo")

        self.c.setFont("Helvetica", 8)
        y = self.height - 120
        for row in funcionarios:
            self.c.drawString(10, y, str(row['id_funcionario']))
            self.c.drawString(40, y, row['nome'])
            self.c.drawString(150, y, row['matricula'])
            self.c.drawString(200, y, row['cpf'])
            self.c.drawString(250, y, row['telefone'])
            self.c.drawString(300, y, str(row['grupo']))
            y -= 20

        self.footer(1)
        self.save_pdf('pdfFuncionarios.pdf')

    def generate_pdf_clientes(self, clientes):
        self.c.setAuthor("Pastelaria do Zé")
        self.c.setTitle("Clientes")
        self.header()
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawCentredString(self.width / 2, self.height - 60, "Clientes")
        self.c.setFont("Helvetica", 6)
        self.c.drawRightString(self.width - 10, self.height - 70, f"Emitido em: {datetime.now()}")
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(10, self.height - 100, "ID")
        self.c.drawString(40, self.height - 100, "Nome")
        self.c.drawString(150, self.height - 100, "CPF")
        self.c.drawString(200, self.height - 100, "Telefone")

        self.c.setFont("Helvetica", 8)
        y = self.height - 120
        for row in clientes:
            self.c.drawString(10, y, str(row['id_cliente']))
            self.c.drawString(40, y, row['nome'])
            self.c.drawString(150, y, row['cpf'])
            self.c.drawString(200, y, row['telefone'])
            y -= 20

        self.footer(1)
        self.save_pdf('pdfClientes.pdf')

    def generate_pdf_produtos(self, produtos):
        self.c.setAuthor("Pastelaria do Zé")
        self.c.setTitle("Produtos")
        self.header()
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawCentredString(self.width / 2, self.height - 60, "Produtos")
        self.c.setFont("Helvetica", 6)
        self.c.drawRightString(self.width - 10, self.height - 70, f"Emitido em: {datetime.now()}")
        self.c.setFont("Helvetica-Bold", 8)
        self.c.drawString(10, self.height - 100, "ID")
        self.c.drawString(40, self.height - 100, "Nome")
        self.c.drawString(150, self.height - 100, "Descrição")
        self.c.drawString(300, self.height - 100, "Foto")
        self.c.drawString(400, self.height - 100, "Valor Unitário")

        self.c.setFont("Helvetica", 8)
        y = self.height - 140
        for row in produtos:
            self.c.drawString(10, y, str(row['id_produto']))
            self.c.drawString(40, y, row['nome'])
            self.c.drawString(150, y, row['descricao'])
            img_data = re.sub('^data:image/.+;base64,', '', row['foto'])
            img = Image.open(BytesIO(base64.b64decode(img_data)))
            img_path = f"temp_{row['id_produto']}.png"
            img.save(img_path, "PNG")
            self.c.drawImage(img_path, 300, y - 30, width=40, height=40)
            os.remove(img_path)
            self.c.drawString(400, y, str(row['valor_unitario']))
            y -= 60

        self.footer(1)
        self.save_pdf('pdfProdutos.pdf')