# ts-canny-project

Le groupe décide d'effectuer le projet numéro **2**, soit **Traitement d'image - Canny**.

## Descriptif

- On va lire une image quelconque 
- Illustration des composants RGB (image 2x2 avec (221) original, (222) R, (223) G et (224) B) 
- Illustration des composants CMY (image 2x2 avec (221) original, (222) C, (223) M et (224) Y) 
- Passage de l’image lue de la couleur au noir et blanc (Y=0.299∙R+0.587∙G+0.114∙B) 
- Détection de contour selon l’algorithme de Canny (https://fr.wikipedia.org/wiki/Filtre_de_Canny) 
- Calcul et illustration de la FFT des images avant et après filtrage

### Avancement

| Objectif                        | Fait |
|---------------------------------|------|
| Lire une image                  | Oui  |
| Illustrer composants RGB        | Oui  |
| Illustrer composants CMY        | Oui  |
| Passer l'image RGB -> Grayscale | Oui  |
| Détection Canny                 | Oui  |
| Calcul et illustration FFT      | 0%   |


## Modules

| Module        | Utilité                                          |
|---------------|--------------------------------------------------|
| file_selector | Permet de lister et choisir une image à analyser |
| plotter       | Définir toutes les méthodes de plot              |
| canny         | Canny Edge detector                              |

## Sources

- https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123

## Members

<table>
   <tr>
      <td>
         <a href="https://labinfo.ing.he-arc.ch/edouard.goffinet"><img width=140px src="https://secure.gravatar.com/avatar/dc1f4f69a0a8b698062a058b7f1bf5a3?s=800&d=identicon"><br>
         Goffinet Edouard</a>
      </td>
      <td>
         <a href="https://labinfo.ing.he-arc.ch/luca.laissue"><img width=140px src="https://secure.gravatar.com/avatar/11c7eac012d1aa910c8790345185e67e?s=800&d=identicon"><br>
         Laissue Luca</a>
      </td>
      <td>
         <a href="https://labinfo.ing.he-arc.ch/lucas.fridez"><img width=140px src="https://secure.gravatar.com/avatar/72c1469bf815bd4e0a858341571d5111?s=800&d=identicon"><br>
         Fridez Lucas</a>
      </td>
   </tr>
</table>
