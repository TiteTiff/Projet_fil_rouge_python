import Formateur
import Apprenant
import Promotion

formateur1 = Formateur.Formateur("Yoann", 1)
print(formateur1)


apprenant1= Apprenant.Apprenant("Tiffanie", 1, ["Java", "Python"])
print(apprenant1)
apprenant1.ajouter_competence(3)

try:
	apprenant1.ajouter_competence(3)
except ValueError as e:
	print(e)



promotion1 = Promotion.Promotion()
promotion1.ajouter_utilisateur(formateur1)

promotion2 = Promotion.Promotion()
promotion2.ajouter_utilisateur(apprenant1)

promotion3=promotion1+promotion2
print(promotion3)
