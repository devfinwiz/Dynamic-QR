from distutils.command.upload import upload
import gradio as gr
from QR_Generator import generate_qr
import qrcode

def tutorial():
    url="https://github.com/devfinwiz/Dynamic-QRCode-Generator/raw/master/Tutorial.mp4"
    QRcode = qrcode.QRCode(version=1,box_size=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H
        )
    # adding URL or text to QRcode
    QRcode.add_data(url)
    # generating QR code
    QRcode.make()
    # adding color to QR code
    QRimg = QRcode.make_image(fill_color="white",back_color="black").convert('RGB')

    #QRimg.save('Tutorial.png')
    return QRimg


with gr.Blocks(title="Dynamic-QR",css="#heading{background-color:#32a8a8}") as demo:

    gr.Label(elem_id="heading",value="DYNAMIC-QR",label="Title")

    with gr.Tab("Input"):
        text_input = gr.Textbox(label="URL",placeholder="URL To Be Mapped To QR code")
        color_input = gr.ColorPicker(label="Pick A Color")
        status=gr.Textbox(label="Status")
        text_button = gr.Button("Generate QR Code",elem_id="generate_qr")

    with gr.Tab("Output"):
        with gr.Row():
            image_output = gr.Image(label="QR Code").style(height=350,width=500)

    with gr.Tab("View Demo"):
        with gr.Row():
            tut_button=gr.Button("View Demo Usage")
            demo_video = gr.Image(label="Demo").style(height=350,width=500)

        gr.Label("Scan The Code For Demo Tutorial")

    tut_button.click(tutorial,inputs=[],outputs=[demo_video])
    text_button.click(generate_qr, inputs=[text_input,color_input], outputs=[status,image_output])
    
demo.launch()

