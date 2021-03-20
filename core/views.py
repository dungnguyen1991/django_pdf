from django.shortcuts import render

import io
from django.http import FileResponse

# reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle

def home(request):
    return render(request, 'core/home.html', {})

def reportlab_view(request):
    documentTitle = 'Document title'

    image = Image('core/qr_code.jpg')
    image.drawWidth = 2*cm
    image.drawHeight = 2*cm
    
    buffer = io.BytesIO()


    pdfmetrics.registerFont(
        TTFont('times_new_roman', 'core/font-times-new-roman.ttf')
    )

    doc = SimpleDocTemplate(buffer, pagesize=A4)
    doc.title = documentTitle

    elements = []

    

    data= [
        ['NS Đại Học - Chuyên Sách & Tài Liệu Ôn Thi', 'HÓA ĐƠN TMĐT'],
        ['Hotline: 0385840395 - 0563841586', 'Mã HĐ: 60312537'],
        ['www.sachlaptrinh.tk', image],
        ['NS Lập Trình - Chuyên Sách CNTT', ''],
        ['www.facebook.com/ICTBookShop', ''],
    ]
    t=Table(data, colWidths=[8*cm, 8*cm])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'times_new_roman'),
        #('BACKGROUND',(1,2),(-1,-1), colors.green),
        ('SPAN',(1,2),(1,4)),
        ('ALIGN', (1,0), (1,4), 'CENTER')
        # ('GRID', (0,0), (-1,-1), 1, colors.black),
        # ('BACKGROUND',(1,1),(-2,-2),colors.green),
        # ('TEXTCOLOR',(0,0),(1,-1),colors.red)
        ])
    )

    t2 = Table(data= [['Mã đơn TMĐT nguồn từ\n253268482194103', 'PHIẾU ĐÓNG GÓI 13\nXử lý: Kho Sách HN1 - In\nlúc: 17/08/2020 17:52:29']],
                      colWidths=[8*cm, 8*cm])

    t2.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'times_new_roman'),
        ('GRID', (0,0), (-1,-1), 3, colors.gray),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
        ])
    )

    paraStyle = ParagraphStyle('para_style', fontName='times_new_roman')

    p = Paragraph('Khách hàng: <b>Nguyễn Quốc Dũng</b> ĐT: <b>0939042969</b>', paraStyle)

    t3 = Table(data= [[p],
                      ['Địa chỉ giao hàng: Số 37, đường Trần Đại Nghĩa, ấp Mỹ Trung 1, Xã Mỹ Thạnh Trung, Huyện Tam Bình,\nVĩnh Long'],
                      ['Tổng thu người nhận: 105.900 gồm tổng sp 80.000 + cước ship COD 25.900'],
                      ['Đối tác: Tự vận chuyển']],
                      colWidths=[16*cm])

    t3.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'times_new_roman'),
        #('GRID', (0,0), (-1,-1), 1, colors.black),
        #('ALIGN', (0,0), (-1,-1), 'CENTER'),
        #('VALIGN', (0,0), (-1,-1), 'MIDDLE')
        ])
    )

    t4 = Table(data= [['STT', 'Sản phẩm', 'Mã SP', 'KL', 'SL', 'Đơn\ngiá', 'Thành\nTiền', 'Chiết\nkhấu', 'Thanh\ntoán'],
                      ['1', 'Giải thuật và lập trình - Lê Minh\nHoàng/ 332tr.', 'lmhctdl', '520', '1', '80.000', '80.000', '', '80.000'],
                      ['Tổng', '', '', '520', '1', '80.000', '80.000', '', '80.000'],
                      ['Phí thu của khách (Cước VC + dịch vụ thu tiền COD): 25.900']],
                      colWidths=[0.8*cm, 6*cm, 1.5*cm, 1*cm, 0.6*cm, 1.5*cm, 1.5*cm, 1.5*cm, 1.5*cm])

    t4.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'times_new_roman'),
        ('SPAN', (0,2), (2,2)),
        ('SPAN', (0,-1), (-1,-1)),
        ('GRID', (0,0), (-1,-2), 1, colors.black),
        ('ALIGN', (0,0), (0,0), 'CENTER'),
        ('ALIGN', (4,0), (4,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,2), (0,2), 'RIGHT'),
        ('ALIGN', (0,-1), (0,-1), 'RIGHT'),
        ])
    )

    t5 = Table(data= [['Tổng SP', 'Chiết khấu', 'Phí thu khách', 'Đã chuyển khoảng', 'Tổng cần thu'],
                      ['80.000', '', '25.900', '', '105.900']],
                      colWidths=[3.2*cm, 3.2*cm, 3.2*cm, 3.2*cm, 3.2*cm])

    t5.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'times_new_roman'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ])
    )

    t6 = Table(data= [['Khiếu nại sau khi nhận hàng: Hotline\nSĐT hoặc Facebook', 'Người lập phiếu: Nguyễn Xuân Hoàng\nĐT: 0939049999'],
                      ['Link download CD, tài nguyên\nhttps://bit.ly/ictbook-download-CD', 'SHOP HỖ TRỢ XỬ LÝ MỌ VẤN ĐỀ\nSAU BÁN HÀNG']],
                      colWidths=[9*cm, 7*cm])

    t6.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'times_new_roman'),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
        ])
    )

    elements.append(Table([[t],
                           [t2],
                           [t3],
                           [t4],
                           [t5],
                           [t6],
                          ]))
    # write the document to disk
    doc.build(elements)

    # pdf.showPage()
    # pdf.save()

    
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
