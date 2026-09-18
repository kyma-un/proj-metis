from ultralytics import YOLO
from pathlib import Path

def main():
    # Absolute paths resolved to avoid paths issues
    ROOT = Path(__file__).resolve().parent.parent
    DATA = ROOT / "data" / "data.yaml"
    MODEL = ROOT / "models" / "yolo26x.pt"

    model = YOLO(MODEL)

    model.train(
        data=DATA,
        epochs=200,
        imgsz=640,
        batch=16,
        freeze=10,
        lr0=0.001,
        lrf=0.01,
        warmup_epochs=3, 
        mixup=0.0,
        cutmix=0.5,
        project="training_results",
        name="v1-4",
    )


if __name__ == "__main__":
    main()