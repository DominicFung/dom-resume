import fitz

if __name__ == "__main__":
  pdffile = "resume.pdf"
  doc = fitz.open(pdffile)

  for i in range(2):
    page = doc.load_page(i)
    pix = page.get_pixmap()
    output = f"img/resume-p{i+1}.png"
    pix.save(output)