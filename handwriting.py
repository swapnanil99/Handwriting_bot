import pywhatkit as pw 

text = "Hello, this is a handwritten message!"
# Generate handwritten image
pw.text_to_handwriting(text, "demo.png", rgb=(0, 0, 255))
# Display the generated image
print("Handwritten message saved as.")
