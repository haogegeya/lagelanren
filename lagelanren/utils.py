#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 14:57
# @Author  : forhaogege@163.com

import re
import os
import json
import requests
from datetime import datetime
import markdown
from command_so.models import Content as CContent, Label
from five_two_zero.models import Content, Key, Question

def init():
    base_dir = r"C:\Users\Administrator\Downloads\linux-command-master\linux-command-master\command"
    labels = Label.objects.filter(name__in=("Linux", "shell"))
    for item in os.listdir(base_dir):
        with open(os.path.join(base_dir, item), "r", encoding="utf-8") as f:
            text = f.read()
            cmd = item.split(".")[0]
            summary = re.findall(r"===([\s\S]*?)#", text)[0].strip()
            summary = cmd + "---" + summary
            print(summary)
            if CContent.objects.filter(summary=summary).exists():
                continue
            text = markdown.markdown(text)
            if not text:
                continue
            content = CContent.objects.create(summary=summary, text=text)
            for label in labels:
                content.labels.add(label)
                content.save()

def init_five_two_zero():
    base_dir = r"C:\Users\Administrator\Desktop\data\content.json"
    with open(base_dir, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data["RECORDS"]:
            Content.objects.create(answer_id=int(item["answerId"]), author=item["author"], author_id=item["authorId"], city=item["city"], comment_count=int(item["commentCount"]),
                                   content=item["content"], create_time=datetime.fromtimestamp(int(item["createTime"])), update_time=datetime.fromtimestamp(int(item["updateTime"])), gender=item["gender"], head_url=item["headUrl"],
                                   is_picture=bool(int(item["isPicture"])), question_id=int(item["questionId"]), voteup_count=int(item["voteupCount"]), is_zhihu=True, is_activate=True)


def init_five_two_zero_key():
    base_dir = r"C:\Users\Administrator\Desktop\data\count.json"
    with open(base_dir, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data["RECORDS"]:
            Key.objects.create(key=item["key"], total=item["count"],create_time=item["createTime"], update_time=item["updateTime"])

def init_question():
    res = requests.get("https://www.zhihu.com/question/275359100")
    res.encoding = "utf-8"
    pattern = re.compile("""class=\\\\"internal\\\\"\\\\u003E([\s\S]*?)\\\\u003C[\s\S]*?(https:\\\\u002F\\\\u002Fwww.zhihu.com\\\\u002Fquestion\\\\u002F(\d*?))\\\\""")
    questionIdList = list(set(re.findall(pattern, res.text)))
    for item in questionIdList:
        print(item)
        Question.objects.create(question_id=int(item[2]), title=item[0], url=item[1].encode('utf-8').decode("unicode_escape"))

if __name__ == '__main__':
    base_dir = r"D:\github\linux-command-master\command"
    base_dir = r"C:\Users\EDY\Desktop\content.json"
    with open(base_dir, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data["RECORDS"]:
            if(item["author"] != "匿名用户"):
                break