import Formateur
import Apprenant
import Promotion
from Competence import Competence
from Validation import Validation

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

java=Competence(25, "java")
print(java)
python=Competence(26, "python")
print(python)
php=Competence(27, "php")
print(php)

validationjava=Validation(10, 1, 25, "validé", "Tiffanie")
print(validationjava)
validationpython=Validation(11, 1, 26, "auto-validé", "Tiffanie")
print(validationpython)
validationphp=Validation(12, 1, 27, "non-validé", "")
print(validationphp)