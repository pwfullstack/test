# -*- coding: utf-8 -*-

import qiniu.config
import logging

from qiniu import Auth, put_data, etag, urlsafe_base64_encode

#需要填写你的 Access Key 和 Secret Key
access_key = '-jARJyewlbfHBIdRwOjY0C7mzruExER-00N_o1hH'
secret_key = 'M9XUOBT-L1UaXMIymOb7k6iqVK_Zz_7M7H0F9L8g'

#要上传的空间
bucket_name = 'python'


def storage(data):
    """
    七牛云存储上传文件接口
    """
    if not data:
        return None
    try:
        #构建鉴权对象
        q = Auth(access_key, secret_key)

        #生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name)
        ret, info = put_data(token, None, data)

    except Exception as e:
        logging.error(e)
        raise Exception("上传文件到七牛错误")
        

    if info and info.status_code != 200:
        raise Exception("上传文件到七牛错误")


    return ret["key"]

if __name__ == '__main__':
   storage(data)




