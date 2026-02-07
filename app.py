import gradio as gr
import os

# Read the HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Create a Gradio interface that displays the HTML
with gr.Blocks(title="地球能量系統 - Earth Heat") as demo:
    gr.HTML(html_content)

# Launch the app
if __name__ == "__main__":
    demo.launch()
