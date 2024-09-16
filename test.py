from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import qrcode
import streamlit as st
import pandas as pd
import os

def create_pdf_with_vcard(name, loading_advice_no, quantity, product, filename):
    # Create the vCard data
    vcard_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
NOTE:Loading Advice No: {loading_advice_no}, Quantity: {quantity}, Product: {product}
END:VCARD
"""

    # Generate the QR code with vCard data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')

    # Save the QR code to an image file
    qr_img.save("qr_code_vcard.png")

    # Create the PDF
    pdf_canvas = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Draw the text fields on the PDF
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(100, height - 100, f"Name: {name}")
    pdf_canvas.drawString(100, height - 140, f"Loading Advice No: {loading_advice_no}")
    pdf_canvas.drawString(100, height - 180, f"Quantity: {quantity}")
    pdf_canvas.drawString(100, height - 220, f"Product: {product}")

    # Draw the QR code on the PDF
    pdf_canvas.drawImage("qr_code_vcard.png", 400, height - 300, width=150, height=150)

    # Finalize the PDF
    pdf_canvas.showPage()
    pdf_canvas.save()

# Example usage




name = st.text_input("Name: ","")
loading_advice_no= st.text_input("Loading Advice: ","")
quantity= st.text_input("Quantity: ","")
product= st.text_input("Product: ","")
filename="output_vcard.pdf"


# create_pdf_with_vcard(
#     name="John Doe",
#     loading_advice_no="LA123456",
#     quantity="100",
#     product="Safety Equipment",
#     filename="output_vcard.pdf"
# )

if st.button("Generate file"):
    create_pdf_with_vcard(name,
    loading_advice_no,
    quantity,
    product,
    filename)
    
    # Provide download link for the generated PDF
    with open(filename, "rb") as pdf_file:
        st.download_button(
            label="Download PDF",
            data=pdf_file,
            file_name=filename,
            mime="application/pdf"
        )

    # Clean up the generated PDF file
    os.remove(filename)
