from playwright.sync_api import sync_playwright
import pytest

# @pytest.mark.api
def test_get_api():
    with sync_playwright() as p:
        # browser = p.chromium.launch()
        # context =  browser.new_context()
        # page = context.new_page()
        context = p.request.new_context()
        statusData = context.get("https://dummyjson.com/products")
        # print(statusData.json())
        print(statusData.status)
        print(statusData.status_text)
        assert statusData.status==200
        jsonData = statusData.json()
        assert jsonData["products"][0]["title"]=="Essence Mascara Lash Princess"

# @pytest.mark.api
def test_get_api_auth():
    with sync_playwright() as p:
        # browser = p.chromium.launch()
        # context =  browser.new_context()
        # page = context.new_page()
        context = p.request.new_context()
        # statusData = context.get("https://dummyjson.com/products",headers={"Authorization":"Bearer 123456"})
        statusData = context.get("https://dummyjson.com/products",headers={"x-api-key":"123456789"})
        # print(statusData.json())
        print(statusData.status)
        print(statusData.status_text)
        assert statusData.status==200
        jsonData = statusData.json()
        assert jsonData["products"][0]["title"]=="Essence Mascara Lash Princess"




# @pytest.mark.api
def test_get_api_basicauth():
    with sync_playwright() as p:
        # browser = p.chromium.launch()
        # context =  browser.new_context()
        # page = context.new_page()
        context = p.request.new_context(http_credentials={
            "username":"trupura",
            "password":"test123"
        })
        # statusData = context.get("https://dummyjson.com/products",headers={"Authorization":"Bearer 123456"})
        statusData = context.get("https://dummyjson.com/products")
        # print(statusData.json())
        print(statusData.status)
        print(statusData.status_text)
        assert statusData.status==200
        jsonData = statusData.json()
        assert jsonData["products"][0]["title"]=="Essence Mascara Lash Princess"



@pytest.mark.api
def test_post_api():
    with sync_playwright() as p:
        context = p.request.new_context()
        reqBody = {
            "title": "Essence Mascara Lash Princess",
            "description": "The Essence Mascara Lash Princess is a popular mascara known for its volumizing and lengthening effects. Achieve dramatic lashes with this long-lasting and cruelty-free formula.",
            "category": "beauty",
            "price": 9.99
        }
        statusData = context.post("https://dummyjson.com/products/add",data=reqBody)
        # print(statusData.json())
        print(statusData.status)
        print(statusData.status_text)
        assert statusData.status==201
        jsonData = statusData.json()
        assert jsonData["title"]=="Essence Mascara Lash Princess"