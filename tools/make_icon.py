from PIL import Image, ImageDraw
from pathlib import Path
S=130
im=Image.new("RGB",(S,S),(22,28,45))
d=ImageDraw.Draw(im)
d.rounded_rectangle((4,4,125,125),radius=24,fill=(30,38,56),outline=(238,25,137),width=5)
# bright shield, symbolizes keeping developer access protected
d.polygon([(65,19),(104,34),(96,81),(65,106),(34,81),(26,34)],fill=(238,25,137))
d.polygon([(65,26),(96,39),(89,77),(65,97),(41,77),(34,39)],fill=(247,248,252))
# clock with contrasting hands
d.ellipse((45,43,85,83),fill=(22,28,45))
d.ellipse((50,48,80,78),fill=(249,250,253))
d.line((65,63,65,52),fill=(22,28,45),width=4)
d.line((65,63,75,69),fill=(22,28,45),width=4)
Path("app/icon.png").parent.mkdir(parents=True,exist_ok=True)
im.save("app/icon.png")
print("Wrote app/icon.png, 130x130 RGB")
