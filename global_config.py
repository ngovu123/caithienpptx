"""
A set of configurations used by the app.
"""
import logging
import os

from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class GlobalConfig:
    """
    A data class holding the configurations.
    """

    HF_LLM_MODEL_NAME = 'mistralai/Mistral-Nemo-Instruct-2407'
    LLM_MODEL_TEMPERATURE = 0.2
    LLM_MODEL_MIN_OUTPUT_LENGTH = 100
    LLM_MODEL_MAX_OUTPUT_LENGTH = 4 * 4096
    LLM_MODEL_MAX_INPUT_LENGTH = 750

    HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN', '')
    METAPHOR_API_KEY = os.environ.get('METAPHOR_API_KEY', '')

    LOG_LEVEL = 'DEBUG'
    COUNT_TOKENS = False
    APP_STRINGS_FILE = 'strings.json'
    PRELOAD_DATA_FILE = 'examples/example_02.json'
    SLIDES_TEMPLATE_FILE = 'langchain_templates/template_combined.txt'
    INITIAL_PROMPT_TEMPLATE = 'langchain_templates/chat_prompts/initial_template_v4_two_cols_img.txt'
    REFINEMENT_PROMPT_TEMPLATE = 'langchain_templates/chat_prompts/refinement_template_v4_two_cols_img.txt'

    LLM_PROGRESS_MAX = 90
    ICONS_DIR = 'icons/png128/'

    PPTX_TEMPLATE_FILES = {
        'Cơ bản': {
            'file': 'pptx_templates/Blank.pptx',
            'caption': '🟠 Tạo bài thuyết trình tốt (Sử dụng [Hình ảnh ](https://unsplash.com/photos/AFZ-qBPEceA) của [cetteup](https://unsplash.com/@cetteup?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) trên [Unsplash](https://unsplash.com/photos/a-foggy-forest-filled-with-lots-of-trees-d3ci37Gcgxg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash))'
        },
        'Tạo bài thuyết trình ngắn gọn': {
            'file': 'pptx_templates/Minimalist_sales_pitch.pptx',
            'caption': '⚫ Độ tương phản cao'
        },
        'Công cụ tạo ra các bài thuyết trình tài liệu cho phòng họp hoặc hội nghị.': {
            'file': 'pptx_templates/Ion_Boardroom.pptx',
            'caption': '🔴 Đưa ra những lựa chọn thiết kế nổi bật'
        },
        'Phong cách đơn sắc thành phố': {
            'file': 'pptx_templates/Urban_monochrome.pptx',
            'caption': '⚪ Ngạc nhiên trong thế giới đơn sắc'
        },
    }

    # This is a long text, so not incorporated as a string in `strings.json`
    CHAT_USAGE_INSTRUCTIONS = (
        'Mô tả ngắn gọn chủ đề của bài thuyết trình của bạn trong hộp văn bản được cung cấp dưới đây.'
        ' Ví dụ:\n'
        '- Make a slide deck on AI.'
        '\n\n'
        'Subsequently, you can add follow-up instructions, e.g.:\n'
        '- Can you add a slide on GPUs?'
        '\n\n'
        ' You can also ask it to refine any particular slide, e.g.:\n'
        '- Make the slide with title \'Examples of AI\' a bit more descriptive.'
        '\n\n'
        'See this [demo video](https://youtu.be/QvAKzNKtk9k) for a brief walkthrough.\n\n'
        ' SlideDeck AI does not have access to the Web, apart for searching for images relevant'
        ' to the slides. Photos are added probabilistically; transparency needs to be changed'
        ' manually, if required.'
        '\n\n'
        'If you like SlideDeck AI, please consider leaving a heart ❤️ on the'
        ' [Hugging Face Space](https://huggingface.co/spaces/barunsaha/slide-deck-ai/) or'
        ' a star ⭐ on [GitHub](https://github.com/barun-saha/slide-deck-ai).'
    )


logging.basicConfig(
    level=GlobalConfig.LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
