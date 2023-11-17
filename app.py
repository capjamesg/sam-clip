from autodistill_clip import CLIP
from autodistill.detection import CaptionOntology
from autodistill_grounded_sam import GroundedSAM
import supervision as sv

from autodistill.core.custom_detection_model import CustomDetectionModel
import cv2

classes = ["McDonalds", "Burger King"]


SAMCLIP = CustomDetectionModel(
    detection_model=GroundedSAM(
        CaptionOntology({"logo": "logo"})
    ),
    classification_model=CLIP(
        CaptionOntology({k: k for k in classes})
    )
)

IMAGE = "logo.jpg"

results = SAMCLIP.predict(IMAGE)

image = cv2.imread(IMAGE)

annotator = sv.MaskAnnotator()
label_annotator = sv.LabelAnnotator()

labels = [
    f"{classes[class_id]} {confidence:0.2f}"
    for _, _, confidence, class_id, _ in results
]

annotated_frame = annotator.annotate(
    scene=image.copy(), detections=results
)
annotated_frame = label_annotator.annotate(
    scene=annotated_frame, labels=labels, detections=results
)

sv.plot_image(annotated_frame, size=(8, 8))
