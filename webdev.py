from lxml import etree as et;
import requests;
from urllib.request import urlopen;

local = 'file:///home/pterik/github/russian-invading-casualties/webdev.html';
response = urlopen(local);

root = et.Element('html', version="5.0")
# Передайте родительский узел, имя дочернего узла,
# и любое количество дополнительных атрибутов
et.SubElement(root, 'head');
et.SubElement(root, 'title', bgcolor="red", fontsize='22');
et.SubElement(root, 'body', fontsize="15");
print(et.tostring(root, pretty_print=True).decode("utf-8"));
for e in root:
    print(e.tag);
root.set('newAttribute', 'attributeValue')
# Распечатываем root снова, чтобы увидеть, был ли добавлен новый атрибут
print(et.tostring(root, pretty_print=True).decode("utf-8"))
print(root.get('newAttribute'))
print(root[1].get('alpha')) # root[1] accesses the `title` element
print(root[1].get('bgcolor'))
root = et.Element('html', version="5.0")
et.SubElement(root, 'head')
et.SubElement(root, 'title', bgcolor="red", fontsize="22")
et.SubElement(root, 'body', fontsize="15")
# Добавить текст в Elements и SubElements
root.text = "This is an HTML file"
root[0].text = "This is the head of that file"
root[1].text = "This is the title of that file"
root[2].text = "This is the body of that file and would contain paragraphs etc"
print(et.tostring(root, pretty_print=True).decode("utf-8"))

for i in range(len(root)):
    if (len(root[i]) > 0):
        print("True")
    else:
        print("False")
for i in range(len(root)):
    print(et.iselement(root[i]))