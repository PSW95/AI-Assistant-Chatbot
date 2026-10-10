from collections import deque
import re
from config import mem_limit


class store_mem:
    def __init__(self):
        self.history = deque(maxlen=mem_limit)



    @staticmethod
    def normalize_text(text):
        text = text.lower().strip()
        text = re.sub(r"[^\w\s]","",text)    
        return " ".join(text.split())

    def add_hist(self,user_msg,ai_msg):
        self.history.append({ "user":user_msg, "ai":ai_msg})


    def check_with_prev_ans(self,que):
        norm_que = self.normalize_text(que)

        for i in reversed(self.history):
            prev_que = self.normalize_text(i["user"])

            if norm_que == prev_que:
                return i["ai"]

        return None


    def get_hist(self):
        return list(self.history)




