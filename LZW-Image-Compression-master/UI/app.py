import streamlit as st
import os
import time
from LZW import LZW
from PIL import Image

st.set_page_config(page_title='img compression', layout="wide")

st.title('Image Compression using LZW')
st.markdown('---')

col1, col2 = st.columns(2)

with col1:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTsLYff7B9acyeArjgao7z20CGJh4FrjOgzuB_TwCbpA-H1njc3HiMY79J3MoZe6ktU90&usqp=CAU')

with col2:
    st.markdown('Image compression is a critical aspect of managing and transmitting visual dataefficiently.')
    st.markdown('This project explores the realm of image compression with a specific focus on the Lempel-Ziv-Welch (LZW) method.')
    st.markdown('Lossless compression technique that aims to reduce the size of image fileswhile preserving image quality. ')
    st.markdown('LZW is a renownedb It is a dictionary-based algorithm that excels at retaining the integrity of every pixel in the original image.')

st.sidebar.write('Developed by ')
st.sidebar.write('Krithika L - 21PD19')
st.sidebar.write('Sanjana R - 21PD31')


st.title('Compress an Image')
with st.subheader('Upload Image'):
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    upload_dir = "LZW-Image-Compression-master/LZW-Image-Compression-master/Images/"
    if uploaded_image is not None:
        image1 = Image.open(uploaded_image)
        image1.save("D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/Images/image.jpg")

        jpeg_image = Image.open("D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/Images/image.jpg")
        tiff_path = "D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/Images/image_tif.tif"
        jpeg_image.save(tiff_path,"TIFF")

# compressor = LZW(os.path.join("../Images","small.tif"))
compressor = LZW("D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/Images/image_tif.tif")
compressor.compress()

decompressor = LZW("D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/UI/CompressedFiles/image_tifCompressed.lzw")
decompressor.decompress()

# Display the uploaded image
st.markdown('---')
st.subheader('Original Image')
image1 = Image.open("D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/Images/image.jpg")
st.image(image1, caption='Uploaded Image', use_column_width=True)

st.markdown("---")
st.subheader('Decompressed Image')
image2  = Image.open("D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/UI/DecompressedFiles/image_tifDecompressed.tif")
st.image(image2, caption='Decompressed Image', use_column_width=True)

st.markdown("---")
st.subheader('Compression Benefits')
file_path = "D:/Lab_Main/Sem_5/Data Compression/package/LZW-Image-Compression-master/LZW-Image-Compression-master/UI/compressionBenefits.txt"
with open(file_path, "r") as file:
    for line in file:
        st.write(line)

