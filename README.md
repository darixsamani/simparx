# simpar
this is package for a simple paragraph recognition based on the morphology operator

## Screen

| Image   | MASK Image  | Image recognized  |
:-------------------------:|:-------------------------:|:-------------------------:|
|  ![Image](https://raw.githubusercontent.com/darixsamani/simpar_cli/main/img/simple_a26.jpg) | ![Mask](https://raw.githubusercontent.com/darixsamani/simpar_cli/main/img/mask.jpg)   | ![Image recognized](https://raw.githubusercontent.com/darixsamani/simpar_cli/main/img/simple_a26_r.jpg)


## How to Install

```
pip install simpar

```

## How to use


```python

import simpar


 simpar_instance = Simpar("./img/simple_a20.jpg")
 simpar_instance.start()
 simpar_instance.save_image("./img/reco")

```

 


## Next

![next](https://raw.githubusercontent.com/darixsamani/simpar_cli/main/img/next.png)

### Francais
  Nous faisons une reconnaissance de paragraphe basée sur une les opération morphologiques qui est une
  méthode analytique qui  est instable lorsque la structure de l'image est complexe dans la suite de notre travail nous allons 
  a partir des images et leurs masque entraîner une modelé d'intelligence artificielle pour
  générer les masques de reconnaissance de paragraphe d'image, Ainsi Nous allons mieux gérer la structure des images complexes

### English

We use a morphological operation for paragraph recognition. This analytical method becomes unstable with complex image structures. To handle complex structures, we'll use masks to model artificial intelligence for image paragraph recognition.

