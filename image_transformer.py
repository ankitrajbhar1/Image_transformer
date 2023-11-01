import streamlit as st
import cv2
import numpy as np

st.title("Image Transformation App")

# Upload an image
image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image is not None:
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Affine transformation options
    transformation = st.selectbox("Select Transformation", ["None", "Translation", "Rotation", "Scaling", "Shearing"])

    if transformation != "None":
        image = cv2.imread(image.name)  # Load the image
        if image is not None:
            if transformation == "Translation":
                x_translation = st.slider("X Translation", -100, 100, 0)
                y_translation = st.slider("Y Translation", -100, 100, 0)
                translation_matrix = np.float32([[1, 0, x_translation], [0, 1, y_translation]])
                transformed_image = cv2.warpAffine(image, translation_matrix, (300, 300))

            elif transformation == "Rotation":
                angle = st.slider("Rotation Angle", -180, 180, 0)
                rotation_matrix = cv2.getRotationMatrix2D((150, 150), angle, 1)
                transformed_image = cv2.warpAffine(image, rotation_matrix, (300, 300))

            elif transformation == "Scaling":
                scaling_factor = st.slider("Scaling Factor", 0.1, 2.0, 1.0, step=0.1)
                scaling_matrix = np.float32([[scaling_factor, 0, 0], [0, scaling_factor, 0]])
                transformed_image = cv2.warpAffine(image, scaling_matrix, (300, 300))

            elif transformation == "Shearing":
                shear_factor = st.slider("Shear Factor", -1.0, 1.0, 0.0, step=0.1)
                shear_matrix = np.float32([[1, shear_factor, 0], [shear_factor, 1, 0]])
                transformed_image = cv2.warpAffine(image, shear_matrix, (300, 300))


            st.image(transformed_image, caption="Transformed Image", use_column_width=True)
        else:
            st.error("Failed to load the image. Please check the image file.")
    else:
        st.error("Please select a transformation to apply.")
