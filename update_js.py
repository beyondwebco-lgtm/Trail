with open("script.js", "r") as f:
    js = f.read()

# Add safety checks
js = js.replace("modelViewer.addEventListener", "if (modelViewer) modelViewer.addEventListener")
js = js.replace("modelViewer.cameraOrbit", "if (modelViewer) modelViewer.cameraOrbit")
js = js.replace("cards.forEach", "if (cards.length > 0) cards.forEach")
js = js.replace("berriesFG.style.transform", "if (berriesFG) berriesFG.style.transform")
js = js.replace("berriesBG.style.transform", "if (berriesBG) berriesBG.style.transform")
js = js.replace("leavesBG.style.transform", "if (leavesBG) leavesBG.style.transform")

with open("script.js", "w") as f:
    f.write(js)
