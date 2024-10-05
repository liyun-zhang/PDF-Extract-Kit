import os
import fitz
import numpy as np
from tqdm import tqdm
from PIL import Image
fitz.TOOLS.set_aa_level(0)

def load_pdf_fitz(pdf_path, dpi=600):
    images = []
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        page = doc[i]
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pm = page.get_pixmap(matrix=mat, alpha=False)

        # If the width or height exceeds 9000 after scaling, do not scale further.
        if pm.width > 9000 or pm.height > 9000:
            pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)

        img = Image.frombytes("RGB", (pm.width, pm.height), pm.samples)
        images.append(np.array(img))
    return images


if __name__ == '__main__':
    images = load_pdf_fitz("../../local/43-main.pdf")
    for idx, img in enumerate(images):
        if idx == 14:
            Image.fromarray(img).save(os.path.join("data/input", "43-main.pdf".replace(".pdf", f"_600.png")))