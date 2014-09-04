__author__ = 'gengjie'
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pycurl
import json
def data_post(value):
    pc = pycurl.Curl()
    pc.setopt(pycurl.POST, 1)
    pc.setopt(pc.HTTPHEADER, ["Content-Type: application/json"])
    pc.setopt(pycurl.URL, 'http://www.baidu.com')
    data = json.dumps(value)
    pc.setopt(pc.POSTFIELDS, data)
    # pc.setopt(pycurl.HTTPPOST, [("Content-type:application/json", (pc.FORM_CONTENTS, value))])
    pc.perform()
    response_code = pc.getinfo(pycurl.RESPONSE_CODE)
    print response_code
    pc.close()

if __name__ == "__main__":
    value = {"add": {"doc": {"pid": 257, "prodesc": "Test20140826"}}}
    #value='&stream.body=<add><doc><field name="pid">257</field><field name="prodesc">Test 20140826</field></doc></add>'
    data_post(value)