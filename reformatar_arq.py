projeto = "valores"
horas_estimadas= "48"
valor_hora = "120"
prazo_estimado= "2 dias"
valor_total_estimado= '(120 * 48)=5760'

from fpdf import FPDF
pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial")


pdf.image("template.png", x=0, y=0)

pdf.text(115 , 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, valor_total_estimado)


pdf.output("Orcamento Python.pdf")