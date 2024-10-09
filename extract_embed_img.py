import fitz
import argparse
import os

def extract_embeded_img(pdf_path, paper_idx, img_path):
    doc = fitz.open(pdf_path)

    img_cnt = 0
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        images = page.get_images(full=True)
        
        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            img_cnt += 1
            with open(os.path.join(img_path, f"P-{paper_idx}-O{img_cnt}.{image_ext}"), "wb") as image_file:
                image_file.write(image_bytes)

parser = argparse.ArgumentParser(description="Extract embedded images from a PDF document")
parser.add_argument("--pdf", type=str, help="Path to the PDF document")
parser.add_argument("--index", type=int, help="Index of the paper")
parser.add_argument("--output", type=str, help="Path to save the extracted images")
args = parser.parse_args()
extract_embeded_img(args.pdf, args.index, args.output)