### v1-2
Tiene los siguientes parametros:
    model.train(
        data=DATA,
        epochs=100,
        imgsz=640,
        batch=16,
        freeze=10,
        lr0=0.001,
        lrf=0.01,
        warmup_epochs=3,
        mixup=0.5,
        cutmix=0.5,
        project="training_results",
        name="v1",
    )

### v1-3 7 sep 1:13 p.m (COT) , 8:14 p.m (Francia)
Tiene los siguientes hiperparametros:
    model.train(
        data=DATA,
        epochs=100,
        imgsz=640,
        batch=8,
        freeze=10,
        lr0=0.001,
        lrf=0.01,
        warmup_epochs=3,
        mixup=0.5,
        cutmix=0.5,
        project="training_results",
        name="v1-3",
    )

### v1-3 7 sep 7:11 p.m (COT) , 2:11 a.m (Francia)
Tiene los siguientes hiperparametros:
    model.train(
        data=DATA,
        epochs=100,
        imgsz=640,
        batch=32,
        freeze=10,
        lr0=0.001,
        lrf=0.01,
        warmup_epochs=3,
        mixup=0.5,
        cutmix=0.5,
        project="training_results",
        name="v1-3",
    )

### v1-3 14 sep 
Tiene los siguientes hiperparametros:
    model.train(
        data=DATA,
        epochs=100,
        imgsz=640,
        batch=32,
        freeze=10,
        lr0=0.001,
        lrf=0.01,
        warmup_epochs=3,
        mixup=0.5,
        cutmix=0.5,
        project="training_results",
        name="v1-3",
    )

### v1-3 15 sep 
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