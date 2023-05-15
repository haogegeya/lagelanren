#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 17:33
# @Author  : forhaogege@163.com

import re
import json
import requests
from urllib.parse import quote
if __name__ == '__main__':
    # base_url = "https://www.zhihu.com/api/v4/questions/{}/feeds?cursor=01ca7a773930faf26beba4bdd645ab5c&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=20&offset={}"
    base_url = "https://www.zhihu.com/api/v4/questions/{}/feeds?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset={}&limit=20&sort_by=updated"
    answerUrl = base_url.format(319319691, 0)
    # print(answerUrl)
    res = requests.get(answerUrl)
    # print(res.json())
    data = res.json()["data"]
    contentItem = {}
    # print(data)
    for item in data:
        item = item["target"]
        # print(item)
        # break
        contentItem["questionId"] = item["question"]["id"]
        contentItem["city"] = item["question"]["title"].split("的")[0].split("在")[-1].strip()
        contentItem["answerId"] = item["id"]
        contentItem["author"] = item["author"]["name"]
        contentItem["headUrl"] = item["author"]["avatar_url"]
        contentItem["authorId"] = item["author"]["url_token"]
        contentItem["gender"] = item["author"]["gender"]
        contentItem["voteupCount"] = item["voteup_count"]
        contentItem["commentCount"] = item["comment_count"]
        contentItem["createTime"] = item["created_time"]
        contentItem["updateTime"] = item["updated_time"]
        content = item["content"]
        content = ("").join(content.split("\n"))
        pattern = re.compile(r'<noscript>[\s\S]*?src=\"([\s\S]*?)"')
        result1 = re.findall(pattern, content)
        if result1:
            result2 = re.sub(r'<figure[\s\S]*?</figure>', "{}", content)
            imgList = []
            for item in result1:
                str = "<img src='{}'>".format(item)
                imgList.append(str)
            result2 = result2.format(*imgList)
            contentItem["content"] = result2
            contentItem["isPicture"] = 1
        else:
            contentItem["content"] = content
            contentItem["isPicture"] = 0
