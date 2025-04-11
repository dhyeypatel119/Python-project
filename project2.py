import gradio as gr
import google.generativeai as genai

# 🔑 API setup
genai.configure(api_key="AIzaSyBr063I1Fa_ZwEi7nPEoJ0r6ToHii_yEUU")
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_names(domain, keywords, tone, emojis):
    if not domain or not keywords:
        return "⚠️ Please provide domain and keywords."

    prompt = f"""
You're a brand consultant AI. Create 5 unique, creative project names for a project in the domain of "{domain}", 
focused on "{keywords}", with a tone that is "{tone}". { 'Include emojis fitting the theme.' if emojis else 'Do not include emojis.' }

For each, give:
- Project Name (bold)
- A one-line creative explanation (italic)
Use markdown formatting and number the names.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"

# 💻 Gradio App
with gr.Blocks() as demo:
    gr.Markdown("## 🤖✨ Project Name Forge — *Gemini AI Edition*")
    gr.Markdown("Craft powerful, unique names for your next tech project — with AI magic ✨")

    with gr.Row():
        domain = gr.Textbox(label="📂 Project Domain", placeholder="e.g. AI, IoT, Robotics")
        tone = gr.Dropdown(["Creative", "Professional", "Funny", "Minimal", "Technical"], label="🎨 Tone", value="Creative")
    
    keywords = gr.Textbox(label="📝 Keywords / Description", placeholder="e.g. LPG gas detector using AI/ML")
    emojis = gr.Checkbox(label="🌈 Add Emojis?", value=True)

    output = gr.Markdown()
    btn = gr.Button("🎲 Generate Project Names")

    btn.click(fn=generate_names, inputs=[domain, keywords, tone, emojis], outputs=output)

demo.launch()
