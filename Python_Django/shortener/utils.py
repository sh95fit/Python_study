from shortener.models import ShortenedUrls, Users
from django.db.models import F

from django.http.response import JsonResponse

from rest_framework.response import Response


from datetime import datetime, timedelta


from shrinkers.settings import EMAIL_ID, EMAIL_PW
from time import time
import yagmail  # pip install yagmail


def url_count_changer(request, is_increase: bool):
    count_number = 1 if is_increase else -1
    Users.objects.filter(user_id=request.user.id).update(
        url_count=F('url_count') + count_number)


# ?    return JsonResponse(status=status, data=dict(msg="ok"))
def MsgOk(status: int = 200):
    return Response({"msg": "ok"}, status=status)


def get_kst():
    return datetime.utcnow() + timedelta(hours=9)


email_content = """
<div style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;border:none;border-bottom:solid #EEEEEE 1.0pt;padding:0cm 0cm 6.0pt 0cm;background:white;'>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:11.25pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;background:white;border:none;padding:0cm;'><span style='font-size:25px;font-family:"Helvetica Neue";color:#11171D;'>{}님! Shrinkers TEST입니다.</span></p>
</div>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:11.25pt;margin-left:0cm;line-height:17.25pt;font-size:15px;font-family:"Calibri",sans-serif;background:white;vertical-align:baseline;'><span style='font-size:14px;font-family:"Helvetica Neue";color:#11171D;'>본 메일은 테스트용입니다.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;background:white;'><strong><span style='font-size:24px;font-family:"Helvetica Neue";color:#11171D;'>확인 후 삭제해주세요.</span></strong></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:11.25pt;margin-left:0cm;line-height:17.25pt;font-size:15px;font-family:"Calibri",sans-serif;background:white;vertical-align:baseline;'><span style='font-size:14px;font-family:"Helvetica Neue";color:#11171D;'>이상입니다.</span></p>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:11.25pt;margin-left:0cm;line-height:17.25pt;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;background:white;vertical-align:baseline;'><span style='font-size:14px;font-family:"Helvetica Neue";color:#11171D;'><img width="378" src="https://dl1gtqdymozzn.cloudfront.net/forAuthors/K6Sfkx4f2uH780YGTbEHvHcTX3itiTBtzDWeyswQevxp8jqVttfBgPu86ZtGC6owG.webp" alt="sample1.jpg" class="fr-fic fr-dii"></span></p>
<p>
<br>
</p>
"""


def send_email(**kwargs):
    mailing_list = kwargs.get("mailing_list", None)
    # print(mailing_list)
    content = kwargs.get("content", None)
    if mailing_list:
        yag = yagmail.SMTP({EMAIL_ID: "Shrinkers X Hun's"}, EMAIL_PW)
        # https://myaccount.google.com/u/1/lesssecureapps
        # contents = [email_content.format(mailing_list[0])]
        # yag.send(mailing_list[1], "E-mail TEST.", contents)
        contents = [email_content.format(
            mailing_list[0])] if not content else content
        yag.send(mailing_list[1], "안녕하세요, Hun's Shrinkers입니다.", contents)
