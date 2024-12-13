from zenrows import ZenRowsClient

client = ZenRowsClient("d97012c5fe5d247c24155d1d6224a01cd73cfa4a")
#url = "https://t.ly/Q1uF-"
url = "https://www.google.com/search?q=software+developer+jobs&sca_esv=a66cce0409c10300&sxsrf=ADLYWIIiDvI2p_5P6dHBFpqrOCH3zAYqyA%3A1726234038966&source=hp&ei=tj3kZv6oOOiD7M8P5tzZ8Q0&iflsig=AL9hbdgAAAAAZuRLxvjOMeXeDS6VUXjDsLFjSoByKx4o&oq=software+d&gs_lp=Egdnd3Mtd2l6Igpzb2Z0d2FyZSBkKgIIADIKECMYgAQYJxiKBTILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgAQyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEi_lwJQ6PYBWO6PAnAFeACQAQCYAVGgAeYGqgECMTO4AQPIAQD4AQGYAhKgAvIHqAIKwgIHECMYJxjqAsICBxAuGCcY6gLCAg4QLhiABBjHARiOBRivAcICBRAuGIAEwgIOEC4YgAQYsQMYgwEYigXCAgsQLhiABBjRAxjHAcICDhAAGIAEGLEDGIMBGIoFwgIIEAAYgAQYsQPCAggQLhiABBixA8ICDhAAGIAEGLEDGIMBGMkDwgILEAAYgAQYkgMYigXCAg4QABiABBixAxiSAxiDAcICCxAuGIAEGLEDGIMBwgILEC4YgAQYxwEYrwHCAgQQIxgnwgIREC4YgAQYsQMY0QMYgwEYxwGYAxCSBwIxOKAH5oQB&sclient=gws-wiz"

url += "&premium_proxy=true" + "&js_render=true" + "&proxy_country=us" + "&autoparse=true"

response = client.get(url)

print(response.text)