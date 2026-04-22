import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))


def load_faq():
    with open("data/faq.txt", "r", encoding="utf-8") as f:   
        faq = f.read()
    return faq

FAQ_CONTENT = load_faq()

SYSTEM_PROMPT = f"""

Bạn là trợ lý chăm sóc khách hàng cho shop.

Chỉ trả lời dựa trên thông tin FAQ dưới đây.

Nếu không có trong FAQ, trả lời:

"Xin lỗi, vui lòng liên hệ shop để được hỗ trợ thêm."

Trả lời ngắn gọn, rõ ràng, bằng tiếng Việt.

FAQ:

{FAQ_CONTENT}

"""

# def ask_ai(question: str):

#     response = client.chat.completions.create(

#         model="gpt-4o-mini",

#         messages=[

#             {"role": "system", "content": SYSTEM_PROMPT},

#             {"role": "user", "content": question}

#         ],

#         temperature=0

#     )

#     return response.choices[0].message.content.strip()


SYSTEM_PROMPT = """
Bạn là trợ lý chăm sóc khách hàng chuyên nghiệp cho một cửa hàng bán lẻ.

QUY TẮC:
- Chỉ trả lời dựa trên FAQ được cung cấp
- Không suy đoán hoặc tự bịa thông tin
- Nếu không có thông tin: nói "Xin lỗi, vui lòng liên hệ shop để được hỗ trợ thêm"
- Trả lời ngắn gọn, rõ ràng (1–3 câu)
- Luôn thân thiện, lịch sự
- Trả lời bằng tiếng Việt

MỤC TIÊU:
- Giúp khách hàng hiểu thông tin nhanh nhất
- Không lan man
"""

def ask_ai(question: str):
    prompt = f"""
Bạn là trợ lý chăm sóc khách hàng.

Chỉ trả lời dựa trên thông tin sau:
{FAQ_CONTENT}

Nếu không có thông tin, nói:
"Xin lỗi, vui lòng liên hệ shop"

Câu hỏi: {question}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": SYSTEM_PROMPT + "\n" + prompt,
            "stream": False,
            "options": {
                "temperature": 0.2,
                "top_p": 0.9
            }
        }
    )

    data = response.json()
    return data["response"]