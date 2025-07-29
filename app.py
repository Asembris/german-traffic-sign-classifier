import tensorflow as tf
import numpy as np
import gradio as gr
from PIL import Image
from tensorflow.keras.layers import InputLayer as _InputLayer
from tensorflow.keras.mixed_precision import Policy
class InputLayer(_InputLayer):
    def __init__(self, *args, batch_shape=None, **kwargs):
        if batch_shape is not None:
            # Keras 3’s InputLayer wants `input_shape`
            kwargs['input_shape'] = tuple(batch_shape[1:])
        super().__init__(*args, **kwargs)


custom_objs = {
    "InputLayer": InputLayer,
    "DTypePolicy": Policy
}


model = tf.keras.models.load_model("model.h5", custom_objects=custom_objs,compile=False)


mapping = {}
with open("class_mapping.txt", "r") as f:
    for line in f:
        idx, name = line.strip().split(":", 1)
        mapping[int(idx)] = name.strip()


def preprocess(img: Image.Image):
    img = img.resize((32, 32))
    arr = np.array(img, dtype="float32") / 255.0
    return np.expand_dims(arr, 0)

def classify(image):
    x = preprocess(image)
    preds = model.predict(x)[0]
    class_id = int(np.argmax(preds))
    return { mapping[class_id]: float(np.max(preds)) }


iface = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=1, label="Prediction"),
    title="German Traffic‑Sign Classifier",
    description="Upload an image; returns the most likely class and confidence."
)

if __name__ == "__main__":
    iface.launch(share=True)
