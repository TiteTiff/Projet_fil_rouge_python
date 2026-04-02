from Utilisateur import Utilisateur


class Promotion():
	def __init__(self)->None:
		self.utilisateur:list[Utilisateur]

	def ajouter_utilisateur(self,utilisateur:Utilisateur)->None:
		self.utilisateur.append(utilisateur)

	def __add__(self, promotion_deux:Promotion)->Promotion:
		nouvelle_promotion = Promotion()
		nouvelle_promotion.utilisateur = self.utilisateur+promotion_deux.utilisateur
		return nouvelle_promotion

	def __str__(self)->str:
		utilisateur= ", ".join(str(u) for u in self.utilisateur)
		return f"Promotion : {utilisateur}"

