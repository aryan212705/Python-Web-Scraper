import urllib.request
from bs4 import BeautifulSoup
link = "https://docs.python.org/3/library/math.html"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page,"lxml")
main_section = soup.find("div", class_ = "section")
module_name = main_section.find("h1").get_text()
module_desc = main_section.find("p").get_text()
print(module_name, "\n")
print(module_desc, "\n\n")
section_name = []
func_name = []
func_desc = []
for section in main_section.find_all("div", class_  = "section"):
    section_name.append(section.find("h2").get_text())
    name, desc = [], []
    for function in section.find_all("dl", class_ = "function"):
        name.append(function.find("dt").get_text())
        desc.append(function.find("dd").get_text())
    func_name.append(name)
    func_desc.append(desc)

for i in range(len(section_name)):
    print(section_name[i],"\n")
    for j in range(len(func_name[i])):
        print(func_name[i][j],"\n")
        print(func_desc[i][j])
