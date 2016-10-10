from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.response import TemplateResponse
import urllib.parse
from django.http import HttpResponse, HttpResponseRedirect
import pycurl
from io import StringIO
import io
import certifi




# Create your views here.
def pay(request):
	url = 'http://127.0.0.1:8000/invoke/'
	values = {
			"api_key": "3413-4198-6419-7575",
			"api_secret": "u&bNeUoO%&Brz4Lw0U0+Atx1g(Z%8xd=2q^D43tng57YplGYH6",
			"amount":"10",}
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8') # data should be bytes
	req = urllib.request.Request(url, data)
	resp = urllib.request.urlopen(req)
	respData = resp.read()

	print(respData)
	return HttpResponse(respData)
def makepay(request):
	buf = io.BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, 'http://127.0.0.1:8000/invoke/')
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.setopt(c.POSTFIELDS, 'amount=100&api_key=3413-4198-6419-7575')
	c.setopt(c.VERBOSE, True)
	c.perform()
	a= buf.getvalue()
	print(a)
	buf.close()
	return HttpResponse(a)





