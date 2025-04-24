from fpdf import FPDF




def main():

    pdf = FPDF()
    str = input("Name: ") + "\n\ntook CS50"
    pdf.set_top_margin(30)
    pdf.set_font('helvetica', size=60)

    pdf.add_page()
    pdf.cell(text="CS50 Shirtificate", align='C', center=True)
    pdf.set_auto_page_break(False, margin=4)
    pdf.set_y(70)
    #pdf.set_x(5)
    pdf.image('shirtificate.png', h=pdf.eph/1.3, w=pdf.epw, x=pdf.epw/20)

    pdf.set_y(130)
    pdf.set_font('Courier', style='B', size=40)
    pdf.set_text_color(255,255,255)
    #pdf.cell(text=str, align='C', center=True)
    pdf.multi_cell(0, text=str, align='C', center=True)

    pdf.output("shirtificate.pdf")


'''
    level0 = TitleStyle("Helvetica", "B", 20, (0, 0, 0))
    pdf.section_title_styles(level0)
    pdf.start_section('CS50 Shirtificate', level=0, strict=True)
'''

if __name__ == '__main__':
    main()
