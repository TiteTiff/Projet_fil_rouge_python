import Utilisateur

class Promotion:
	def __init__(self):
		self.utilisateur=[]

	def ajouter_utilisateur(self,utilisateur:Utilisateur):
		self.utilisateur.append(utilisateur)

	def __add__(self, promotion_deux:Promotion):
		nouvelle_promotion = Promotion()
		nouvelle_promotion.utilisateur = self.utilisateur+promotion_deux.utilisateur
		return nouvelle_promotion

	def __str__(self):
		utilisateur= ", ".join(str(u) for u in self.utilisateur)
		return f"Promotion : {utilisateur}"

