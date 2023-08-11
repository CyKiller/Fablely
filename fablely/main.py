from flask import Flask, request, jsonify
from novel_generator import NovelGenerator
from dialogue_enhancer import DialogueEnhancer
from script_transitioner import ScriptTransitioner
from embedding_storage import EmbeddingStorage
from custom_agent import CustomAgent
from utils import setup_logger

app = Flask(__name__)
logger = setup_logger("fablely", "fablely.log")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    writing_style = data.get('writing_style', '')
    chapter_count = data.get('chapter_count', 1)
    genre = data.get('genre', '')

    dialogue_enhancer = DialogueEnhancer(prompt)
    script_transitioner = ScriptTransitioner(prompt)
    embedding_storage = EmbeddingStorage()
    custom_agent = CustomAgent()

    novel_generator = NovelGenerator(prompt, writing_style, chapter_count, genre, 
                                     dialogue_enhancer, script_transitioner, 
                                     embedding_storage, custom_agent)
    
    try:
        novel = novel_generator.generate_novel()
        return jsonify({'novel': novel}), 200
    except Exception as e:
        logger.error(f"Error generating novel: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
