import os
from dotenv import load_dotenv
from openai import OpenAI

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

def ask_ai(question: str):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {"role": "system", "content": SYSTEM_PROMPT},

            {"role": "user", "content": question}

        ],

        temperature=0

    )

    return response.choices[0].message.content.strip()