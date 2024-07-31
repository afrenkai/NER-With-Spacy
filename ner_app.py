import spacy
from spacy import displacy
import gradio as gr

# Load the transformer model
nlp = spacy.load("en_core_web_trf")

def perform_ner(text):
    doc = nlp(text)
    
    # Generate HTML visualization
    html = displacy.render(doc, style="ent", page=False)
    
    # Extract entities for text output
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return html, entities

# Define Gradio interface
iface = gr.Interface(
    fn=perform_ner,
    inputs=gr.Textbox(lines=5, label="Enter text for NER"),
    outputs=[
        gr.HTML(label="Visualization"),
        gr.JSON(label="Entities")
    ],
    title="Named Entity Recognition with spaCy",
    description="Enter some text to identify named entities using the en_core_web_trf model.",
)

# Launch the app
iface.launch()