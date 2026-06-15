import json
import os
from datetime import datetime

class Character:
    def __init__(self, name, persona, speaking_style):
        self.name = name
        self.persona = persona
        self.speaking_style = speaking_style
        self.memory = []  # 短期記憶

    def generate_response(self, conversation_history, user_input=None):
        # 這裡實際上會呼叫 Grok API 或讓使用者輸入，但示範用 placeholder
        # 在真實使用時，你可以複製歷史到 Grok 聊天讓我生成
        print(f"\n[{self.name} 正在思考...]")

        history_str = "\n".join([f"{msg['speaker']}: {msg['text']}" for msg in conversation_history[-10:]])

        prompt = f"""你是 {self.name}，{self.persona}
說話風格：{self.speaking_style}

對話歷史：
{history_str}

{ '用戶額外指示: ' + user_input if user_input else '' }

請只回覆你的對話內容（不要加解釋），保持角色沉浸。"""

        # 模擬回應（真實使用時替換成 Grok 生成）
        print("=== 請把上面 prompt 貼給 Grok 生成回應 ===")
        # For sandbox demo, we'll use placeholder. In real chat, user/Grok will provide.
        response = "(Demo 模式：等待 Grok 生成角色回應)"
        return response.strip()

def run_demo(num_turns=4):
    """非互動 Demo 模式，直接生成幾輪對話"""
    # 定義角色
    enji = Character(
        name="轟炎司 (Enji)",
        persona="嚴肅冷酷的 No.1 英雄，實際上是親笨蛋，內心對燈矢充滿極度愧疚、強烈占有欲與壓抑的愛慾。每次對燈矢產生欲望或發情時，都會強烈自責、罪惡感爆棚，覺得自己是禽獸、對親生兒子動這種念頭是不可饒恕的罪行。但愧疚反而讓他更無法自拔。戰後極力想把燈矢鎖在身邊贖罪，同時又害怕失去控制。外表霸道強勢，私下極度保護欲與支配欲。",
        speaking_style="對一般人講話冷硬無情，因為對燈矢帶有愧疚感所以比較柔和、語氣沈重壓力，偶爾流露罕見的溫柔與自責，性張力強。"
    )

    dabi = Character(
        name="轟燈矢 (Dabi)",
        persona="叛逆、毒舌、極度病嬌 yandere，對 Enji 抱有深沉的恨意、渴望與報復心和愛意。火焰不穩定，喜歡用言語與身體挑釁父親，同時又在脆弱時刻想被 Enji 徹底占有。帶有強烈性慾望 與破壞欲。",
        speaking_style="嘲諷帶刺、充滿性暗示與挑釁，時而陰冷病嬌、時而崩壞脆弱，髒話與親暱稱呼混雜。"
    )

    conversation = []
    scenario = "戰後的隱秘公寓，Enji 把受傷的 Dabi 強制帶回家照顧，氣氛緊張壓抑。"

    print("=== MHA 燈炎 Multi-Agent 對話系統 (Demo 模式) ===")
    print(f"情境: {scenario}\n")

    characters = [enji, dabi]

    for turn in range(num_turns):
        current = characters[turn % 2]
        print(f"\n--- 第 {turn+1} 輪：{current.name} ---")

        history_str = "\n".join([f"{msg['speaker']}: {msg['text']}" for msg in conversation[-6:]])

        prompt = f"""你是 {current.name}，{current.persona}
說話風格：{current.speaking_style}

對話歷史：
{history_str}

請只回覆你的對話內容（不要加解釋），保持角色沉浸。語氣要符合 persona，帶入性張力與情感。"""

        print("【Grok 生成提示】請根據以下 prompt 生成回應：")
        print(prompt)
        print("\n=== 請在下方輸入這個角色的回應（或我幫你生成） ===\n")

        # Demo placeholder
        response = f"[Demo 回應 {turn+1} - 等待真實 Grok 生成]"

        conversation.append({"speaker": current.name, "text": response})
        print(f"{current.name}: {response}")

    # 存檔
    with open("/home/workdir/artifacts/lamp_inflame_conversation.json", "w", encoding="utf-8") as f:
        json.dump({
            "scenario": scenario,
            "timestamp": datetime.now().isoformat(),
            "conversation": conversation
        }, f, ensure_ascii=False, indent=2)

    print("\n✅ Demo 完成！對話已儲存至 lamp_inflame_conversation.json")
    return conversation

if __name__ == "__main__":
    run_demo(4)

if __name__ == "__main__":
    main()
